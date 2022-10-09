lyrics=""" aankh mare kin ladka aankh mare sitti bajaye  beech sadak pe  """
D={}

for i in lyrics.split():
    if i not in D:
        D[i]=1
    else:
        D[i]=D[i]+1

for i in D:
    if D[i]==max(D.values()):
        print(i,max(D.values()))
        break