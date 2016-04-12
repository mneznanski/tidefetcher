import requests
from xml.etree import ElementTree as ET

url = 'http://tidesandcurrents.noaa.gov/api/datagetter?' 
begin_date = 'begin_date=20151101'
end_date = 'end_date=20151130'
station = '&station=9437540'
product = '&product=predictions'
datum = '&datum=mllw'
url = url + begin_date + '&' + end_date
url += station + product + datum
url += '&interval=h&units=english&time_zone=lst_ldt&application=EOMG&format=xml'

response = requests.get(url)

tideData = ET.fromstring(response.content)

for entry in tideData:
    print entry.tag, entry.attrib