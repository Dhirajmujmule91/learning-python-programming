# Write a program that takes total bill amount and number of friends as input. 
# Calculate how much each person will pay.
# Also print the datatype of each variable used.


TotalBill=int(input("Total Bill:"))
NumberofFriends=int(input("Friends"))

Contribution=(TotalBill/NumberofFriends)
print("Each will pay: ", Contribution)
print("Datatype of TotalBill variable is:", type(TotalBill))
print("Datatype of NumberofFriends is: ", type(NumberofFriends))
