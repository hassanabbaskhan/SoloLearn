#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''Here is the problem statement.

You are making a ticketing system.
The price of single ticket is $100.
For children under age 3 years old, the ticket is free.

Your program needs to take the ages of 5 passengers as input
and output the total price of the tickets'''

total=0
i=0

while i<5: # no of iterations will be 0, 1, 2, 3, 4
    
    age=int(input("Enter the age \n"))
    i=i+1
    
    if age<=3:
        continue #if age is less than equal to 3, no change, just keep going,
        
    total=total+100 #otherwise the formula will be carried.
    
print("the total price will be $",total) #remove the indentation to display the total after inputs are done.


# In[ ]:




