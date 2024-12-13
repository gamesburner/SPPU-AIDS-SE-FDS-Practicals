
list_marks=[]

print(("Enter marks out of 100 according to roll no.  Enter 'A' for absent students during test"))

n=int(input("Enter total strength of class "))

for i in range(n):
    print("Enter Marks for ",i+1,": ")
    m=input()
    list_marks.append(m)
print(list_marks)


def avg(l):
    sum=0
    count=0
    for i in range(len(l)):
        if l[i]!='A':
            sum=sum+int(l[i])
            count+=1
    print("Avg marks of present students")
    print(sum/count)


def high(l):
    temp=0
    for i in range(len(l)):
        if l[i]!='A':
            if int(l[i])>=temp:
                temp=int(l[i])
   
    print("Highest score in class: ",temp)


def low(l):
    temp=100
    for i in range(len(l)):
        if l[i]!='A':
            if int(l[i])<=temp:
                temp=int(l[i])
    print("Lowest score in class: ",temp)
            

def absent_count(l):
    count=0
    for i in range(len(l)):
        if l[i]=='A':
            count+=1
    print("Total no of absent students: ",count)


def high_freq(l):
    count2=0
    markshf=l[0]
    for i in l:
        if i!='A':
            count1=l.count(i)
        if count1>count2:
            count2=count1
            markshf=i

   
    print("Marks ",markshf," repeated ",count2," times")


while(True):
    print("\n \t MENU ")
    print("1: Average Score of Class")
    print("2: Highest and Lowest Score of Class")
    print("3: Count of student absent during test")
    print("4: Marks with highest frequency")
    print("5: Exit")
    p=int(input("Enter your choice "))

    if p==1:
        avg(list_marks)
    
    elif p==2:
        high(list_marks)
        low(list_marks)
    
    elif p==3:
        absent_count(list_marks)
    
    elif p==4:
        high_freq(list_marks)
    
    elif p==5:
        break

    else:
        print("Enter correct option \n \n")
    
