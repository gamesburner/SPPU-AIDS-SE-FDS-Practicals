
std=[]
def storing_data(std):
    n=int(input("Enter Total No. of Students: "))
    for i in range(n):
        print("Enter percentage of ROLL NO. ",i+1," : ")
        a=float(input())
        std.append(a)
    

def slsort(arr):
    sortd=[]
    sortd=arr
    print("\nOriginal List: \n",sortd)
    l=len(sortd)
    
    for i in range(l):
        temp=0
        min=i

        for j in range(i+1,l):
            if sortd[min]>sortd[j]:
                min=j
        
        temp=sortd[i]
        sortd[i]=sortd[min]
        sortd[min]=temp
    
    return sortd


def bsort(arr):
    sortd=[]
    sortd=arr
    print("\nOriginal List: \n",sortd)
    l=len(sortd)
    
    for i in range(l):
        for j in range(l):
            if sortd[i]<sortd[j]:
                temp=sortd[i]
                sortd[i]=sortd[j]
                sortd[j]=temp
    return sortd
                

def top(arr):
    sortd=[]
    l=len(arr)
    count=0
    i=l
    while(count<5):
        sortd.append(arr[i-1])
        i=i-1
        count=count+1
    return sortd        
            

while(True):
    print("\n\n \t  M E N U ")
    print("1: Enter Student Percentage")
    print("2: Sort with SELECTION SORT")
    print("3: Sort with BUBBLE SORT")
    print("4: Exit")
    ch=int(input("Enter your choice: "))

    if ch==1:
        storing_data(std)
        print("\nStored Data:")
        print(std)
        print("--------------------------------------------------------")

    elif ch==2:
        if not std:
            print("\n\t\tEnter Student Percentage with option 1 \n")
        else:
            s1=slsort(std)
            print("Sorted List: \n",s1)
            cc=int(input("\nEnter 1 for top five scores\n"))
            
            if cc==1:
                print("Top five scores below: ")
                print(top(s1))
            else:
                print("\n\t\tBack to MENU")

    elif ch==3:
        if not std:
            print("\n\t\tEnter Student Percentage with option 1 \n")
        else:
            s1=bsort(std)
            print("Sorted List: \n",s1)
            cc=int(input("\nEnter 1 for top five scores\n"))
            
            if cc==1:
                print("Top five scores below: ")
                print(top(s1))
            else:
                print("\n\t\tBack to MENU")

    elif ch==4:
        break

    else:
        print("\n Enter valid choice \n")

