import tarfile

class Descompresor_tar_gz:


    ruta_tar_gz = ""
    ruta_extracc = ""

    def establecer_archivo(self,ruta_archivo,ruta_extracc):

        self.ruta_tar_gz = ruta_archivo
        self.ruta_extracc = ruta_extracc


    def descomprimir(self):

        try:

            with tarfile.open(self.ruta_tar_gz, "r:gz") as tar:
                tar.extractall(path=self.ruta_extracc)
                print(f"Archivos extraidos en {self.ruta_extracc}")

        except:

            print("Ocurrió un error al extraer los archivos.")
