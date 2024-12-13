
def matric(r,c):    
    matrix=[]
    for i in range (r):
        row=[]
        print("Enter values for row ",i)
        for j in range(c):
            a=int(input("Enter values: "))
            row.append(a)
        matrix.append(row)
    return matrix


def ad(a,b):    
    result=[[0 for i in range(r)]for j in range(c)]
    for i in range(len(a)):
        for j in range(len(b)):
            result[i][j]=a[i][j]+b[i][j]
    return result


def sb(a,b):    
    result=[[0 for i in range(r)]for j in range(c)]
    for i in range(len(a)):
        for j in range(len(b)):
            result[i][j]=a[i][j]-b[i][j]
    return result


def mul(a,b):
    if len(a[0]) != len(b):
        print("Invalid matrix dimensions")
    
    result = [[0 for j in range(len(b[0]))] for i in range(len(a))]
    
    def m(a,b,result,i,j,k):
        
        if i >= len(a):
            return
        
        if j >= len(b[0]):
            return m(a, b, result, i+1, 0, 0)
        
        if k >= len(b):
            return m(a, b, result, i, j+1, 0)
        
        result[i][j] += a[i][k] * b[k][j]
        m(a, b, result, i, j, k+1)
    
    m(a,b,result,0,0,0)
    return result


def transpose(a):   
    result=[[0 for i in range(r)]for j in range(c)]
    for i in range(len(a)):
        for j in range(len(a)):
            result[i][j]=a[j][i]
    return result


while(True):
    print("\n\n\t\t M E N U :")
    print("1: Addition of 2 Matrices")
    print("2: Subtraction of 2 Matrices ")
    print("3: Multiplication of 2 Matrices")
    print("4: Transpose of a Matrix")
    print("5: Exit")
    p=int(input())

    
    if p==1:  
        print("For Matrix A: ")         
        r = int(input("Enter numbers of rows and columns: ")) 
        c=int(input())
        a = matric(r, c)

  
        print("For Matrix B: ")
        r = int(input("Enter numbers of rows and columns: ")) 
        c=int(input())
        b = matric(r, c)
       
        
        print("\tMatrix A is :")
        for i in (a):
            print(i)

        print("\tMatrix B is :")
        for i in (b):
            print(i)

        
        a1=ad(a,b)
        print("Addition of Matrix A and B is: ")         
        for i in (a1):     
            print(i)

    
    elif p==2:             
        print("For Matrix A: ")         
        r = int(input("Enter numbers of rows and columns: ")) 
        c=int(input())
        a = matric(r, c)

  
        print("For Matrix B: ")
        r = int(input("Enter numbers of rows and columns: ")) 
        c=int(input())
        b = matric(r, c)
    
        
        print("\tMatrix A is :")
        for i in (a):
            print(i)

        print("\tMatrix B is :")
        for i in (b):
            print(i)

        a1=sb(a,b)
        print("Subtraction of Matrix A and B is: ")          
        for i in (a1):      
           print(i)

    
    elif p==3:             
        print("For Matrix A: ")         
        r = int(input("Enter numbers of rows and columns: ")) 
        c=int(input())
        a = matric(r, c)

  
        print("For Matrix B: ")
        r = int(input("Enter numbers of rows and columns: ")) 
        c=int(input())
        b = matric(r, c)
    
        
        print("\tMatrix A is :")
        for i in (a):
            print(i)

        print("\tMatrix B is :")
        for i in (b):
            print(i)

        a1=mul(a,b)  
        print("Multiplication of Matrix A and B is: ")  
        for i in (a1):
            print(i)
    
        
    elif p==4:             
        print("For Matrix A: ")         
        r = int(input("Enter numbers of rows and columns: ")) 
        c=int(input())
        a = matric(r, c)


        print("\tMatrix A is :")
        for i in (a):
            print(i)

        a1=transpose(a)  
        print("Transpose of Matrix A is: ")  
        for i in (a1):
            print(i)
    
    elif p==5:
        break
    
    else:
        print("Invalid choice. Please choose a valid option.")

