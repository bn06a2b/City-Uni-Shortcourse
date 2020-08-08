#Exercise 1

#create variable called miles
#miles=100
#create kilometres variable and multiply miles by 1.609
#kilometres=miles*1.609
#print(kilometres)

#Exercise 2.1

#create variable called length,width and area
#length=3
#width=4
#area= length * width
#print(area)

#Exercise 2.2
#prompt user to enter the length and width of the rectangle
#length=float(input("Type in the length"))
#width=float(input(("Types in the width")))
#define the area
#area= length * width
#print the length, width and area
#print("The length is " + str(length),"the width is",str(width),"and the area is", str(area))

#Computing loan payments
#loan_amount=float(input("type in the loan amount "))
#interest_rate=float(input("type in the interest rate % "))
#years=float(input("type in the term period for borrowing "))
#monthly_interest_rate=float((interest_rate/100)/12)
#power=(years*12)
#monthly_payment= (loan_amount*monthly_interest_rate)/(1-1/(1+monthly_interest_rate)**power)
#print("Your monthly payment is", round(monthly_payment,2))
#print(monthly_interest_rate)

#password exercise
#Password="HELLO"
#PASSWORD_entered=input("Type in your password ")
#if PASSWORD_entered==Password:
 #   print("Access Granted")
#else:
 #   print("Forbidden")

#password and login exercise

#username="Amer"
#Password="Bob"
#username_entered=input("Type in username ")
#password_entered=input("Type in password ")

#if username_entered==username and password_entered==Password:
 #   print("Access Granted")
#else:
 #   print("Forbidden")

 #Exercise: check number divisor
#num=int(input("Type in a number "))
#if num %5==0 and num%2==0:
 #   print("HiFive and HiEven")
#elif num %5==0:
 #   print("HiFive")
#elif num%2==0:
 #   print("HiEven")

#Exercise: grading students

#score=eval(input("type in your score "))
#if score > 90:
#    print("A")
#elif score >=80:
 #   print("B")
#elif score >=70:
    #print("C")
#elif score >=60:
 #   print("D")
#else:
#    print("F")

#leap year
#year=int(input("Type in the year "))
#if (year %4==0 and year %100!=0) or year %400==0:
 #   print(year, "is a leap year")
#else:
 #   print(year, "is not a leap year")

#Chinese Zodiac exercise

year=eval(input("Type in the year "))

if year%12==0:
    print(year, "is the year of the monkey ")
elif year%12==1:
    print(year,"is the year of the rooster")
elif year%12==2:
    print(year, "is the year of the dog")
elif year%12==3:
    print(year, "is the year of the pig")
elif year%12==4:
    print(year, "is the year of the rat")
elif year%12==5:
    print(year, "is the year of the ox")
elif year%12==6:
    print(year, "is the year of the tiger")
elif year%12==7:
    print(year, "is the year of the rabbit")
elif year%12==8:
    print(year, "is the year of the dragon")
elif year%12==9:
    print(year, "is the year of the snake")
elif year%12==10:
    print(year, "is the year of the horse")
elif year%12==11:
    print(year, "is the year of the sheep")






