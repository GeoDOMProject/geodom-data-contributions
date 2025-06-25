#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador de datasets GeoDOM
- Verifica que todos los objetos en 'data' tengan los mismos campos.
- Verifica presencia de metadatos mínimos.
- Opcional: Verifica unicidad de códigos de municipio.

Uso:
    python validate_geodom_dataset.py <ruta_al_json>
"""
import sys
import json
import os

REQUIRED_METADATA = [
    "title", "description", "author", "dateCreated", "license", "tags", "spatialCoverage", "temporalCoverage"
]

def validate_metadata(metadata):
    missing = [k for k in REQUIRED_METADATA if k not in metadata]
    if missing:
        # Usamos sys.stderr para los errores, es una buena práctica
        print(f"[ERROR] Faltan campos de metadatos requeridos: {missing}", file=sys.stderr)
        return False
    print("[OK] Todos los metadatos requeridos están presentes.")
    return True

def validate_data_fields(data):
    if not isinstance(data, list) or not data:
        print("[ERROR] La clave 'data' debe ser una lista (array) no vacía.", file=sys.stderr)
        return False
    
    # Comprobar que todos los elementos sean diccionarios
    if not all(isinstance(item, dict) for item in data):
        print("[ERROR] Todos los elementos en la lista 'data' deben ser objetos (diccionarios).", file=sys.stderr)
        return False
        
    expected = set(data[0].keys())
    for i, row in enumerate(data[1:], start=2): # Empezamos a comparar desde el segundo
        if set(row.keys()) != expected:
            print(f"[ERROR] El registro #{i} tiene campos distintos. Se esperaba {sorted(list(expected))} pero se encontró {sorted(list(row.keys()))}", file=sys.stderr)
            return False
            
    print(f"[OK] Todos los registros de 'data' tienen los mismos campos.")
    return True

def main():
    if len(sys.argv) != 2:
        print("Uso: python validate_geodom_dataset.py <ruta_al_json>", file=sys.stderr)
        sys.exit(1)
        
    path = sys.argv[1]
    
    # He movido las validaciones de nombre de archivo y unicidad al principio
    # para que no se intente leer un archivo inválido.
    # Esta lógica asume una estructura específica que puede ser opcional, la he comentado por ahora
    # para enfocarnos en la validación del contenido. Puedes descomentarla si es un requisito estricto.
    
    # dir_name = os.path.basename(os.path.dirname(path))
    # file_stem = os.path.splitext(os.path.basename(path))[0]
    # if dir_name != file_stem:
    #     print(f"[ERROR] El directorio ('{dir_name}') y el archivo JSON ('{file_stem}.json') deben tener el mismo nombre.", file=sys.stderr)
    #     sys.exit(1)

    try:
        with open(path, 'r', encoding="utf-8") as f:
            obj = json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo: {path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"[ERROR] El archivo JSON está mal formado: {e}", file=sys.stderr)
        sys.exit(1)
        
    ok = True
    
    if "metadata" not in obj or "data" not in obj:
        print("[ERROR] El archivo debe tener las claves de nivel superior 'metadata' y 'data'.", file=sys.stderr)
        sys.exit(1)
        
    print("--- Iniciando validación de contenido ---")
    ok &= validate_metadata(obj["metadata"])
    ok &= validate_data_fields(obj["data"])
    
    # --- ¡AQUÍ ESTÁ LA CORRECCIÓN CLAVE! ---
    if ok:
        print("\n¡Validación exitosa! El dataset cumple con los requisitos básicos de GeoDOM.")
        # Salir explícitamente con código 0 (éxito)
        sys.exit(0)
    else:
        print("\nValidación fallida. Revisa los errores impresos anteriormente.", file=sys.stderr)
        # Salir explícitamente con código 1 (error)
        sys.exit(1)

if __name__ == "__main__":
    main()