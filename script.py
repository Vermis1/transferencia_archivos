import os
import shutil
import hashlib
import logging

# Configurar el registro
logging.basicConfig(filename='transfer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_hash(file_path):
    """Calcula el hash SHA256 de un archivo."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def check_disk_space(destination, required_space):
    """Verifica si hay suficiente espacio en el disco en el destino."""
    statvfs = os.statvfs(destination)
    available_space = statvfs.f_frsize * statvfs.f_bavail
    return available_space >= required_space

def transfer_files(source, destination, action):
    try:
        # Verificar si el directorio de destino existe
        if not os.path.exists(destination):
            os.makedirs(destination)

        # Transferir archivos
        for filename in os.listdir(source):
            source_file = os.path.join(source, filename)
            dest_file = os.path.join(destination, filename)
            if os.path.isfile(source_file):
                # Calcular hash del archivo de origen antes de transferirlo
                source_hash = calculate_hash(source_file)
                
                # Verificar espacio en disco
                file_size = os.path.getsize(source_file)
                if not check_disk_space(destination, file_size):
                    logging.error(f"Espacio insuficiente para transferir {filename}.")
                    print(f"Error: Espacio insuficiente para transferir {filename}.")
                    continue

                # Preguntar si se debe sobrescribir
                if os.path.exists(dest_file):
                    overwrite = input(f"El archivo {filename} ya existe en el destino. ¿Desea sobrescribirlo? (s/n): ")
                    if overwrite.lower() != 's':
                        logging.info(f"Archivo {filename} no sobrescrito.")
                        continue

                # Realizar la acción de transferencia
                if action == 'cortar':
                    shutil.move(source_file, dest_file)
                elif action == 'copiar':
                    shutil.copy2(source_file, dest_file)
                
                # Verificar la transferencia
                if os.path.exists(dest_file):
                    dest_hash = calculate_hash(dest_file)
                    if source_hash == dest_hash:
                        logging.info(f"Archivo {filename} transferido y verificado exitosamente.")
                        print(f"Archivo {filename} transferido y verificado exitosamente.")
                    else:
                        logging.error(f"Error: El archivo {filename} no coincide después de la transferencia.")
                        print(f"Error: El archivo {filename} no coincide después de la transferencia.")
                else:
                    logging.error(f"Error: El archivo {filename} no se encontró en el destino.")
                    print(f"Error: El archivo {filename} no se encontró en el destino.")
    except Exception as e:
        logging.error(f"Error al transferir archivos: {e}")
        print(f"Error al transferir archivos: {e}")

if __name__ == "__main__":
    source_dir = input("Introduce el directorio de origen: ")
    dest_dir = input("Introduce el directorio de destino: ")

    # Confirmar la operación
    confirm = input(f"¿Desea transferir archivos de {source_dir} a {dest_dir}? (s/n): ")
    if confirm.lower() == 's':
        action = input("¿Desea copiar o cortar los archivos? (copiar/cortar): ").lower()
        if action in ['copiar', 'cortar']:
            transfer_files(source_dir, dest_dir, action)
        else:
            print("Acción no válida. Operación cancelada.")
    else:
        print("Operación cancelada.")