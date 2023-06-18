from mediawiki import MediaWiki
import wikitextparser as wtp
from bs4 import BeautifulSoup


SECTIONS = {
    "regions": 'Regions',
    "cities": 'Cities',
    "other_dests": 'Other destinations',
}

def find_section_by_title(sections, title):
    for section in sections:
        if section.title == title:
            return section

def get_section_wikilinks(section):
    links = []
    extensions=["file:", "image:", "png", "jpg", "jpeg", "File", "JPG", "PNG", "Image"]
    for link in section.wikilinks:
        if not any(ext in link for ext in extensions):
            links.append(link)
    return links

API_URL = "https://wikitravel.org/wiki/en/api.php"
wt = MediaWiki(url=API_URL)

COUNTRY = "Brazil"

dest = wt.page(COUNTRY)
parsed = wtp.parse(dest.wikitext)

scrape = {}
for section_name in SECTIONS:
    section = find_section_by_title(parsed.sections, SECTIONS[section_name])
    links = get_section_wikilinks(section)
    scrape[section_name] = links

print(scrape)
# BeautifulSoup(parsed.plain_text(), 'lxml').find_all('sleep')

# Recursive scrape:
   # wtp.parse(wt.page(scrape['regions'][0].title).wikitext)
# Stop when reaches leaf - city.

'''
    This function extract locations from a page recursively.
    The leaf of the tree is city page.
    The page hiercy is as follows:
        Country
            Regions
                Sub-Regions (if this coutry is huge)
                    Sub-Regions
                        ...
                            City


    When City is hit - location from See section are scraped.

    Page is passed
    location list is returned
    the location list of the recursive function is appended to the list.
    
    If non City page is met (is there a why to determine what is the type of the page?)
        Create list of link of sub pages
            For each page call scrape.

    locations.append(location_scraper(page))
    return locations 
''' 

'''
Regions
Districts
Cities



'''

LOCATIONS = []
def location_scraper(page):
     
    # Attempt to get page type

    if location not in LOCATIONS:
            LOCATIONS.append(location) 
            # calling it self
            location_scraper(page)



   
# lists

   
# function created
def scrape(site):
       
    # getting the request from url
    r = requests.get(site)
       
    # converting the text
    s = BeautifulSoup(r.text,"html.parser")
       
    for i in s.find_all("a"):
          
        href = i.attrs['href']
           
        if href.startswith("/"):
            site = site+href
            
            # If not a city:
            print(page)
            if location not in LOCATIONS:
                LOCATIONS.append(location) 
                # calling it self
                scrape(page)
