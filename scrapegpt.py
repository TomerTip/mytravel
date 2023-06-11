import requests
from bs4 import BeautifulSoup

# Specify the URL of the Wikivoyage page
url = 'https://en.wikivoyage.org/wiki/Rio_de_Janeiro'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the elements containing the coordinates and their names
# Adjust this based on the HTML structure of the specific page
coordinate_elements = soup.find_all('span', class_='geo')
name_elements = soup.find_all('span', class_='vcard')

# Verify that the number of coordinates and names match


# Extract the coordinates and names
data = []
for coordinate_element, name_element in zip(coordinate_elements, name_elements):
    #lat, lon = coordinate_element.text.strip().split(';')
    lat, lon = 1,1
    import ipdb;ipdb.set_trace()
    name = name_element.text.strip()
    data.append((name, float(lat), float(lon)))

# Print the extracted names and coordinates
for name, lat, lon in data:
    print(f"{name}: ({lat}, {lon})")
