function is_server() {
    return ! (typeof window != 'undefined' && window.document);
}

if(!is_server()){
    console.log("%cInPay'i fraud protection politikamız nedeniyle yalnızca client-side olarak çalıştıramazsınız.", "color: red; font-size:25px;")
}

class Charge{
    constructor(sc_key, receiving_wallet){
        
        this.sender_wallet = sc_key;
        this.receiving_wallet = receiving_wallet
    }
    charge(amount){
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "http://172.105.248.143/api/charge", true)
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function() {
            if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
                return true;
            }
            else if(this.readyState === XMLHttpRequest.DONE){
                return false;
            }
        }
        xhr.send("wallet_sc_key={sckey}&receiving_wallet={receiving_wallet}&amount={amount}".replace("{sckey}", this.sender_wallet).replace("{receiving_wallet}", this.receiving_wallet).replace("{amount}", amount));
    }
    installmentCharge(installment_amount, total_months){
        today = new Date()
        today = today.getDate();
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "http://172.105.248.143/api/charge", true)
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function() {
            if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
                return true;
            }
            else if(this.readyState === XMLHttpRequest.DONE){
                return false;
            }
        }
        xhr.send("wallet_sc_key={sckey}&receiving_wallet={receiving_wallet}&installment_amount={amount}&total_months={total_months}&day_of_month={day_of_month}".replace("{sckey}", this.sender_wallet).replace("{receiving_wallet}", this.receiving_wallet).replace("{amount}", installment_amount).replace("{total_months}", total_months).replace("{day_of_month}", today));
    }
    marketplaceCharge(amount, second_receiver, commission_percentage){
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "http://172.105.248.143/api/charge", true)
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function() {
            if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
                return true;
            }
            else if(this.readyState === XMLHttpRequest.DONE){
                return false;
            }
        }
        xhr.send("wallet_sc_key={sckey}&receiving_wallet={receiving_wallet}&amount={amount}".replace("{sckey}", this.sender_wallet).replace("{receiving_wallet}", this.receiving_wallet).replace("{amount}", amount / 100 * (100 - amount)));
        xhr.send("wallet_sc_key={sckey}&receiving_wallet={receiving_wallet}&amount={amount}".replace("{sckey}", this.sender_wallet).replace("{receiving_wallet}", second_receiver).replace("{amount}", amount / 100 * amount));
    }
    marketplaceInstallmentCharge(installment_amount, total_months, second_receiver, commission_percentage){
        today = new Date()
        today = today.getDate();
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "http://172.105.248.143/api/charge", true)
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function() {
            if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
                return true;
            }
            else if(this.readyState === XMLHttpRequest.DONE){
                return false;
            }
        }
        xhr.send("wallet_sc_key={sckey}&receiving_wallet={receiving_wallet}&installment_amount={amount}&total_months={total_months}&day_of_month={day_of_month}".replace("{sckey}", this.sender_wallet).replace("{receiving_wallet}", this.receiving_wallet).replace("{amount}", installment_amount / 100 * (100 - commission_percentage)).replace("{total_months}", total_months).replace("{day_of_month}", today));
        xhr.send("wallet_sc_key={sckey}&receiving_wallet={receiving_wallet}&installment_amount={amount}&total_months={total_months}&day_of_month={day_of_month}".replace("{sckey}", this.sender_wallet).replace("{receiving_wallet}", second_receiver).replace("{amount}", installment_amount / 100 * commission_percentage).replace("{total_months}", total_months).replace("{day_of_month}", today));
    }
}
