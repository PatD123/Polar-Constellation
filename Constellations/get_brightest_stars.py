from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re, json

# Getting the page
URL = "https://www.astronomytrek.com/star-constellations-brightest-stars/"
uClient = uReq(url=URL)
page_html = uClient.read()
page_soup = soup(page_html, "html.parser")

# Opening a file to write in
stars_file = open("brightest_stars.txt", 'w')

#
def find_space(star):
    for i in range(0, len(star)):
        if star[i] == " " and star[i + 1] == "(":
            return i


brightest_uncleaned = page_soup.find_all("tr")
for html in brightest_uncleaned:
    col_4 = html.contents[4].contents[0]
    col_5 = html.contents[5].string
    if col_5 is not None:
        idx = find_space(col_5)
        col_5 = col_5[0:idx]
        if col_5 == "Brightest Star": continue
        stars_file.write(col_5 + "\n")
    else:
        idx = find_space(col_4)
        col_4 = col_4[0:idx]
        stars_file.write(col_4 + "\n")

stars_file.close()