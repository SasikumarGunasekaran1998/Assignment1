def myReduce(func,data):#My Reduce Function
    reduced_val = add(data[0],data[1])
    for i in range(2,len(data)):
        reduced_val = add(reduced_val,data[i])   
    return reduced_val

if __name__ == "__main__":
    data = [1,3,4,5,10]
    add = lambda u,v : u+v
    sum_value = myReduce(add,data)
    print(sum_value)
    
