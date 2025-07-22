# Dataset: Aliases de Regiones de la República Dominicana

Este dataset contiene un listado de las regiones de la República Dominicana junto con sus aliases y códigos, basado en las 10 Regiones Únicas de Planificación establecidas en la **Ley Orgánica No. 345-22**.

## Metadatos

* **Título:** Listado de aliases de las regiones de la República Dominicana
* **Descripción:** Dataset que incluye nombres oficiales y variantes comunes (aliases) de las regiones de la República Dominicana para facilitar la limpieza y normalización de nombres en análisis de datos.
* **Autor de la Compilación:** Daniel E. de la Rosa (Adatar)
* **Fuente Primaria:** Ley Orgánica de Regiones Únicas de Planificación de la República Dominicana, núm. 345-22
* **Fecha de Creación del Dataset:** 2025-07-21
* **Licencia de la Compilación:** CC0 1.0 Universal (Dominio Público)
* **Cobertura Espacial:** República Dominicana
* **Cobertura Temporal:** 2025 - Presente

## Propósito

Este dataset está diseñado específicamente para ser utilizado en pipelines de limpieza y normalización de nombres de regiones en sistemas de análisis de datos. Permite reconocer variantes comunes, abreviaciones y errores tipográficos para mapearlos al nombre oficial correspondiente.

## Estructura del archivo JSON

El archivo `regiones_alias.json` contiene:
1. `metadata`: Información descriptiva sobre el dataset
2. `data`: Array de objetos con la estructura tabular de regiones y aliases

## Definición de campos

| Campo       | Descripción                                                                     | Ejemplo          |
| :---------- | :------------------------------------------------------------------------------ | :--------------- |
| `REG_ID`    | Código numérico de la región (2 dígitos con cero inicial)                     | `"01"`           |
| `REG_CODE`  | Código alfanumérico de la región (abreviación)                                | `"CNT"`          |
| `REG_NAME`  | Nombre oficial de la región según la Ley 345-22                              | `"Cibao Norte"`  |

## Ejemplos de aliases incluidos

- `"Región Cibao Norte"` → `"Cibao Norte"`
- `"Norte"` → `"Cibao Norte"`
- `"CN"` → `"Cibao Norte"`
- `"Yuma"` → `"Del Yuma"`
- `"Valle"` → `"El Valle"`
- `"Central"` → `"Cibao Sur"` (alias histórico)

## Uso recomendado

Este dataset está optimizado para ser usado con las funciones de limpieza de nombres del ecosistema GeoDOM, específicamente:

- `geodomR::gd_clean_region_name()` (en desarrollo)
- `geodomR::dr_clean_region_name()` (mejorado)

## Ejemplos de uso

### R con geodomR
```r
library(geodomR)

# Limpiar nombres de regiones
regiones_limpias <- gd_clean_region_name(c("norte", "Región Valdesia", "yuma"))
# Resultado: c("Cibao Norte", "Valdesia", "Del Yuma")
```

### Python con requests
```python
import requests
import json

# Cargar dataset desde GeoDOM
url = "https://geodom.adatar.do/dataset/regiones_alias"
response = requests.get(url)
data = response.json()

# Acceder a los datos
regiones = data['data']
print(f"Total de aliases: {len(regiones)}")
```

## Cómo citar

Si utilizas este dataset en tu investigación o proyecto, por favor, cítalo de la siguiente manera:

> de la Rosa, D. E. (2025). *Dataset: Aliases de Regiones de la República Dominicana*. GeoDOM. Recuperado de [geodom.adatar.do/dataset/regiones_alias](https://geodom.adatar.do/dataset/regiones_alias)

## Contribuir

Si identificas aliases adicionales o correcciones necesarias, puedes contribuir a través del repositorio [geodom-data-contributions](https://github.com/GeoDOMProject/geodom-data-contributions).
