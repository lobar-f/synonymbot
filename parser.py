from bs4 import BeautifulSoup as BS
import requests

base_url='https://www.thesaurus.com/browse/'

def parser(url):
    r=requests.get(url)
    soup=BS(r.text, 'html.parser')
    words_list=soup.find_all('ul', class_="css-123gjy7 e1ccqdb60")
    return words_list
   
list_of_idioms=parser(base_url)
print(list_of_idioms)