'''Here is the problem statement.

You are making a ticketing system.
The price of single ticket is $100.
For children under age 3 years old, the ticket is free.

Your program needs to take the ages of 5 passengers as input
and output the total price of the tickets'''

total=0
i=5
while i>0:
    i=i-1
    age=int(input("Enter age \n"))
    if age>3:
        total+=100
print("The total price will be $",total)
