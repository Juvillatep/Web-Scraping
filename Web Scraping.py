from bs4 import BeautifulSoup
from urllib.request import urlopen

def Obtener_Carreras(URL):
    Pagina = urlopen(URL)
    html = Pagina.read().decode("utf-8")
    InCarreras = html.find('<ul class="list-group">')
    FinCarreras = html.find('(SNIES 3 )</li>')
    Carreras = html[InCarreras:FinCarreras]
    Carreras = BeautifulSoup(Carreras, "html.parser")
    Texto = Carreras.get_text()
    Lista = Texto.split(')')
    print('Selecciona la carrera a la que pertenece:')
    for Palabra in range(len(Lista)):
        if '*' not in Lista[Palabra]:
            Insice = Lista[Palabra].find('(')
            Lista[Palabra] = Lista[Palabra][:Insice]
            print(Lista[Palabra])
        else:
            Insice = Lista[Palabra].find('*')
            Lista[Palabra] = Lista[Palabra][:Insice]
            print(Lista[Palabra])
def Main():
    URL = 'https://admisiones.unal.edu.co/pregrado/oferta-de-programas-curriculares/'
    Obtener_Carreras(URL)
Main()

