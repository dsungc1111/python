coffee = 10

while True:
    money = int(input("돈을 넣어주세요 : "))
    if money == 300:
        print("Here is coffee~")
        coffee = coffee - 1
    elif money > 300:
        print("coffee and change %dwon is here" % (money-300))
        coffee = coffee - 1
    else:
        print("money isn't enough, remain coffee : %d" % coffee)
    if coffee == 0:
        print("stop selling")
        break
