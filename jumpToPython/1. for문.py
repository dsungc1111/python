scores = [100, 90, 60, 50, 40]

number = 0

for score in scores:
    number = number+1
    if score >= 65:
        print("accept")
    elif score < 65 and score >= 50:
        print("please wait")
    else:
        print("fail, sry..")
