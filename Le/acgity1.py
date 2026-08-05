def totcalc(billamount, tip):
    total = billamount + (billamount * tip)
    return total
    total = round(total, 2)
    print(f"please pay ${total}")