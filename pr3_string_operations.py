
st=input("Enter the string: ")
s1=list(st)


def long_word(st):           
    slw=list(st.split(' '))
    long=''
    for i in slw:
        if(len(i))>(len(long)):
            long=i
    print(long)


def freq(st):                 
    lst=[]
    for i in st:
        lst.append(i)
    a=input("Enter character to find frequency: ")
    count=0
    for i in lst:
        if i==a:
            count+=1
    print("Highest frequency of ",a," is ",count)


def pal(st):                
    st1=st.replace(" ","")

    lst=[]
    for i in st1:
        lst.append(i)
    rev=''
    for i in range(len(lst),0,-1):
        rev=rev+lst[i-1]
    
    if(st1==rev):
        print("Palindrome")
    else:
        print("Not Palindrome")


def freqeach(st):             
    freq=list(st.split(' '))
    word=[]
    for i in freq:
        if i not in word:
            word.append(i)
    
    for a in word:
        count=0
        for i in freq:
            if i==a:
                count+=1
        print("Frequency of ",a," is ",count)

     
def app(st):              
    aps=list(st.split(' '))
    a=input("Enter substring to find index of: ")
    for i in range(len(aps)):
        if a==aps[i]:
            print("index is ",i+1)


while(True):
    print("\t M E N U")
    print("1: Find word with longest length")
    print("2: Find Frequency of particular char in given string")
    print("3: Find whether string is PALINDROME or  NOT")
    print("4: Find Frequency of each word")
    print("5: Find index of given substring")
    print("6: Exit")
    
    ch=int(input("Enter your choice"))


    if ch==1:
        long_word(st)

    elif ch==2:
        freq(st)
    
    elif ch==3:
        pal(st)
    
    elif ch==4:
        freqeach(st)

    elif ch==5:
        app(st)

    elif ch==6:
        break

    else:
        print("Enter correct choice")

