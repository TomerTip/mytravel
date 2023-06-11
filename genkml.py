"""
<Placemark>
        <name>Catania Airport</name>
        <styleUrl>#icon-1504-FF5252-nodesc</styleUrl>
        <Point>
          <coordinates>
            15.0657746,37.4673046,0
          </coordinates>
        </Point>
    </Placemark>
"""  
from pykml.factory import KML_ElementMaker as KML
from pykml import parser
from lxml import etree

FILENAME="mytravel.kml"

#kml_str = """<kml xmlns="http://www.opengis.net/kml/2.2"><Document></Document></kml>"""

#root = parser.fromstring(STYLE)
#doc = root.Document

PM_NAME = 'Ipanema'
LONG, LAT = ('-22.987', '-43.213')

FOLDER_NAME = "Beaches"

#doc = KML.kml()

BEACHES = {
  "Ramos": ["-22.83877", "-43.250151"],
  "Flamengo": ["-22.9287", "-43.1712"],
  "Botafogo": ["-22.9455", "-43.18093"],
  "Urca": ["-22.948", "-43.163164"],
  "Vermelha": ["-22.95544", "-43.164715"],
  "Leme": ["-22.9642", "-43.16936"],
  "Copacabana": ["-22.9707", "-43.18187"],
  "Arpoador": ["-22.9887", "-43.19258"],
  "Ipanema": ["-22.987", "-43.2139"],
  "Leblon": ["-22.988", "-43.224710"],
  "São Conrado": ["-22.99901", "-43.25611"],
  "Barra da Tijuca": ["-23.0111", "-43.360312"],
  "Recreio dos Bandeirantes": ["-23.0265", "-43.4613"],
  "Macumba": ["-23.0352", "-43.49314"],
  "Prainha": ["-23.0409", "-43.505515"],
  "Grumari": ["-23.0481", "-43.520316"],
  "Abricó": ["-23.0481", "-43.5128617"]
}


DOC_NAME="mytravel"
DOC_DESCRIPTION="This is my first mytravel"

BEACH_ICON="#beach"


beaches = KML.Folder(
        KML.name(FOLDER_NAME)
    )

for name, coords in BEACHES.items():
    beach = KML.Placemark(
        KML.name(name),
        KML.description(""),
        KML.styleUrl(BEACH_ICON),
        KML.Point(
           KML.coordinates(f"{coords[1]},{coords[0]}")
       )
    )
    beaches.append(beach)

style_normal = KML.Style(
    KML.IconStyle(
        KML.scale(1),
        KML.Icon(
            KML.href("images/icon-10.png")
        )
    ),
    KML.LabelStyle(
        KML.scale(0)
    ),
    id="beach-normal"
)

style_highlight = KML.Style(
    KML.IconStyle(
        KML.scale(1),
        KML.Icon(
            KML.href("images/icon-10.png")
        )
    ),
    KML.LabelStyle(
        KML.scale(0)
    ),
    id="beach-highlight"
)

style_map = KML.StyleMap(
    KML.Pair(
        KML.key("normal"),
        KML.styleUrl("#beach-normal")
    ),
    KML.Pair(
        KML.key("highlight"),
        KML.styleUrl("#beach-highlight")
    ),
    id="beach"
)


document = KML.Document(
        KML.name(DOC_NAME),
        KML.description(DOC_DESCRIPTION),
        style_normal,
        style_highlight,
        style_map
    )

document.append(beaches)

kml = KML.kml()
kml.append(document)
kml_string = etree.tostring(kml, pretty_print=True, encoding='utf-8', xml_declaration=True)

with open(FILENAME, 'wb') as f:
    f.write(kml_string)


print("KML file created successfully.")
