import os,random

os.system("cls")

def Partation(List,Left,Right):  
    Pivot = List[Left]   # Compare this value to other elements 
    Start = Left   # First Index of the list
    End = Right     # LAst Index of the list

    while(Start < End):   
        while(Start <= Right and List[Start] <= Pivot):  
            Start += 1  
                         # Start <= Right and List[End] > Pivot control out of index
        while(End >= Left and List[End] > Pivot):
            End -= 1
            
        if(Start < End):  # Swap start and end
            List[Start],List[End] = List[End],List[Start]

    List[Left],List[End] = List[End],List[Left]
 
    return End

def QuickSort(List,Left,Right):

    if(Left < Right):
        Pivot = Partation(List,Left,Right)

        QuickSort(List,Left,Pivot-1)
        QuickSort(List,Pivot+1,Right)  
    

if(__name__ == "__main__"):
    
    print('''Sort Algorithm 🎯
    3.Merge Sort
        Steps ⭐
            1.Enter the number of data
            2.Random list
            3.Sorted list\n''')

    while True:  # Runs until Get the correct Value

        try:  # To Handel the Run Time Errors 
            length = int(input("Enter the length of the Data : "))  #get the lenght from user            
            if(length > 0):
                break  # Loop Will stop 
            else:
                print("❌ Enter Positive Value (Greater Than 0)")
        except ValueError: # if the user entered other than integer 
            print("❌ Invalid Number")
    
    l = list()   #empty List

    print("\nBefore Sort : ",end="")
    for i in range(length):     #loop(0 to length)
        l.append(random.randrange(1,100) )    #stores a random number in the l

    print(*l,sep=", ")      # prints the List to the user with comma seperated

    QuickSort(l,0,length-1)

    print("\n\nAfter Quick Sort : ",end="")
    print(*l,sep=", ")      # prints the List to the user with comma seperated