#just remember, continue statment skip an iteration in loop, break statment stops the loop
#continue while loop combination
#if we use while loop and need to add some conditional statements to carry forward during the loop,
# a certain iteration can be hold and loop may be set as continue after that.

# lets go through this code to see.

i=0
while i<5:
    i=i+1 # iteration to have loop
    if i==3: #conditional statment
        print("Skipping 3")
        continue
    print(i)
