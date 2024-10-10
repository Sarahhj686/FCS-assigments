list1 = [54,76,2,4,98,100]
int1=int(input("enter a number:"))
int2=int(input("enter another number:"))
if int1>int2:
    int1,int2 = int2,int1
for i in list1:
    if int1<i<int2 :
        print(i)
