import requests
import barra_progreso

class Descargador:

    barra_progreso = barra_progreso.BarraProgreso()

    def descargar_archivo(self,url,nombre_archivo_local):
        
        # Transmitir el contenido para evitar cargar el archivo entero en memoria:
        with requests.get(url, stream=True) as solicitud:
             
            tamanyo_archivo = int(solicitud.headers.get('content-length'),0) 
            descargado = 0

            try:

                solicitud.raise_for_status() # Comprueba errores en la solicitud
                
                with open(nombre_archivo_local, 'wb') as archivo:
                    
                    print(f"\nDescargando {nombre_archivo_local}:")
                    for trozo in solicitud.iter_content(chunk_size=1024):
                        if trozo: # Filtrar trozos 'vivos'
                            archivo.write(trozo)

                            descargado+=len(trozo)
                            self.barra_progreso.imprimir_progreso_descarga(trozo, tamanyo_archivo, descargado) 
                    print(f"\nArchivo descargado y guardado en {nombre_archivo_local}")
                    
            except requests.exceptions.HTTPError as err:

                print(f"La URL es incorrecta: {err}")
