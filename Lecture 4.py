
# Exercise 1

#listing = []
#list_input=input("Type in a number to the list ")



#while list_input != 'q':
 #   listing.append(int(list_input))
  #  list_input = input("Type in a number to the list ")


#listing.sort()
    #print(list)

#for numbe in listing:
 #   print(numbe)

#Exercise 2

#def chinese_year():
    #create input to type in the year
 #   year=eval(input("Type in the year "))
    #create a list
  #  zodiac= ["monkey","rooster","dog","pig", "rat","ox","tiger","rabbit","dragon","snake","horse","sheep"]
    #print the year and zodiac%12
   # print(year,"is", zodiac[year%12])

#chinese_year()

#Exercise 3

#import random
#random_list = [random.choice(list(range(1, 100))) for _ in range(10)]
#def get_min(random_list):
    #loop through each element in the list
 #   for element in random_list:
        #create variable called smallest and equate to minimum value in the list
  #     smallest= min(random_list)
    #outside the loop print the smallest variable and its location in the list
   # print(smallest)
    #print(random_list.index(smallest))

#get_min(random_list)

#Exercise 4 - Eliminate duplicates

#def eliminateDuplicates():
 #   lst=[]
  #  num=input("Enter ten numbers: ")
   # while len(lst)<10:
    #    num=input("Enter ten numbers: ")
     #   lst.append(num)
      #  lst.sort()

    #print("The distinct numbers are",lst)

#eliminateDuplicates()

#def main():
    # Read numbers as a string from the console
 #   s = input("Enter numbers: ")
  #  items = s.split() # Extracts items from the string
   # numbers = [ int(x) for x in items ] # Convert items to numbers

    #print("The distinct numbers are:", eliminateDuplicates(numbers))

#def eliminateDuplicates(list):
 #   result = []
  #  for element in list:
   #     if not (element in result):
    #        result.append(element)

    #return result

#main()

#Exercise 5

#def main():
 #   s1 = input("Enter the first string: ").strip()
  #  s2 = input("Enter the second string: ").strip()

   # print(s1, "and", s2, "are",
    #  ("anagram." if isAnagram(s1, s2) else "not anagram."))

#def isAnagram(s1, s2):
 #   if len(s1) != len(s2):
  #      return False

   # newS1 = sort(s1);
    #newS2 = sort(s2);

    #return newS1 == newS2

#def sort(s):
 #   r = list(s)
  #  r.sort()

   # result = ""
    #for ch in r:
     #   result += ch

    #return result

#main()


#Exercise 6
import random

def main():
    #list of words which can be used in hangman
    words = ["write", "program", "that", "receive", "positive", "change", "study", "excellent", "nice"]

    #Create a variable called gameFinished=False as default
    gameFinished = False
    #use a while condition to say while the game is not finished
    while not gameFinished:
        #index variable
        index = random.randint(0, len(words) - 1)
        hiddenWord = words[index]
        guessedWord = len(hiddenWord) * ['*']
        numberOfCorrectLettersGuessed = 0
        numberOfMisses = 0
        #while number of correct letters entered less than length of the word prompt the use to guess a word and strip out any spaces etc around it
        while numberOfCorrectLettersGuessed < len(hiddenWord):
            letter = input("(Guess) Enter a letter in word " + toString(guessedWord) + " > ").strip()
            if letter in guessedWord:
                print("\t", letter, "is already in the word")
                #stop duplicate letters from being added again
            elif hiddenWord.find(letter) < 0:
                print("\t", letter, "is not in the word")
                numberOfMisses += 1
                #inform user that letter not in the word and increase Guess Count
            else:
                k = hiddenWord.find(letter)
                while k >= 0:
                    guessedWord[k] = letter
                    numberOfCorrectLettersGuessed += 1
                    k = hiddenWord.find(letter, k + 1)
        print("The word is " + hiddenWord + ". You missed "
                + str(numberOfMisses) + (" time" if (numberOfMisses <= 1) else " times"))
        anotherGame = input("Do you want to guess for another word? Enter y or n> ").strip()
        if anotherGame == 'n':
            print("Finished")
            gameFinished = True

def toString(list):
    s = ""
    for e in list:
        s += e
    return s

main()