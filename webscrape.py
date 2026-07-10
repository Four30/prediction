import requests
from bs4 import BeautifulSoup

url = "https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-advanced/cambridge-international-as-and-a-levels/grade-threshold-tables/november-2025/"
response = requests.get(url)
print(response)
#raw_html = BeautifulSoup(response.text,'html.parser')
#if response.status_code == 200:
#    headings = raw_html.find_all('div')
#    for heading in headings:
#        print(heading.text.strip())

#else:
#    print(response.status_code)
