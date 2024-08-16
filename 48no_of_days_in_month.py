def using_if_else(y,m):
    if m == 2 and (y % 400 == 0 or (y % 100 != 0 and y % 4 == 0)):
        print("Number of days is 29")

    elif(m==2) :
        print("Number of days is 28")

    elif(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) :
        print("Number of days is 31")

    else :
        print("Number of days is 30")

    
def using_array(y,m):
    arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    if(m==2 and ((y%400==0) or ((y%100!=0) and (y%4==0)))) :
        print("Number of days is ", arr[m-1]+1)
    
    else :
        print("Number of days is ", arr[m-1])

year = int(input())
month  = int(input())

using_if_else(year,month)
using_array(year,month)