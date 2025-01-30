def adamnumbers(a):
    square=a*a
    rev=0
    rev2=0
    while(square!=0):
        ld=square%10
        rev=(rev*10)+ld
        square//=10
    while(a!=0):
        ld1=a%10
        rev2=(rev2*10)+ld1
        a//=10
    revsq=rev2*rev2
    if(rev==revsq):
        print(f"The number {a} is:","Adam number")
    else:
        print(f"The number {a} is:","Not Adam number")
num=int(input("Enter the number:"))
adamnumbers(num)
    
