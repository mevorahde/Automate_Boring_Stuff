#! python3
"""
lucky.py - Opens several Google search results.
Created on Wed Dec  19, 2018
@author: David E. Mevorah
"""
import requests, sys, webbrowser, bs4

print('Googling....') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search results links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

#input('Press Enter to Exit...')
