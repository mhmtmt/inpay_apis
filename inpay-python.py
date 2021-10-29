import requests
import datetime


class Charge:
    def __init__(self, sc_key, receiving_wallet):
        self.sc_key = sc_key
        self.receiving_wallet = receiving_wallet

    def charge(self, amount):
        r = requests.post("http://172.105.248.143/api/charge", data={"wallet_sc_key": self.sc_key,
                                                                     "receiving_wallet": self.receiving_wallet,
                                                                     "amount": amount})
        if r.text == "Ödeme Onaylandı":
            return {"status": True, "reason_of_failure": "Success"}
        elif not r.ok:
            return {"status": False, "reason_of_failure": "Yetersiz cüzdan bakiyesi"}
        else:
            return {"status": False, "reason_of_failure": r.text}

    def installmentCharge(self, installment_amount, total_months):
        r = requests.post("http://172.105.248.143/api/createInstallmentCharge",
                          data={"wallet_sc_key": self.sc_key,
                                "receiving_wallet": self.receiving_wallet,
                                "installment_amount": installment_amount,
                                "total_months": total_months,
                                "day_of_month": datetime.datetime.today().day
                                })

        if r.text == "Ödeme Onaylandı":
            return {"status": True, "reason_of_failure": "Success"}
        elif not r.ok:
            return {"status": False, "reason_of_failure": "Yetersiz cüzdan bakiyesi"}
        else:
            return {"status": False, "reason_of_failure": r.text}
