data1 = ["x","y","z"] #Print Val_1
info1 = [i*x for i in data1 for x in range(1,5)]
print(info1)

info2 = [i*x for i in range(1,5) for x in data1]#Print Val_2
print(info2)

info3 = [([i]+[i+1]+[i+2]+[i+3]) for i in range(2,6) ]
info31 = [[j] for i in range(4,7) for j in range(i-2,i+1)]
print(str(info31)+str(info3))


info4 = [(i,x) for x in range(1,4) for i in range(1,4)]
print(info4)



