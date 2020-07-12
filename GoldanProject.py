#Golden Project

def next1(n):
    #print(ord(n))
    k=[67,71,73,79,83,89,97,101,103,107,109,113]
    if(ord(n)<=67):
        ans=67
    elif(ord(n)>=113):
        ans=113
    else:
        for i in range(0,12):
            if k[i]>ord(n):
                d1=k[i]-ord(n)
                d2=ord(n)-k[i-1]
                if d1<d2:
                    ans=k[i]
                    break
                else:
                    ans=k[i-1]
                    break
    #print(ans)
    return chr(ans)
t=0
i=0
n=0
t=int(input())
ch=[]
while(t!=0):
    n=int(input())
    ch=input()
    for i in range(0,n):
        temp=ch[i]
        ne=next1(temp)
        k=ch[0:i]+ne+ch[i+1:n]
        ch=k
    print(ch)
    t-=1
