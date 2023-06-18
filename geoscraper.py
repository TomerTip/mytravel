from bs4 import BeautifulSoup, NavigableString
from mediawiki import MediaWiki
import requests
import wikitextparser as wtp
from pprint import pprint

# Get html page
# Find id=See header
# Get parent element of See header
# Get all vcard elements
# create a dictionary of {location:(lattitude:longitude)}

API_URL = "http://en.wikivoyage.org/w/api.php"
wt = MediaWiki(url=API_URL)

COUNTRY=""
CITY="Rio De Janiero"
DEST = CITY + ", " + COUNTRY
print ("Scraping " + DEST + "...")

wiki_page = wt.page(DEST)
soup = BeautifulSoup(wiki_page.html, 'lxml')


def get_section(section_name):

    section_header = soup.find("span", {"id" : section_name})
    next_header = section_header.parent.find_next_sibling("h2")

    def between(cur, end):
        html = u""
        for tag in section_header.parent.find_next_siblings():
            if tag == next_header:
                return html
            else:
                html += tag.decode()
        return html

    section = BeautifulSoup(between(section_header, next_header), 'lxml')
    return section


def get_locations_coords(doc):
    location_coords = {}

    #for bdi in soup.find_all("span", {"class" : "vcard"}):

    for bdi in doc.find_all(class_="vcard"):

        #name = ...
        
        # class : listing-content
        # class : listing-address
        geos = bdi.findChildren("span", {"class" : "listing-coordinates"}, recursive=True)
        for geo in geos:
            name = geo.parent.findChildren("span", {"class" : "listing-name"})[0].get_text()
            #address = geo.parent.findChildren("bdi", {"class" : "listing-address"})[0].get_text()
            lat = geo.findChildren("abbr", {"class" : "latitude"})[0].get_text()
            long = geo.findChildren("abbr", {"class" : "longitude"})[0].get_text()
        
        #location_coords[name] = address
        location_coords[name] = (lat, long)
       

    pprint(location_coords)
    return location_coords


def get_locations_coords_by_section(section_name='See'):
    section = get_section(section_name)
    location_coords_dict = get_locations_coords(section)
    return location_coords_dict


get_locations_coords_by_section(section_name="See")



