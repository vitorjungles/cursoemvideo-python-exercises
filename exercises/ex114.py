import urllib.request
try:
    r = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('\033[0;31mSite Pudim não está acessível no momento.\033[m')
else:
    print('\033[0;33mSite Pudim acessado com sucesso.\033[m')
