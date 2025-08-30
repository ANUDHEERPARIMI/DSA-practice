t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    print(min(n,m//2)+min(n,m//2)*2)
