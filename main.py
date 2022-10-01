def fibbo(num):
    a,b=0,1
    i=2
    print(a)
    print(b)
    while(i<num):
        c=a+b
        print(c)
        a=b
        b=c
        i=i+1
while True:
    fibbo(int(input("Enter the range of the fibbonakki number :")))