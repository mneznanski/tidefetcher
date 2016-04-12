import requests
from xml.etree import ElementTree as ET
import datetime
import calendar

def timeframe():
    year = datetime.date.today().year
    userin = int(raw_input("Enter a month as a number: "))
    monthdays = format(calendar.monthrange(year, userin)[1])
    if len(str(userin)) == 1:
        twodigmonth = '0' + str(userin)
    else:
        twodigmonth = str(userin)
    
    return "begin_date=" + str(year) + twodigmonth + "01&end_date=" + str(year) + twodigmonth + monthdays 

station = '&station=9437540'
product = '&product=predictions'
datum = '&datum=mllw'

url = 'http://tidesandcurrents.noaa.gov/api/datagetter?' 
url = url + timeframe()
url += station + product + datum
url += '&interval=h&units=english&time_zone=lst_ldt&application=EOMG&format=xml'

response = requests.get(url)

tideData = ET.fromstring(response.content)

for entry in tideData:
    print entry.tag, entry.attrib