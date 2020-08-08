#Exercise: Guess Number

#import random

# Generate a random number to be guessed
#number = random.randint(1, 100)

#print("Guess a magic number between 0 and 100")

#number_guess=''


#while number_guess !=number:
 #   number_guess=int(input("type in a number "))
  #  if number_guess>number:
   #     print("number is too high ")

    #elif number_guess<number:
     #   print("number is too low ")

    #elif number_guess==number:
     #   print("Correct number- the number is",number)

#Exercise: compute average

#create positive and negative counters as well as count and total
#count_positive=0
#count_negative=0
#count=0
#total=0

#number=int(input("Type in a number, the input ends if it is 0 "))

#if number >0:
 #   count_positive +=1
#else:
 #   count_negative +=1

#while number !=0:
 #   number = int(input("Type in a number, the input ends if it is 0 "))
  #  total +=number
   # count +=1
#else:
    #total= sum(number)
#if count== 0:
 #   print("No numbers are entered")

#print statements

#print("The number of positives is",count_positive)
#print("The number of negatives is", count_negative)
#print("The total is", total)
#print("The average is", total/count)

#Exercise: conversion from miles to km

#miles=1

#print ("Miles", "Kilometres")
#for miles in range(1,11):
 #   print(miles,miles*1.609)

#Exercise: Display Leap Years
#year= 2001
#for year in range(2001,2101):
 #  if (year %4==0 and year %100!=0) or year %400==0:
  #     print(year, end= " ")
#the end= " " parameter ends the output with a space


#Exercise Bonus palindrome

#word=eval("input a word")
#is_palindrome = True

#for i in range(0, len(line) // 2):
 #   if line[i] != line[len(line) - 1 - i]:
  #      is_palindrome = False
   #     break

#if is_palindrome:
 #   print(line, "is a palindrome")
#else:
 #   print(line, "is not a palindrome")
