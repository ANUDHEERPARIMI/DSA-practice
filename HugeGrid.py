# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    ans=0
    i=j=0
    while (i<n and j<n):
        if i==j:
            ans+=(s[i]=='1')
            j+=1
        else:
            ans+=(s[i]=='1')+(s[j]=='1')
            i+=1
    print(ans)
        
        
    