import random

from list_of_countries import COUNTRIES

def main():
    countries=list(COUNTRIES.keys())
    country_to_guess = random.choice(countries)
    guess=input("Type in the capital of ",country_to_guess )

    if guess.lower() == COUNTRIES[country_to_guess].lower:
        print("correct")

    else:
        print("The correct answer is ",COUNTRIES[country_to_guess])
