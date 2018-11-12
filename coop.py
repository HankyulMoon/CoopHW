def find():
    
    f= open("D:/mytest/a.txt","r")
    line = f.readlines()
    f.close

    col = len(line[0])-1
    row=len(line)

    for i in range(row-1):
        line[i] = line[i][0:-1]
    #print("line :", line)

    for i in range(row):
        if col < (len(line[i])):
            col = len(line[i])


    #print("row : ",row)
    #print("col : ",col)

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

    #print("array : ",A)

    a1=0
    a2=0
    z1=0
    z2=0
    z3=0
    z4=0


    for i in range(row):
        for j in range(col):
            if(A[i][j] == '1'):
                a1 = j
                #print(i,j,a1)
                for z in range(j+1,col):
                    if(A[i][z] == '1'):
                        a2 = z
                        z1=[i,a1]
                        z2=[i,a2]
                        #print("h : ",i,a1,a2)
                        for x in range(i+1,row):
                            if(A[x][a1] == '1' and A[x][a2]=='1'):
                                
                                z3=[x,a1]
                                z4=[x,a2]
                                #print("TRUE")
                                #print("loca : ",z1,z2,z3,z4)
                                return True
                    
            
            a1=0
            a2=0
            a3=0
            a4=0
            

    #print("FALSE")
    return False


##################

if(find()):
    print("T")
else:
    print("F")
                        
                
                    




