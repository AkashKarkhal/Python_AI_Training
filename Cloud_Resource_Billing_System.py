compute_hours = int(input("Enter compute hours: "))
storage_used = int(input("Enter storage used (GB): "))
plan = input("Enter support plan (Basic/Premium/Enterprise): ").lower()

if compute_hours <= 100:
    compute_cost = compute_hours * 5
elif compute_hours <= 200:
    compute_cost = (100 * 5) + ((compute_hours - 100) * 4)
else:
    compute_cost = (100 * 5) + (100 * 4) + ((compute_hours - 200) * 3)

if storage_used <= 500:
    storage_cost = storage_used * 2
else:
    storage_cost = (500 * 2) + ((storage_used - 500) * 1.5)

if plan == "basic":
    support_fee = 500

elif plan == "premium":
    support_fee = 1000
    compute_cost = compute_cost * 0.9

elif plan == "enterprise":
    support_fee = 2000
    storage_cost = storage_cost * 0.8

else:
    print("Invalid Plan")
    exit()

bill = compute_cost + storage_cost + support_fee

print("\n----- BILL DETAILS -----")
print("Compute Cost:", compute_cost)
print("Storage Cost:", storage_cost)
print("Support Fee:", support_fee)
print("Total Bill:", bill)