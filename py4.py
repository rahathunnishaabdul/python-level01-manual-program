print("Nisha supermarket")
print("No:4,Nehru street,puducherry")
print("----------------------------")
print("bill receipt")
print("----------------------------")
sl=input("enter the sl:")
particular=input("Enter the Par:")
rate=input("Enter the rate:")
quantity=input("Enter the quantity:")
total=rate*quantity
print("total amount:",total)
GST("GST(10percentage):",GST)
paid=total+GST
print("amount to be paid:",paid)
