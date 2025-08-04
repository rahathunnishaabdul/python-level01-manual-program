print("Nisha International [p] ltd")
print("NO:15, nagpur dist,bangalore")
print("---------------------------")
print("Employee payroll system")
print("-----------------------")
id=int(input("Enter the Employee id:"))
name=input("Enter the name:")
salary=int(input("Enter the salary:"))
print("income")
bonus=salary*20/100
print("bonus(20):",bonus)
overtime=salary*10/100
print("overtime(10)",overtime)
travel=salary*5/100
print("travel-allowance(5per):",travel)
grosspay=salary+bonus+overtime+travel
print("grosspay in rupees:",grosspay)
