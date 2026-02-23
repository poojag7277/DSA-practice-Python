#Example
#Sample Input 0
#1
#1
#1
#2
#Sample Output 
#[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
#Explanation 
#Each variable  and  will have values of  or . All permutations of lists in the form .
#Remove all arrays that sum to  to leave only the valid permutations


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

result=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                result.append([i,j,k])
                
print(result)    
