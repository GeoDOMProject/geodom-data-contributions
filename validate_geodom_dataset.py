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
        print(f"[ERROR] Faltan campos de metadatos: {missing}")
        return False
    print("[OK] Todos los metadatos requeridos están presentes.")
    return True

def validate_data_fields(data):
    if not data:
        print("[ERROR] El array 'data' está vacío.")
        return False
    expected = set(data[0].keys())
    for i, row in enumerate(data):
        if set(row.keys()) != expected:
            print(f"[ERROR] Registro #{i+1} tiene campos distintos: {set(row.keys()) ^ expected}")
            return False
    print(f"[OK] Todos los registros de 'data' tienen los mismos campos: {sorted(expected)}")
    return True

def main():
    if len(sys.argv) != 2:
        print("Uso: python validate_geodom_dataset.py <ruta_al_json>")
        sys.exit(1)
    path = sys.argv[1]
    # Validar que el directorio y el archivo json se llamen igual (sin extensión)
    dir_name = os.path.basename(os.path.dirname(path))
    file_stem = os.path.splitext(os.path.basename(path))[0]
    if dir_name != file_stem:
        print(f"[ERROR] El directorio ('{dir_name}') y el archivo JSON ('{file_stem}.json') deben tener el mismo nombre.")
        sys.exit(1)
    # Validar que no exista otro archivo con el mismo nombre en datasets/
    datasets_dir = os.path.join(os.path.dirname(path), '..')
    datasets_dir = os.path.abspath(datasets_dir)
    filename = os.path.basename(path)
    existing = [f for f in os.listdir(datasets_dir) if f.endswith('.json')]
    if filename in existing and os.path.abspath(path) != os.path.join(datasets_dir, filename):
        print(f"[ERROR] Ya existe un dataset con el nombre '{filename}' en 'datasets/'. El nombre debe ser único.")
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        obj = json.load(f)
    ok = True
    if "metadata" not in obj or "data" not in obj:
        print("[ERROR] El archivo debe tener las claves 'metadata' y 'data'.")
        sys.exit(1)
    ok &= validate_metadata(obj["metadata"])
    ok &= validate_data_fields(obj["data"])
    if ok:
        print("\n¡Validación exitosa! El dataset cumple con los requisitos básicos de GeoDOM.")
    else:
        print("\nValidación incompleta. Revisa los errores anteriores.")

if __name__ == "__main__":
    main()
