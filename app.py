from bs4 import BeautifulSoup
import requests
from utils import cls
from imgViewer import openImg
from colors import *

SITE = "https://warframe.fandom.com/pt-br/wiki/Mods#ModList"
SITE_PREFIX = "https://warframe.fandom.com"


def scrap(title):
    html = requests.get(SITE).content
    soup = BeautifulSoup(html, 'html.parser')
    index = 0
    cls()
    for item in soup.find_all('div', attrs={'class': 'tabbertab', 'title': title}):
        for x in item.find_all('span', attrs={'class': 'mod-tooltip'}):
            index += 1
            print(f'Mod Name: {RED+x.text+RESET}')
            for y in x.find_all('a', href=True):
                print(f'Site: {CYAN} {SITE_PREFIX}' + y['href'] + RESET)

    print(f'\nPesquisamos por ({title}) e tivemos {index} resultados.')
    input('\n\nTecle ENTER para continuar !')


def scrapImg(imgLink):
    pass


while True:
    cls()

    opts = f"Options: {RED}warframe, rifle, pistola, arma branca, sentinela, kubrow, kavat, aura, postura - close (para sair do script){RESET}"
    print(opts)

    wat = input("\nOque vc procura: ")
    if not wat:
        break
    
    if wat == 'warframe':
        scrap('Warframe')

    elif wat == 'rifle':
        scrap('Rifle')
    
    elif wat == 'pistola':
        scrap('Pistola')
        
    elif wat == 'arma branca':
        scrap('Arma Branca')
    
    elif wat == 'sentinela':
        scrap('Sentinela')
        
    elif wat == 'kubrow':
        scrap('Kubrow')
    
    elif wat == 'kavat':
        scrap('Kavat')
    
    elif wat == 'aura':
        scrap('Aura')
    
    elif wat == 'postura':
        scrap('Postura')
    
    elif wat == 'close':
        break

    else:
        cls()
        print(f'Vc inseriu ({wat}) esta nao é uma opcao valida\n\nPor favor informe uma das opcoes acima !')
        input('\n\ntecle enter para continuar !')

cls()
print('\nScript ended !')