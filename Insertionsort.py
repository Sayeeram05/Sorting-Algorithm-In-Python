import random   # random library

def InsertionSort(l=list(),length=int):
    for i in range(1,length):
        key = l[i]
        j = i-1
        while(l[j] > key and j >= 0):
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key


print("Sort Algorithm\n\t2.Insertion Sort\n\nSteps\n\t1.Enter the number of data\n\t2.Random list\n\t3.Sorted list\n")

length = int(input("Enter the length of the Data : "))  #get the lenght from user

l = list()   #empty list

print("\nBefore Sort : ",end="")
for i in range(length):     #loop(0 to length)
    l.append(random.randrange(1,100) )    #stores a random number in the l

print(*l,sep=", ")  # prints the list with comma seperation

InsertionSort(l,length)

print("\n\nAfter Bubble Sort : ",end="")
print(*l,sep=", ")      # prints the list to the user with comma seperated