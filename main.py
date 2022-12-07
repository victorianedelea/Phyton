print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
#print(type(bill_float))
bill = float(bill)

tips = int(input("How much tip would you like to give? 10,12, or 15? "))
#print(type(tips))
tips = int(tips)

people = input("How many people to split the bill? ")
#print(type(people))
people = int(people)

bill_with_tips = tips / 100 * bill + bill
bill_with_tips = float(bill_with_tips)

bill_per_person = bill_with_tips / people
bill_per_person = round(bill_per_person, 2)

print(f"Each person should pay: {bill_per_person}")



