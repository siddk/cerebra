"""
batch_scrape.py

Scrapes the Marvel Wiki for the top N articles, by returning the URLs of all hyperlinks off the
EARTH-616 Wiki article.
"""
from bs4 import BeautifulSoup
import re
import urllib2

BASE_URL = "http://marvel.wikia.com"
EARTH_616 = "/wiki/Earth-616"


def get_hyperlinks():
    """
    Parse the body of the Earth-616 Article for all the hyperlinks, return them as
    as set.

    :return: Set of all article hyperlinks in the Earth-616 Universe.
    """
    page = urllib2.urlopen(BASE_URL + EARTH_616)
    soup = BeautifulSoup(page.read())

    hyperlinks = [x for x in soup.find_all(href=re.compile("^/wiki/")) if ":" not in x.get('href')]
    hyperlinks = filter(lambda elem: elem.get('class') is None or elem.get('class') == ["mw-redirect"], hyperlinks)
    return set(map(lambda elem: elem.get('href'), hyperlinks))


def write_hyperlinks(hyperlink_set):
    """
    Write all hyperlinks to a CSV file.

    :param  hyperlink_set: Set of all hyperlinks to write.
    """
    with open('earth616.csv', 'w') as f:
        for h in hyperlink_set:
            f.write(BASE_URL+ "%s\n" % h)

if __name__ == "__main__":
    write_hyperlinks(get_hyperlinks())
