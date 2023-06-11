#!/usr/bin/env python3

import subprocess

def buscar_archivos_con_suid():
    """Esta función busca todos los archivos con el bit SUID establecido."""
    try:
        # Ejecuta el comando `find`
        proceso = subprocess.Popen(['find', '/', '-perm', '-4000', '-user', 'root', '-type', 'f', '-exec', 'ls', '-ldb', '{}', ';'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
        # Obtiene la salida del comando
        salida, _ = proceso.communicate()

        # Decodifica la salida de bytes a string y la divide en líneas
        archivos_suid = salida.decode('utf-8').split('\n')

        # Devuelve la lista de archivos
        return archivos_suid
    except Exception as e:
        print(f'Error durante la búsqueda de archivos con SUID: {e}')
        return None

def main():
    """Función principal."""
    print('Buscando archivos con el bit SUID establecido...')
    archivos_suid = buscar_archivos_con_suid()

    if archivos_suid is not None:
        print('Se encontraron los siguientes archivos con el bit SUID establecido:\n')
        for archivo in archivos_suid:
            print(archivo)

if __name__ == '__main__':
    main()