print("sankar super market")
print("no 35,nehur street,tindivanam")
print("-------------------------------------------------------------------------------------------------------------------")
print("bill receipt")
print("-------------------------------")
s1=int(input("enter the serial number:"))
pr=str(input("enter the product:"))
rate=int(input("enter the rate:"))
qty=int(input("enter the quantity:"))
total=rate*qty
print("total amount",total)
gst=total*100/10
paid=total+gst
print("amount to be paid Rs.",paid)
