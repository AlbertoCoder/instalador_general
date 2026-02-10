import tarfile
import sys
import barra_progreso
import os

class Descompresor_tar_gz:

    def descomprimir(self,ruta_tar,ruta_extracc):

        with tarfile.open(ruta_tar, "r:gz") as tar:

            try:

                miembros = tar.getmembers()
                total_archivos = len(miembros)

                for i, miembro in enumerate(miembros, start=1):
                    tar.extract(miembro,path=ruta_extracc)
                    progreso = (i/total_archivos) * 100
                    sys.stdout.write(f"\rExtrayendo: {progreso:.2f}% ({i}/{total_archivos})")
                    sys.stdout.flush()

                print(f"\n¡Extracción completa en {ruta_extracc}!")
            except:

                print(f"Hubo un error al extraer en {ruta_extracc}")
