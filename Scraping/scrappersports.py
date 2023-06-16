import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(soup, quotes):
    # retrieving all the quote <div> HTML element on the page
    quote_elements = soup.find_all('div')
    #attrs={'class': 'KambiBC-event-groups'}
    print(quote_elements)

    # iterating over the list of quote elements
    # to extract the data of interest and store it
    # in quotes
    for quote_element in quote_elements:
        
        time_date = quote_element.find('span', class_='KambiBC-event-item__start-time--date')       
        time_time = quote_element.find('span', class_='KambiBC-event-item__start-time--date')
        teams = quote_element.find('div', class_='KambiBC-event-participants__name')
        events = quote_element.find('div', class_='KambiBC-event-participants')
        bet_team = quote_element.find('div', class_='OutcomeButton__Label-sc-lxwzc0-2 efOwr')
        bet_odds = quote_element.find('div', class_='OutcomeButton__Odds-sc-lxwzc0-6 iYOCD')
        test = quote_element.find('div', class_='game-list all-game-list')

        # extracting the tag <a> HTML elements related to the quote
        #tag_elements = quote_element.find('div', class_='tags').find_all('a', class_='tag')

        # storing the list of tag strings in a list
        """
        tags = []
        for tag_element in tag_elements:
            tags.append(tag_element.text)
        """

        # appending a dictionary containing the quote data
        # in a new format in the quote list
        quotes.append(
            {
                'timedate': time_date,
                'time': time_time,
                'teams': teams,
                'events': events,
                'bet-team': bet_team,
                'bet-odds': bet_odds,
                'test': test
            }
        )

# the url of the home page of the target website
base_url = 'https://www.rushbet.co/?page=sportsbook#filter/football/'

# defining the User-Agent header to use in the GET request below
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# retrieving the target web page
page = requests.get(base_url, headers=headers)

# parsing the target web page with Beautiful Soup
soup = BeautifulSoup(page.text, 'html.parser')

# initializing the variable that will contain
# the list of all quote data
quotes = []

# scraping the home page
scrape_page(soup, quotes)

"""
# getting the "Next →" HTML element
next_li_element = soup.find('li', class_='next')

# if there is a next page to scrape
while next_li_element is not None:
    next_page_relative_url = next_li_element.find('a', href=True)['href']

    # getting the new page
    page = requests.get(base_url + next_page_relative_url, headers=headers)

    # parsing the new page
    soup = BeautifulSoup(page.text, 'html.parser')

    # scraping the new page
    scrape_page(soup, quotes)

    # looking for the "Next →" HTML element in the new page
    next_li_element = soup.find('li', class_='next')
"""
# reading  the "quotes.csv" file and creating it
# if not present
csv_file = open('quotessports.csv', 'w', encoding='utf-8', newline='')

# initializing the writer object to insert data
# in the CSV file
writer = csv.writer(csv_file)

# writing the header of the CSV file
writer.writerow(['Timedate', 'Time', 'Teams', 'Events', 'Bet Team', 'Bet Odds', 'Test'])

# writing each row of the CSV
for quote in quotes:
    writer.writerow(quote.values())

# terminating the operation and releasing the resources
csv_file.close()
