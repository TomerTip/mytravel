from mediawiki import MediaWiki
import wikitextparser as wtp
from bs4 import BeautifulSoup


SECTIONS = {
    "see": 'See',
    "do": 'Do',
    "sleep": 'Sleep',
    "eat": 'Eat'
}

def find_section_by_title(sections, title):
    for section in sections:
        if section.title == title:
            return section

def get_locations_from_section(section):
    titles = []
    # Wikilist
    for wikilist in section.lists():
        #import ipdb;ipdb.set_trace();

        bolds = wtp.Section(wikilist.string).get_bolds()
        if len(bolds) != 0:
            title = bolds[0].plain_text()
            titles.append(title)
    # XML
    soup = BeautifulSoup(section.plain_text(), 'lxml')
    for tag in soup.find_all(section.title.lower()):
        title = tag.attrs['name']
        titles.append(title)

    return titles

#API_URL = "https://wikitravel.org/wiki/en/api.php"
API_URL = "http://en.wikivoyage.org/w/api.php"
wt = MediaWiki(url=API_URL)

COUNTRY=""
CITY="Palermo"
DEST = CITY + ", " + COUNTRY
print ("Scraping " + DEST + "...")

#import ipdb;ipdb.set_trace();
dest = wt.page(DEST)
parsed = wtp.parse(dest.wikitext)


scrape = {}
for section_name in SECTIONS:
    section = find_section_by_title(parsed.sections, SECTIONS[section_name])
    locations = get_locations_from_section(section)
    scrape[section_name] = locations

print(scrape)





# BeautifulSoup(parsed.plain_text(), 'lxml').find_all('sleep')

# Tags:
# sleep
# do


    