print("****************************************")
print("UNIQUE CALCULATOR")
print("****************************************")
while True:
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.power")
    print("6.percentage")
    print("7.cube root")
    print("8.square root")
    print("9.average")
    print("10.greatest common divisor(GCD)")
    print("11.least common multiple(LCM)")
    print("12.check whether a prime number or not")
    print("13.find factorial")
    print("14.EXIT")
    print("Instruction:enter only the index of operation that are given in the above list.")
    operation_select=int(input("enter your selected operation:"))
    print("you selected:",operation_select)
    if operation_select == 1:
        x=float(input("enter first number:"))
        y=float(input("enter second number:"))
        Addition=x+y
        print("result obtained is=",Addition)
    elif operation_select==2:
        x=float(input("enter first number:"))
        y=float(input("enter second number:"))
        Subtraction=x-y
        print("result obtained is=",Subtraction)
    elif operation_select==3:
        x=float(input("enter first number:"))
        y=float(input("enter second number:"))
        Multiplication=x*y
        print("result obtained is=",Multiplication)
    elif operation_select==4:
        x=float(input("enter first number:"))
        y=float(input("enter second number:"))
        if y==0:
            print("unable to divide as division by zero is not allowed.")
        else:
            Division=x/y
            print("result obtained is=",Division)
    elif operation_select==5:
        x=float(input("enter base number:"))
        y=float(input("enter exponent number:"))
        number_raised_to_power=x**y
        print("result obtained is:",number_raised_to_power)
    elif operation_select==6:
        number=float(input("enter number:"))
        total=float(input("enter total value:"))
        if total==0:
            print("error:total cannot be zero.")
        else:
            percentage=(number/total)*100
            print("percentage=",percentage,"%")
    elif operation_select==7:
        number=float(input("enter a number:"))
        if number<0:
            cube_root=-((-number)**(1/3))
        else:
            cube_root=number**(1/3)
            print("cube root=",cube_root)
    elif operation_select==8:
        number=float(input("enter number:"))
        if number<0:
            print("square root is not defined for negative numbers.")
        else:
            square_root=number**(1/2)
        print("square root=",square_root)
    elif operation_select==9:
        numbers=list(map(float,input("enter numbers separated by space:").split()))
        if len(numbers)==0:
            print("NO NUMBERS ENTERED.")
        else:
            average=sum(numbers)/len(numbers)
            print("average=",average)
    elif operation_select==10:
        a=int(input("enter first number:"))
        b=int(input("enter second number:"))
        if a==0 and b==0:
            print('GCD is undefined for 0 and 0.')
        else:
            a=abs(a)
            b=abs(b)
            while b!=0:
                a,b=b,a%b
            print("GCD=",a)
    elif operation_select==11:
        a=int(input("enter first number:"))
        b=int(input("enter second number:"))
        if a==0 or b==0:
            print("LCM=0")
        else:
            x=abs(a)
            y=abs(b)
            p=x
            q=y
            while q!=0:
                p,q=q,p%q
            hcf=p
            LCM=abs(a*b)//hcf
            print("LCM=",LCM)
    elif operation_select==12:
        number=int(input("enter a number:"))
        if number <= 1:
            print("The number you entered is not a prime number. ")
        else:
            entered_number_is_prime=True
            for i in range(2,int(number**0.5)+1):
                if number%i==0:
                    entered_number_is_prime=False
                    break
            if entered_number_is_prime:
                print("it is a prime number.")
            else:
                print("it is not a prime number.")
    elif operation_select==13:
        number=int(input("enter a non-negative integer:"))
        if number<0:
            print("factorial is not defined for negative numbers.")
        else:
            factorial=1
            for i in range(1,number+1): 
                factorial=factorial*i
            print("Factorial =",factorial)   
    elif operation_select==14:
        print("THANK YOU!!!! for using unique calculator.....")
        break
    else:
        print("Invalid operation selected.")

        