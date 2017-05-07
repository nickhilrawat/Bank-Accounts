file=open("accntno.txt", "r")
num=int(file.read())
file.close()
file=open("accntno.txt", "w")
num=num+1
file.write(str(num))
print(num)
