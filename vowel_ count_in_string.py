"""

***Problem Statement***

You need to make a program that counts the number of vowels in a given text.
The vowels are a, e, i, o, and u.

Take a string as input and output the number of vowels.

Sample Input:
this is great

Sample Output: 
4
"""

#code starts here !

text=input("Enter text to count vowels \n")
count=0
for vowels in text:
    if vowels =="a" or vowels=="e" or vowels=="i" or vowels=="o" or vowels=="u" or vowels =="A" or vowels=="E" or vowels=="I" or vowels=="O" or vowels=="U":
        count +=1
print ("No. of vowels are",count)
