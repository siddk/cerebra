"""
search_scrape.py

Given a certain search query, uses the Marvel Wiki search API to find the
most related article, and returns the URL

"""

import requests
import json
import urllib

URL = "http://marvel.wikia.com/api/v1/Search/List?query={0}&limit=1&minArticleQuality=10&batch=1&namespaces=0%2C14"

# TODO Figure out Article Disambiguation (Iron Man vs. Tony Stark (Earth-616)
def get_search_url(query):
    """
    Use the Marvel Wiki API to get the most likely article URL that the
    search query is referring to.

    :param  query: Character/Entity that is being looked up
    :return:       URL of most related Wiki Article
    """
    search_url = URL.format(urllib.quote_plus(query))
    response = requests.get(search_url)

    if not response.status_code == 200:
        return None
    else:
        data = json.loads(response.text)
        return data["items"][0]["url"]


