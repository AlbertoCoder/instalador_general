class BarraProgreso:

    def imprimir_progreso(self,paso,progreso_proyectado,progreso):
 
        progreso+=len(paso)
        completado = int(50*progreso/progreso_proyectado) if progreso_proyectado else 0
        print(f"\r[{'\u2588'*completado}{'.'*(50-completado)}] {round(descargado/1024/1024)}/{round(progreso_proyectado/1024/1024)} MB", end='')
