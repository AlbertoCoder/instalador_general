import requests

class Descargador:

    def descargar_archivo(self,url,nombre_archivo_local):

        # Transmitir el contenido para evitar cargar el archivo entero en memoria:
        with requests.get(url, stream=True) as solicitud:

            try:

                solicitud.raise_for_status() # Comprueba errores en la solicitud
                
                with open(nombre_archivo_local, 'wb') as archivo:
                    
                    for trozo in solicitud.iter_content(chunk_size=8192):
                        if trozo: # Filtrar trozos 'vivos'
                            archivo.write(trozo)


                    print(f"Archivo descargado y guardado en {nombre_archivo_local}")
                    
            except requests.exceptions.HTTPError as err:

                print(f"La URL es incorrecta: {err}")


