#Print the runner-up score.
#Sample Input 
#5
#2 3 6 6 5
#Sample Output 5
#Explanation Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    uni=list(set(arr))
    uni.sort()
    print(uni[-2])
   
