#!env/bin/python

"""
AmazonScrape

Usage: amazon_scrape.py [--number=<count>] [--output=output.xlsx]

Select and scrape a given number of Amazon book listings.
"""

from docopt import docopt
import requests
from bs4 import BeautifulSoup
import json

        
def random_amazon_link(number):
    """Use the site http://www.bookbookgoose.com/ to generate a random
    amazon link.  Grab the page and slice it apart for a link"""
    r = requests.get('http://www.bookbookgoose.com/v1/get_books?n={0}'.format(number))
    response = r.json()
    books = []
    for item in response:
        book = {
        'author':item[0],
        'title':item[1],
        'link':item[2],
        }
        books.append(book)
    return books
        

def main():
    arguments = docopt(__doc__)
    print random_amazon_link(5)


if __name__ == '__main__':
    main()