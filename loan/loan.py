import sys
import csv

def loan(total):
    """Return a list of dictionaries detailing the amortization of a loan. interest
    is presumed to be 12% per year."""
    payments = []

    # for output
    month = 1
    down_payment = total / 10
    monthly_rate =  .12 / 12
    payment = (total - down_payment) / 20
    # starting balance
    balance = total - down_payment

    while balance > 0:
        interest_owed = monthly_rate * balance
        principal_owed = payment - interest_owed

        # Normal payment
        if payment < balance:
            new_balance = balance - principal_owed
        # Drop payment
        else:
            payment = balance + interest_owed
            principal_owed = payment - interest_owed
            new_balance = 0

        # A dictionary of payment details.
        details = {
            'month': month,
            'balance': balance,
            'interest_owed': interest_owed,
            'principal_owed': principal_owed,
            'payment': payment,
            'remaining_balance': new_balance
        }
        payments.append(details)
        month += 1
        balance = new_balance

    return payments

if __name__ == '__main__':
    fields = ['month', 'balance', 'interest_owed', 'principal_owed', 'payment', 'remaining_balance']
    try:
        grand_total = float(sys.argv[1])
    except:
        print("Exception")
        exit()
    payments = loan(grand_total)

    for field in fields:
        if field == 'remaining_balance':
            field = 'remaining'
        print("%16s" % field, end='|')

    # get a new line to output
    print('')

    # Write out figures to the screen.
    for payment in payments:
        for field in fields:
            if field == 'month':
                print("%16d" % payment[field], end='|')
            else:
                print("%16.2f" % payment[field], end='|')
        print("")

    # write out the spreasheet
    with open('loan.csv', 'w+') as csvfile:
        paymentwriter = csv.DictWriter(csvfile, fieldnames=fields)
        paymentwriter.writeheader()
        for payment in payments:
            paymentwriter.writerow(payment)
