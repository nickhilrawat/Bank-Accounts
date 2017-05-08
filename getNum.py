def getNum():
    file=open("accntno.txt", "r")
    num=int(file.read())
    file.close()
    file=open("accntno.txt", "w")
    num2=num+1
    file.write(str(num2))
    return num
