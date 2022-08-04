from Bio import Entrez
from Bio import SeqIO
from Bio import GenBank
import re
import pandas as pd
import matplotlib.pyplot as plt
import csv as csv
    
def download_pubmed (keyword):
    """
    El siguiente comando permite buscar articulos en pubmed mediante palabras claves
    """
     
    Entrez.email = 'jefferson.hernandez@est.ikiam.edu.ec'
    busq = Entrez.read(Entrez.esearch(db="pubmed", 
                            term=keyword,
                            usehistory="y"))
    webenv = busq["WebEnv"]
    query_key = busq["QueryKey"]
    handle = Entrez.efetch(db="pubmed",
                           rettype="medline", 
                           retmode="text", 
                           retstart=0,
                           retmax=543, webenv=webenv, query_key=query_key)
    data = handle.read()
    dataexp = re.sub(r'\n\s{6}','', data)
    return dataexp
    

def mapscience(archivo):
    """Este comando genera un mapa de ciencia de los paises de los autores"""
    bytes(archivo, encoding="utf8")
    contentsse = re.sub(r'\s+[Eceinlort]{10}\s+[aders]{7}.*','',archivo)
    contentssc = re.sub(r'\s[\w._%+-]+@[\w.-]+\.[a-zA-Z]{1,4}','',contentsse)
    contentsna = re.sub(r'\..\d.\,',',',contentssc)
    contentsnu = re.sub(r'\..\d.','',contentsna)
    x=contentsnu[1:].split('PMID-')
    AD1=[]
    for PMID in x:
        q=PMID.split('\n')
        for fila in q:
            w=fila.split(' ')
            if w[0] == 'AD':
                e=fila.split(',')
                AD1.append(e[-1])
    
    b=0
    AD2 =[0]*len(AD1)
    for obj in AD1:
        bytes(obj,encoding="utf8")
        if obj != '':
            g=obj
            if g[0] == ' ':
                g = re.sub (r'^\s','',g)
            if g[-1] == '.':
                g = re.sub (r'\.$','',g)
            g = re.sub (r'\.$','',g)
            g = re.sub (r'\s$','',g)
        AD2[b]=g
        b=b+1
    Countries_molde=['Andorra','United Arab Emirates ','Afghanistan','Antigua and Barbuda','Anguilla','Albania','Armenia','Netherlands Antilles','Angola','Antarctica','Argentina','American Samoa','Austria','Australia','Aruba','Azerbaijan','Bosnia and Herzegovina','Barbados','Bangladesh','Belgium','Burkina Faso','Bulgaria','Bahrain', 'Burundi','Benin','Bermuda','Brunei','Bolivia', 'Brazil','Bahamas','Bhutan','Bouvet Island','Botswana','Belarus','Belize','Canada','Cocos [Keeling] Islands','Congo [DRC]','Central African Republic','Congo [Republic]', 'Switzerland',"Côte d'Ivoire",'Cook Islands','Chile','Cameroon','China','Colombia','Costa Rica','Cuba', 'Cape Verde','Christmas Island','Cyprus','Czech Republic','Germany','Djibouti','Denmark','Dominica','Dominican Republic','Algeria','Ecuador' ,'Estonia','Egypt','Western Sahara','Eritrea','Spain','Ethiopia','Finland','Fiji','Falkland Islands [Islas Malvinas]','Micronesia','Faroe Islands','France','Gabon', 'United Kingdom','Grenada','Georgia','French Guiana','Guernsey','Ghana','Gibraltar','Greenland','Gambia', 'Guinea','Guadeloupe','Equatorial Guinea','Greece','South Georgia and the South Sandwich Islands','Guatemala','Guam','Guinea-Bissau','Guyana','Gaza Strip','Hong Kong','Heard Island and McDonald Islands','Honduras','Croatia', 'Haiti','Hungary','Indonesia','Ireland' ,'Israel','Isle of Man','India','British Indian Ocean Territory','Iraq', 'Iran','Iceland','Italy','Jersey','Jamaica','Jordan', 'Japan','Kenya','Kyrgyzstan','Cambodia','Kiribati','Comoros','Saint Kitts and Nevis','North Korea','South Korea','Kuwait','Cayman Islands','Kazakhstan','Laos','Lebanon','Saint Lucia','Liechtenstein','Sri Lanka','Liberia','Lesotho','Lithuania','Luxembourg','Latvia' ,'Libya','Morocco','Monaco','Moldova','Montenegro','Madagascar','Marshall Islands','Macedonia [FYROM]','Mali','Myanmar [Burma]','Mongolia' ,'Macau','Northern Mariana Islands','Martinique','Mauritania','Montserrat','Malta','Mauritius','Maldives','Malawi','Mexico','Malaysia' ,'Mozambique','Namibia','New Caledonia','Niger','Norfolk Island','Nigeria','Nicaragua','The Netherlands','Norway','Nepal','Nauru', 'Niue','New Zealand','Oman','Panama','Peru','French Polynesia', 'Papua New Guinea','Philippines','Pakistan','Poland','Saint Pierre and Miquelon' ,'Pitcairn Islands','Puerto Rico','Palestinian Territories','Portugal','Palau','Paraguay','Qatar','Réunion','Romania', 'Serbia','Russia' ,'Rwanda','Saudi Arabia','Solomon Islands','Seychelles','Sudan','Sweden','Singapore','Saint Helena','Slovenia', 'Svalbard and Jan Mayen','Slovakia','Sierra Leone','San Marino','Senegal','Somalia','Suriname','São Tomé and Príncipe','El Salvador','Syria', 'Swaziland' ,'Turks and Caicos Islands','Chad','French Southern Territories','Togo','Thailand','Tajikistan','Tokelau','Timor-Leste','Turkmenistan' ,'Tunisia','Tonga','Turkey','Trinidad and Tobago','Tuvalu','Taiwan','Tanzania','Ukraine','Uganda','U.S. Minor Outlying Islands','United States of America','Uruguay','Uzbekistan','Vatican City','Saint Vincent and the Grenadines','Venezuela', 'British Virgin Islands','U.S. Virgin Islands','Vietnam','Vanuatu','Wallis and Futuna','Samoa','Kosovo','Yemen','Mayotte','South Africa','Zambia','Zimbabwe']
    AD3=AD2
    f=Countries_molde
    i=len(f)
    ADi=[0]*i
    k=0
    for elem in f:
        d=0
        for comp in AD3:
            if elem == str(comp):
                d=d+1
        ADi[k]=d
        k=k+1
    
    AD4=[]
    Cy=[]
    n=0
    for elem in ADi:
        if str(elem) != '0':
            AD4.append(elem)
            m=Countries_molde[n]
            Cy.append(m)
        n=n+1
        
    zip_coordinates = {}
    with open('Data/countries.txt') as f:
        csvr = csv.DictReader(f)
        for row in csvr:
            zip_coordinates[row['name']] = [float(row['latitude']),
                                            float(row['longitude'])]
    code = []
    long = []
    lat = []
    count = AD4
    for inte in Cy:
        if inte in zip_coordinates.keys():
            code.append(inte)
            lat.append(zip_coordinates[inte][0])
            long.append(zip_coordinates[inte][1])
    plt.scatter(long, lat, s = count, c= count)
    plt.colorbar()
    ard = dict(arrowstyle="->")
    plt.annotate('Singapore', xy = (103.819836, 1.352083), 
                 xytext = (110, 8), arrowprops = ard)
    plt.annotate('Guatemala', xy = (-90.230759, 15.783471), 
                 xytext = (-110, 20.4292), arrowprops= ard)
    plt.annotate('Belgium', xy = (4.469936, 50.503887),
                 xytext = (0, 55.25), arrowprops= ard)
    plt.annotate('United States of America', xy = (-95.712891,37.09024),
                 xytext = (-85.1106, 45.3736), arrowprops= ard)
    plt.annotate('Chile', xy = (-71.542969, -35.675147),
                 xytext = (-85.1106, -30.3736), arrowprops= ard)
    params = plt.gcf()
    plSize = params.get_size_inches()
    params.set_size_inches( (plSize[0] * 3, plSize[1] * 3) )
    plt.xlabel('Longitud')
    plt.ylabel('Latitud')
    plt.title('Mapa de nubes, distribución de autores por país')
    plt.savefig('img/Mapa de nubes 02.jpg', dpi=300, bbox_inches='tight')
    img = plt.show()
        
    return img
