import requests

class Descargador:

    def descargar_archivo(self,url,nombre_archivo_local):
        

        # Transmitir el contenido para evitar cargar el archivo entero en memoria:
        with requests.get(url, stream=True) as solicitud:
            
            tamanyo_total = int(solicitud.headers.get('content-length',0))
            tamanyo_trozo = 1024
            descargado = 0

            try:

                solicitud.raise_for_status() # Comprueba errores en la solicitud
                
                with open(nombre_archivo_local, 'wb') as archivo:
                    
                    for trozo in solicitud.iter_content(chunk_size=tamanyo_trozo):
                        if trozo: # Filtrar trozos 'vivos'
                            archivo.write(trozo)
                            descargado+=len(trozo)
                            completado = int(50*descargado/tamanyo_total) if tamanyo_total else 0
                            print(f"\r[{'\u2588'*completado}{'.'*(50-completado)}] {round(descargado/1024/1024)}/{round(tamanyo_total/1024/1024)} MB", end='')
                    print(f"\nArchivo descargado y guardado en {nombre_archivo_local}")
                    
            except requests.exceptions.HTTPError as err:

                print(f"La URL es incorrecta: {err}")
