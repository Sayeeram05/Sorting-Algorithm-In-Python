import random   # random library

def MergeSort(array):
    if len(array) > 1:   
        m = len(array) // 2  # 5 // 2 = 2  

        l1 = array[:m]   # l1 stores 0 to m-1
        l2 = array[m:]   # l2 stores m to last index
        
        MergeSort(l1)   # recursion of l1 array
        MergeSort(l2)   # recursion of l2 array

        i = j = k = 0   # i for l1 and j for l2 and k for array

        while(i < len(l1) and j < len(l2)):  # this loop insert the small value in the array
            """ print("l1 : ",end="")
            print(*l1)
            print("l2 : ",end="")
            print(*l2)
            print("array : ",end="")
            print(*array) """
            
            if(l1[i] <= l2[j]): 
                array[k] = l1[i]
                i += 1
                
            else:
                array[k] = l2[j]
                j += 1
                
            k += 1
            
            #print(f"1. i = {i} j = {j} k = {k}  arr[k] = {array[k]}\n")
        
        while(i < len(l1)):    # make the array in order next indexes of the inserted value

            """ print("l1 : ",end="")
            print(*l1)
            print("l2 : ",end="")
            print(*l2)
            print("array : ",end="")
            print(*array) """
            #print(f"2. i = {i} j = {j} k = {k}  arr[k] = {array[k]}\n")

            array[k] = l1[i]
            i += 1
            k += 1
            
        while(j < len(l2)):   # make the array in order next indexes of the inserted value

            """ print("l1 : ",end="")
            print(*l1)
            print("l2 : ",end="")
            print(*l2)
            print("array : ",end="")
            print(*array) """
            #print(f"3. i = {i} j = {j} k = {k} arr[k] = {array[k]}\n")

            array[k] = l2[j]
            j += 1
            k += 1
            


print('''Sort Algorithm 🎯
    3.Merge Sort
        Steps ⭐
            1.Enter the number of data
            2.Random array
            3.Sorted array\n''')

length = int(input("Enter the length of the Data : "))  #get the lenght from user

l = list()   #empty array

print("\nBefore Sort : ",end="")
for i in range(length):     #loop(0 to length)
    l.append(random.randrange(1,100) )    #stores a random number in the l

print(*l,sep=", ")      # prints the array to the user with comma seperated

MergeSort(l)

print("\n\nAfter Bubble Sort : ",end="")
print(*l,sep=", ")      # prints the array to the user with comma seperated