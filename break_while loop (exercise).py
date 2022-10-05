#this is any exercise of how to break the while loop using conditional statements
#starting with i=0

i=0
while True:
    print(i)
    i=i+1

    # here if we need to stop the loop after 5 iterations, we will use break as function to end the loop
    if i>=5: 
        print("Breaking Loop")
        break
