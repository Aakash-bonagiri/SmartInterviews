t=int(input())
for i in range(t):
    size=int(input())
    lst=list(map(int,input().split()))
    sum=0
    for j in lst:
        sum+=j
    print(sum)
