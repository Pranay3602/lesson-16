def total_calc(bill_amount, tip_percentage):
    total=bill_amount*(1+0.01*tip_percentage)
    total=round(total,2)
    print(total)
bill_amount=int(input("what is the final bill amount"))
tip_percentage=int(input("what is your tip percent"))
total_calc(bill_amount, tip_percentage)