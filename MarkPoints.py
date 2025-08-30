# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    if n==s.count('0'):
        print('Yes')
    else:
        l=s.split('0')
        c='Yes'
        for val in l:
            if val and val.count('1')<3:
                c='No'
                break
        print(c)
                
            
    