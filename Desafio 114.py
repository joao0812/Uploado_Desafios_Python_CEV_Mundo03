# Programa para verificar se um site está no ar ou bão, se foi possível achar o mesmo ou não

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Site do Pudim etá inacessível no momento')
else:
    print('Consegui acessar o site do Pudim')