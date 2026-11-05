while True:
    amount = float(input("enter purchase amount: "))
    if amount <0:
        break
    if amount == 0:
        continue
    if amount > 1000:
        print("valid purchase, amount")