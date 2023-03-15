import requests
from bs4 import BeautifulSoup



dct = {'rabota':[],
       '999':[]}

uniq=set()


def search_word(n,language):

    print('[+] Process start , wait please ........\n')

    for i in range(1,n):
        response = requests.get(f'https://www.rabota.md/ru/vacancies/category/it/{i}')
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            if link.get('href') != None:
                if language.lower() in link.get('href') and 'void' not in link.get('href'):
                    href = link.get('href')
                    if href[href.rfind('/'):] not in uniq:
                        dct['rabota'].append('https://www.rabota.md'+link.get('href'))
                        uniq.add(href[href.rfind('/'):])
    else:
        print('\n'.join(dct['rabota']))
        print('\n\n')
        print(f" Найдено записей  : -- > {len(dct['rabota'])}")



search_word(int(input('1.Введите кол-во страниц для поиска , желательно до 15 максимум ---- >: ')),
            input('2.Введите язык программирования который вам интересен для поиска ------- >: '))
