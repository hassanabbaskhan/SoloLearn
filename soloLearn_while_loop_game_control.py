"""here is the game mode.
you are making a game, in which player tries to shoot something, so either he misses or hit it.
The player starts with 100 points. 
Each hit will add 10 points to the total while any miss will result in deduciton of points.

Generate program and take 4 inputs of either Hit or miss, and output the required."""

# here code starts
#start the code with no of initiator as zero.

i=0
points=100

#starting while loop, for total no of shoots=4;
#initiator i<4 means, starting from 0, 1, 2, 3

while i <4:
    shoot=input("Enter Hit, if it's done \n") #\n is for new lines
    if shoot=="Hit":
        points+=10
        i+=1
    else:
        points-=20
        i+=1
print("The Total Points will be",points)
