import requests
from bs4 import BeautifulSoup

#способ 2
response = requests.get('https://coinmarketcap.com/')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features='html.parser')

    soup_list = soup.find_all('td', {'style': 'text-align:end'})
    print(soup_list[0].find('span').text)






#способ 1
'''result = []
response = requests.get('https://coinmarketcap.com/')

response_text = response.text
response_parse = response_text.split('<span>')

for element in response_parse:
    if element.startswith('$'):
        for element_2 in element.split('</span>'):
            if element_2.startswith('$') and element_2[1].isdigit():
                result.append(element_2)


print(result[0])'''

