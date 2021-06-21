import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("sakshi-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("sakshi-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("Jack-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Jack-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("Mack-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Mack-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("sakshi-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("sakshi-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("Jack-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Jack-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("Mack-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Mack-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (sakshi,jay,Bharati)")
print("......Hello,Guys Welcome, My Name is Sakshi......\n")       
print("health management system: ")
a=int(input("press 1 for log the value and 2 for retrieve "))

if a==1:
    b = int(input("press 1 for sakshi 2 for Jack 3 for Mack "))
    take(b)
else:
    b = int(input("press 1 for sakshi, 2 for  Jack  And 3 for Mack "))
    retrieve(b)