from descargador import Descargador
from descompresor import Descompresor_tar_gz

url = "https://github.com/neovim/neovim/releases/latest/download/nvim-linux-x86_64.tar.gz"
nombre_archivo_local = url.split("/")[-1]

if __name__ == "__main__":

    descargador = Descargador()

    descargador.descargar_archivo(url, nombre_archivo_local)

    descompresor = Descompresor_tar_gz()

    descompresor.establecer_archivo("nvim-linux-x86_64.tar.gz", "/opt/")

    descompresor.descomprimir()




