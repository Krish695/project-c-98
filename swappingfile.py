def swappingfiledata ():
    filename1=input("Enter file name:  ")
    filename2 = input ("Enter file name:  ")
    with open(filename1,"r") as data1:
        a=data1.read()
    with open(filename2,"r") as data2:
        b=data2.read()

    with open(filename1,"w") as data1:
        data1.write(b)
    with open(filename2,"w") as data2:
        data2.write(a)
swappingfiledata()