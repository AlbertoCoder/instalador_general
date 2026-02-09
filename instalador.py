import sys
import os
from descargador import Descargador
from descompresor import Descompresor_tar_gz

url = "https://github.com/neovim/neovim/releases/latest/download/nvim-linux-x86_64.tar.gz"
urls = []

def abrir_archivo_urls(ruta):
    with open(ruta,'r',encoding='utf-8') as archivo:
        for linea in archivo:
            urls.append(linea.strip())

def instalar(url,nombre_archivo_local):

    descargador = Descargador()

    descargador.descargar_archivo(url, nombre_archivo_local)

    descompresor = Descompresor_tar_gz()

    descompresor.establecer_archivo(nombre_archivo_local, "/opt/")

    descompresor.descomprimir()

def limpiar_pantalla():

    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def main():


    if len(sys.argv) > 1:

        print(f"Archivo de urls: {sys.argv[1]}")

        abrir_archivo_urls(sys.argv[1])

        for url in urls:
            instalar(url,url.split("/")[-1])

    else:

        print("Debes introducir el argumento de ruta del archivo de rutas.")

if __name__ == "__main__":

    limpiar_pantalla() 

    main()







