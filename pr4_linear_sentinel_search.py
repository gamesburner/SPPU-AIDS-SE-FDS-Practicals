
rolno=[]

print("Enter number of students present: ")

n=int(input())

for i in range(n):
    a=int(input("Enter the roll number: "))
    rolno.append(a)

print(rolno)

def lsearch(rolno):
    key=int(input("Enter roll no to search: "))
    l=len(rolno)
    for i in range(l):
        if rolno[i]!=key:
            pass
        else:
            print("Student was present for the program",i)
            break
        if (i==(l-1)):
            print("Student not found!!")


def ssearch(arr):
    key=int(input("Enter roll no to search: "))
    n=len(arr)

    last=arr[n-1]

    arr[n-1]=key
    i = 0

    while(arr[i]!=key):
	    i+=1
    
    arr[n-1]=last

    if ((i<n-1) or (arr[n-1]==key)):
         print("Student was present for the program", i)
    else:
         print("Student not found!!")
         

while(True):
     print("\n\t M E N U")
     print("\n1.Linear Search")
     print("2.Sequential Search")
     print("3.Exit")

     ch=int(input("Enter your choice: "))

     if(ch==1):
          lsearch(rolno)

     elif (ch==2):
         ssearch(rolno)

     elif ch==3:
          break
     
     else:
          print("Invalid choice")

