def greet_customer():
    print("welcome to the lemonade stand!")
    print("fresh lemonade made just for you!")

greet_customer()


price_per_cup = float(input("enter the price per cup in $: "))
cupssold = int (input("enter number of cups sold"))

def caltotal(price, cups):
    total = price * cups
    return total

totcost = caltotal(price_per_cup, cupssold)

rounded_otal = round(totcost, 2)
print("total cost:",rounded_otal)

amountpaid = float(input("enter the amount paid by the user"))

def calculatechange(paid, total):
    change = paid - total
    return change
change_due =calculatechange (amountpaid, rounded_otal)
roundedchange= round(change_due,2)

def thankyoumessage(cups):
    if cups >= 5 :
        return "wow big order "
    else:
        return "thanks for buying"
closingmessage = thankyoumessage(cupssold)
print("")
print("===== LEMONADE STAND RECEIPT =====")
print("Price Per Cup:", price_per_cup)
print("Cups Sold:", cupssold)
print("Total Cost:", rounded_otal)
print("Amount Paid:", amountpaid)
print("Change Due:", roundedchange)
print(closingmessage)
print("===================================")

