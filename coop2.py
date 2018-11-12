#거리를 고려하지 않음
#ex) 000
#    000
#    이 올 때 4가지 경우를 찾는다. |_|-|같은 돌아가는 경우도 포함.


def find():
    
    f= open("D:/mytest/a.txt","r")
    line = f.readlines()
    f.close

    col = len(line[0])-1
    row=len(line)

    for i in range(row-1):
        line[i] = line[i][0:-1]
   
    for i in range(row):
        if col < (len(line[i])):
            col = len(line[i])


    A=[]

    for i in range(row):
        A.append([])

    for i in range(row):
        for j in range(col):
            if(len(line[i]) < col):
                if j >= (len(line[i])):
                    A[i].append('0')
                else:
                      A[i].append(line[i][j])
            else:
                A[i].append(line[i][j])

    return A

    
def ain(A,a,b,B):
    #print("a b = ",a,b)
    #print("A = ",A)

    row = len(A)
    col = len(A[0])
    #print(row,col)

    A[a][b]='1'
    
    
    up=1
    down=1
    left=1
    right=1
    if(a==0):
        if(b==0):
            right=A[a][b+1]
            down=A[a+1][b]
        elif(b==col-1):
            left=A[a][b-1]
            down=A[a+1][b]
        else:
            left=A[a][b-1]
            right=A[a][b+1]
            down=A[a+1][b]

    elif(a==row-1):
        if(b==0):
            right=A[a][b+1]
            up=A[a-1][b]
        if(b==col-1):
            left=A[a][b-1]
            up=A[a-1][b]
        else:
            left=A[a][b-1]
            right=A[a][b+1]
            up=A[a-1][b]

    elif(b==0):
        
        right=A[a][b+1]
        up=A[a-1][b]
        down=A[a+1][b]    
        

    elif(b==col-1):
        left=A[a][b-1]
        up=A[a-1][b]
        down=A[a+1][b]    
        

        
    else:
        left=A[a][b-1]
        up=A[a-1][b]
        down=A[a+1][b]
        right=A[a][b+1]
        
    #print(up,right,down,left)

    if(a==(row-1) and b==(col-1)):
        global cnt
        #cnt= cnt+1
        #print("end1")
        A[a][b]='0'
        B.append('1')
        return
    
    if(up=='1' and down=='1' and left=='1' and right=='1'):
        return

    if(down=='0'):
        ain(A,a+1,b,B)
    if(right=='0'):
        ain(A,a,b+1,B)
    if(left=='0'):
        ain(A,a,b-1,B)
    if(up=='0'):
        ain(A,a-1,b,B)

    A[a][b]='0'
    return
    
def final():
    #cnt=0;
    A=find()
    B=[]
    ain(A,0,0,B)
    return len(B)

########
print(final())
