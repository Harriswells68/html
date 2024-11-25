import pickle
with open("cur.dat", "rb") as fp:
    print(pickle.load(fp))
with open("cur.dat", "wb") as fp:
    k={'month': 11, 'idn': 0}
    pickle.dump(k, fp)

ci=[]
cs=[]

try:
    fp=open("data.pkl", "rb")
    while True:
        k=pickle.load(fp)
        ci.append(list(k.keys())[0])
        cs.append(list(k.values())[0])
        
except:
    fp.close()

print(ci, cs, sep="\n")




