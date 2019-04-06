import numpy as np
import math as m

#funcion que genera una matriz identidad de n*n
def Identity(n):
    result= [[1 if j==i else 0 for j in range(n)] for i in range(n)]
    return result

#funcion que genera una matriz de ceros de n*n
def Ceros(n):
    return [[0 for i in range(n)] for j in range(n)]

#esta función calcula la matriz inversa de otra función en caso de existir
def inversa(A):
    if np.linalg.det(A)!=0:
        B=Adjunta(A).transpose()
        detA=np.linalg.det(A)
        return B/detA
    else:
        print('determinante = 0, no se puede')
        
#esta función calcula la matriz adjunta de una matriz        
def Adjunta(A):
    n=int(m.sqrt(A.size))
    print(np.array(A))
    trans=[[0 for i in range(n)] for k in range(n)]
    for I in range(n):
        for J in range(n):
            r=[[]for i in range(n-1)]
            y=0
            for i in range(n):
                if I!=i:
                    for j in range(n):
                        if J!=j:
                            r[y].append(A[i][j])
                    y+=1
            r=np.array(r)
            trans[I][J]=np.linalg.det(r)*((-1)**((I+1)+(J+1)))          
    R=np.array(trans)
    return R

#función especifica para el proyecto de analisis
def Datos():
    #esta muy clara esta parte
    n=8#int(input("Cuantas columnas tiene la tabla?    "))
    X=list()
    print('Ingresa los datos de x')
    for i in range(n):
        X.append(int(input()))           
    Y=list()
    print('Ingresa los datos de y')
    for i in range(n):
        Y.append(int(input()))
    A=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j]= X[i]**(n-j-1)
            
    A=np.array(A)
    B=np.array(Y)
    print('matriz A:\n',A)
    print('vector B:\n',B)
    return A,B

#esta funcion pide la matriz de coeficientes y el vector de 
#valores independientes para la descompocision LU
def RdSqMatrix():
    n=int(input('ingresa el orden de la matriz:  '))
    matrix=[[] for i in range(n)]
    print('ingresa los numeros')
    for i in range(n):
        print('renglon ',i+1)
        for j in range(n):
            matrix[i].append(int(input()))
    print('ingresa los coeficientes independientes')
    b=list()
    for i in range(n):
        b.append(int(input()))
        
    return np.array(matrix),np.array(b)

#esta matriz revisa que la matriz de coeficientes ingresada tenga
#descomposición LU validando el determinante de las submatrices lider
def SubMatrices(A):
    print('******* verificando submatrices **********')
    n=int(m.sqrt(A.size))
    for i in range (2,n+1):
        M=list()
        for x in range(i):
            n=list()
            for y in range(i):
                n.append(A[x][y])
            M.append(n)
        M=np.array(M)
        print(M,'\n')
        detM=np.linalg.det(M)
        if(detM==0):
            return -1
    return 1
    

def LUCrout2(A):
    n=int(m.sqrt(A.size))
    L=[[0 for j in range(n)] for i in range(n)]
    U=[[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        U[i][i]=1
    for i in range(n):
        L[i][0]=A[i][0]
    for i in range(1,n):
        U[0][i]=A[0][i]/L[0][0]
    for i in range(1,n):
        L[i][1]=A[i][1]-L[i][0]*U[0][1]
    for i in range(2,n):
        U[1][i]=(A[1][i]-L[1][0]*U[0][i])/L[1][1]
    for i in range(2,n):
        L[i][2]=A[i][2]-L[i][0]*U[0][2]-L[i][1]*U[1][2]
    for i in range(3,n):
        U[2][i]=(A[2][i]-L[2][0]*U[0][i]-L[2][1]*U[1][i])/L[2][2]
    for i in range(3,n):
        L[i][3]=A[i][3]-L[i][0]*U[0][3]-L[i][1]*U[1][3]-L[i][2]*U[2][3]
    L=np.array(L)
    U=np.array(U)          
    return L,U

def LUCrout(A):
    n=int(m.sqrt(A.size))
    L=Ceros(n)
    U=Identity(n)
    for i in range(n):
        for y in range(i,n):
            L[y][i]=A[y][i]
            for x in range(0,i):
                L[y][i]=L[y][i]-L[y][x]*U[x][i]
        for y in range(i,n):
            U[i][y]=A[i][y]
            for x in range(0,i):
                U[i][y]=U[i][y]-L[i][x]*U[x][y]
            U[i][y]=U[i][y]/L[i][i]
        #print(np.array(L))
        #print(np.array(U))
    L=np.array(L)
    U=np.array(U) 
    return L,U
 
def cuadrados(A,tol):
    B=[0,0,0,0,0,0]
    p=0
    q=0
    S=0
    R=0
    n=7
    Dq=100
    Dp=100
    x=0
    while x<15:
        x+=1
        B[0]=A[0]
        B[1]=A[1]-(p*B[0])
        B[2]=A[2]-(p*B[1])-(q*B[0])
        B[3]=A[3]-(p*B[2])-(q*B[1])
        B[4]=A[4]-(p*B[3])-(q*B[2])
        B[5]=A[5]-(p*B[4])-(q*B[3])
        R=A[n-1]-(p*B[n-2])-(q*B[n-3])
        S=A[n]-(q*B[n-2])
        p=((A[n-1]-(q*B[n-3]))/B[n-2])
        q=(A[n]/B[n-2])
        Dp=R/B[n-2]
        Dq=S/B[n-2]
        print(B,p,q)#Esta la puedes quitar solo es para ver la it.
        
    print("\nP(x)= (x^2 +(",p,")x +",q,")((",B[0],")x^5 + (",B[1],")x^4+ (",B[2],")x^3+ (",B[3],")x^2+ (",B[4],")x+ (",B[5],")")
    x=int(input("\nValor de x a evaluar:"))
    y=(pow(x,2) +(p*x) +q)*((B[0]*pow(x,5)) + (B[1]*pow(x,4))+ (B[2]*pow(x,3))+ (B[3]*pow(x,2))+ (B[4]*x)+ (B[5]))
    print("El valor de la funcion en x =",x,"es :",y)
  
    
def SolveLUCrout(A,B):
    L,U=LUCrout(A)
    print("Matriz Lower: \n",L)
    print("Matriz Upper: \n",U)
    
    print("\nLinv*B=Y= \n")
    y=inversa(L).dot(B)
    
    print("\nUinv*U=X= \n")
    x=inversa(U).dot(y)
    print('\n**************Solucion del sistema de ecuaciones**************\n')
    print(x)

    return x

def main():
    A,B=Datos()
    if(SubMatrices(A)==-1):
        print("no se puede con esa matriz shavo")
        return 0
    x=SolveLUCrout(A,B)
    cuadrados(x,90)

#A=np.array([[i**j for j in range(1,6)]for i in range(1,6)])
#B = np.array([-1,0,4,4.9])    
main()
