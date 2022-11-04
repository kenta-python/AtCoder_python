N=int(input())
suits=["S","H","C","D"]
cards=[]
for _ in range(N):
    s,n=input().split()
    if s=="S":
        cards.append(int(n))   
    elif s=="H":
        cards.append(13+int(n))   
    elif s=="C":
        cards.append(26+int(n))
    else:
        cards.append(39+int(n))

for i in range(1,53):
    if i not in cards:
        print(suits[(i-1)//13],(i-1)%13+1)