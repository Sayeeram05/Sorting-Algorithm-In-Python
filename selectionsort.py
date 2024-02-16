import random

def selection(l=[],lenght=int):
    minindex = 0
    for i in range(0,length):
        min = l[i]
        for j in range(i,length):
            if(min > l[j]):
                min = l[j]
                minindex = j
        l[minindex] = l[i]
        l[i]=min
        
        
        

print("Sort Algorithm\n\t1.Selection Sort\n\nSteps\n\t1.Enter the number of data\n\t2.Random list\n\t3.Sorted list\n")

length = int(input("Enter the length of the Data : "))  #get the lenght from user

l = list()   #empty list

print("\nBefore Sort : ",end="")
for i in range(length):     #loop(0 to length)
    l.append(random.randrange(1,100) )    #stores a random number in the l

print(*l,sep=", ")      # prints the list to the user with comma seperated

selection(l,length)

print("\n\nAfter Bubble Sort : ",end="")
print(*l,sep=", ")      # prints the list to the user with comma seperated