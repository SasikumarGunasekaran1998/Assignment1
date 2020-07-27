def myFilter(func,data):#My Filter Function
    info = [i for i in data if(func(i))]
    return info
if __name__ == "__main__":
    data = [1,4,3,5,10]
    func = lambda x : x>3
    information = myFilter(func,data)
    print(information)
