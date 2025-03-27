# Transferencia de archivos de directorio a otro

Características del Script

- El script permite transferir archivos de un directorio de origen a un directorio de destino. Puedes elegir entre copiar o mover (cortar) los archivos.
- Calcula y compara el hash SHA256 de los archivos antes y después de la transferencia para asegurar que no se corrompan durante el proceso.
- Antes de transferir un archivo, verifica que haya suficiente espacio en el destino.
- Si un archivo ya existe en el destino, el script pregunta si deseas sobrescribirlo.
- Todas las actividades y errores se registran en un archivo de log llamado transfer.log.
- Solicita al usuario que ingrese los directorios de origen y destino, y confirma la operación antes de proceder.


## Instalación

Abre una terminal y navega al directorio donde se encuentra el script
```bash
cd /[archivo]
sudo python script.py
```
    
El script te pedirá que ingreses el directorio de origen y el directorio de destino.

Elige si deseas "copiar" o "cortar" los archivos. Escribe tu elección y presiona Enter.

Si un archivo ya existe en el destino, el script te preguntará si deseas sobrescribirlo.

Revisa el archivo transfer.log para ver los detalles de la transferencia y cualquier error que haya ocurrido.
