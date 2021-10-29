import inpay

charge = inpay.Charge("i8189010944132646309108259471370", "LdgcAeeru6A4HooHTyHbTds19AkJBvNnoK")

amount_of_a_single_installment = 250.0
number_of_installments = 4
# Can be up to 6
# amount_of_a_single_installment * number_of_installments cannot exceed 3000

charge_amount = 500.0
# No limit

charge.installmentCharge(float(amount_of_a_single_installment), int(number_of_installments))
# To charge in installments

charge.charge(float(charge_amount))
# To charge in a single payment
