import random   # random library

def BubbleSort(l=list(),length=int):    # function to perform sorting
    for i in range(length-1):
        for j in range(length-1-i):
            if(l[j]>l[j+1]):
                temp = l[j+1]
                l[j+1] = l[j]
                l[j] = temp


print("Sort Algorithm\n\t1.Bubble Sort\n\nSteps\n\t1.Enter the number of data\n\t2.Random list\n\t3.Sorted list\n")

length = int(input("Enter the length of the Data : "))  #get the lenght from user

l = list()   #empty list

print("\nBefore Sort : ",end="")
for i in range(length):     #loop(0 to length)
    l.append(random.randrange(1,100) )    #stores a random number in the l

print(*l,sep=", ")      # prints the list to the user with comma seperated

BubbleSort(l,length)    # call the BubbleSort function and pass the attributes

print("\n\nAfter Bubble Sort : ",end="")
print(*l,sep=", ")      # prints the list to the user with comma seperated