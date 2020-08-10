import mechanicalsoup
from time import sleep
import requests
from bs4 import BeautifulSoup
from datetime import date



def main():
    # prompt user to type in ticker
    Ticker = input("Type in the RIC ").upper()

    # use mechanical soup browser
    my_browser = mechanicalsoup.StatefulBrowser()
    # concatenate reuters web page with user input
    page = my_browser.get("https://uk.reuters.com/companies/" + Ticker)
    html_text = page.soup
    
    # print(html_text)
    # return a list of all the tags where we need to obtain latest price, price change, stock name, news, volume and daily price range
    my_tags = html_text.select(".QuoteRibbon-price-Byg3o")
    my_tags2 = html_text.select(".QuoteRibbon-change-1aQtL")
    my_tags3 = html_text.select(".QuoteRibbon-heading-1Jngi")
    my_tags4=html_text.select(".QuoteRibbon-disclaimer-1VLhn")
    my_tags5 = html_text.select(".NewsList-title-container-13xXt")
    my_tags6 = html_text.select(".FeedScroll-container-2mXNY")
    #my_tags7 = html_text.select("#TextLabel__text-label___3oCVw TextLabel__gray___1V4fk TextLabel__regular___2X0ym")
    my_tags8 = html_text.select(".QuoteRibbon-volume-22vsO")
    my_tags9 = html_text.select(".QuoteRibbon-today-range-1ROkl")
    #map tags to variables and index to return appropriate values
    my_price = my_tags[0].text[12:]
    time= my_tags4[0].text
    #timestamp=my_tags7[0].text
    my_change = my_tags2[0].text[6:]
    my_name = my_tags3[0].text
    news = my_tags5[0].text
    todays_range=my_tags9[0].text[13:]
    news2 = (my_tags6[0].text)
    volume = (my_tags8[0].text[6:])


    #return the values on the console

    print("Name: ", my_name[:-3], "Last Price:", my_price, ", Change:", my_change, ", Today's Volume: ", volume, ", Today's Range:",todays_range )
    print(news[:-4], ":", news2[11:])

    # icker=input("Type in the stock ticker ").upper()

    #print(time)
while True:
    sleep(3)
    main()
