print("SANKAR INTERNATIONAL PVT.LTD")
print("NO 15, villupuram dist,Tamilnadu")
print("---------------------------------")
print("Employee payroll system")
print("---------------------------------")
id=int(input("Enter the employee ID:"))
name=str(input("Enter the employee name:"))
sal=int(input("Enter the employee salary:"))
print("Income")
bones=sal*20/100
print("Bones(20 percentage):",bones)
ot=sal*10/100
print("Overtime (10 percentage):",ot)
ta=sal*5/100
print("Travel alloovence(5 percentage):",ta)
gpay=sal+bones+ot+ta
print("Grosspay in Rupees:",gpay)
