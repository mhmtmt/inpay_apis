from inpay import Charge

customer_account_number = "account number"
receiver_api = "receiver wallet api number"

charge = Charge(customer_account_number, receiver_api)

amount_of_a_single_installment = 250.0
number_of_installments = 4
# Can be up to 6
# amount_of_a_single_installment * number_of_installments cannot exceed 3000

second_receiver = "Wallet API No"
commission_percentage = 10

charge_amount = 500.0
# No limit

charge.installmentCharge(float(amount_of_a_single_installment), int(number_of_installments))
# To charge in installments

charge.charge(float(charge_amount))
# To charge in a single payment

charge.marketplaceCharge(charge_amount, second_receiver, commission_percentage)
# To charge in a single payment, get marketplace commission and send directly to seller account

charge.marketplaceInstallmentCharge(float(amount_of_a_single_installment), int(number_of_installments), second_receiver, commission_percentage)
# To charge in installments, get marketplace commission fee and send directly to seller account
