x = int(input())
y = int(input())
z = int(input())
n = int(input())
result = []
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if i+j+k != n:
                result.append([i,j,k])

print(result)


# a , b , c 
# a = 1(0,1)
# b = 1(0,1)
# c = 1(0,1)
# n = 2
0 , 0 , 0    0 , 0 ,1   0,1,0  0,1,1   1,0,0 , 
# [0,0,0],[0,1,0],[0,0,1],[1,0,0]
# a+b+c != n
