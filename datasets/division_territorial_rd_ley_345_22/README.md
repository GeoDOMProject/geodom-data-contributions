# Dataset: División Territorial para Planificación (Ley 345-22)

Este dataset contiene la estructura jerárquica de la división territorial de la República Dominicana, definida específicamente para fines de planificación nacional, según lo establecido en la **Ley Orgánica No. 345-22**.

El objetivo de esta ley es crear un marco de regionalización único para orientar las políticas públicas, la inversión y la gestión del desarrollo de manera coherente en todo el territorio. Este dataset refleja las 10 Regiones Únicas de Planificación oficiales, junto con su composición de provincias y municipios.

## Metadatos

*   **Título:** División Territorial de la República Dominicana para Planificación (Ley 345-22)
*   **Descripción:** Estructura jerárquica de la división territorial de la República Dominicana, definida para fines de planificación, según la Ley Orgánica No. 345-22. El dataset está organizado en las 10 Regiones Únicas de Planificación oficiales, Provincias y Municipios. Los códigos de provincias y municipios se basan en la codificación de la Oficina Nacional de Estadística (ONE).
*   **Autor de la Compilación:** Adatar
*   **Fuente Primaria:**
    *   **Nombre:** Ley Orgánica de Regiones Únicas de Planificación de la República Dominicana, núm. 345-22.
    *   **Publicación:** Gaceta Oficial No. 11077 del 2 de agosto de 2022.
    *   **Fecha de Promulgación:** 29 de julio de 2022.
*   **Fecha de Creación del Dataset:** 2024-05-21
*   **Licencia de la Compilación:** CC0 1.0 Universal (Dominio Público)
*   **Cobertura Espacial:** República Dominicana
*   **Cobertura Temporal:** 2022 - Presente

## Estructura del archivo JSON

El archivo `division_territorial_rd_ley_345_22.json` está estructurado para ser cargado directamente en herramientas de análisis de datos como R o Python (Pandas).

El objeto JSON principal tiene dos claves:
1.  `metadata`: Un objeto que contiene información descriptiva sobre el dataset.
2.  `data`: Un array (lista) de objetos, donde **cada objeto representa un único municipio** en formato tabular. Esta estructura plana elimina la necesidad de procesar jerarquías anidadas.

```json
{
  "metadata": { ... },
  "data": [
    {
      "REG_NAME": "Cibao Norte",
      "REG_CODE": "01",
      "PROV_NAME": "Santiago",
      "PROV_CODE": "25",
      "MUN_NAME": "Santiago",
      "MUN_CODE": "2501"
    },
    {
      "REG_NAME": "Cibao Norte",
      "REG_CODE": "01",
      "PROV_NAME": "Santiago",
      "PROV_CODE": "25",
      "MUN_NAME": "Bisonó",
      "MUN_CODE": "2502"
    }
  ]
}
```

## Definición de campos (Columnas en DataFrame)

| Campo       | Descripción                                                                                               | Ejemplo                      |
| :---------- | :-------------------------------------------------------------------------------------------------------- | :--------------------------- |
| `REG_NAME`  | Nombre oficial de la Región Única de Planificación según la Ley 345-22.                                   | `Cibao Norte`                |
| `REG_CODE`  | Código de la Región Única de Planificación.                                                               | `01`                     |
| `PROV_NAME` | Nombre de la Provincia o Distrito Nacional.                                                               | `Santiago`                   |
| `PROV_CODE` | Código de la provincia según la Oficina Nacional de Estadística (ONE).                                    | `25`                         |
| `MUN_NAME`  | Nombre del Municipio.                                                                                     | `San José de las Matas`      |
| `MUN_CODE`  | Código único del municipio (concatenación de `PROV_CODE` y código municipal), según la ONE.               | `2505`                       |

## Ejemplos de uso (Python y R)

Gracias a la estructura tabular del JSON, cargarlo es un proceso de una sola línea tanto en Python como en R.

### 1. Cargar el JSON en un DataFrame de Pandas (Python)

```python
import pandas as pd
import json

# Asumiendo que el archivo está en la misma carpeta
file_path = 'division_territorial_rd_ley_345_22.json'

with open(file_path, 'r', encoding='utf-8') as f:
    full_data = json.load(f)

# Crear el DataFrame directamente desde la clave 'data'
df = pd.DataFrame(full_data['data'])

print("DataFrame cargado exitosamente. Primeras 5 filas:")
print(df.head())

# Ejemplo de análisis: Contar municipios por región
municipios_por_region = df.groupby('REG_NAME')['MUN_NAME'].count().sort_values(ascending=False)
print("\nConteo de municipios por Región de Planificación:")
print(municipios_por_region)
```

### 2. Cargar el JSON en un data.frame de R

```R
# Se necesita la librería 'jsonlite'
# install.packages("jsonlite")
library(jsonlite)

# Asumiendo que el archivo está en el directorio de trabajo
file_path <- "division_territorial_rd_ley_345_22.json"

# fromJSON convierte el archivo en una lista de R
full_data <- fromJSON(file_path)

# El elemento 'data' ya es un data.frame listo para usar
df <- full_data$data

# Ver las primeras filas
print("data.frame cargado exitosamente. Primeras 6 filas:")
head(df)

# Ejemplo de análisis (usando dplyr)
# install.packages("dplyr")
library(dplyr)
df %>%
  group_by(REG_NAME) %>%
  summarise(total_municipios = n()) %>%
  arrange(desc(total_municipios))
```

## Contexto adicional

>   **Importancia de la Ley 345-22:** Esta ley es fundamental para la administración pública dominicana, ya que busca estandarizar la planificación territorial. Antes de su promulgación, diferentes ministerios y agencias gubernamentales utilizaban distintas divisiones regionales (3, 5, 8 o 10 regiones), lo que generaba inconsistencias y dificultaba la coordinación interinstitucional. Esta ley establece un esquema único y obligatorio para toda la gestión del Estado.

## Cómo citar

Si utilizas este dataset en tu investigación o proyecto, por favor, cítalo de la siguiente manera:

> Adatar (2024). *Dataset: División Territorial para Planificación (Ley 345-22)*. GeoDOM. Recuperado de [geodom.adatar.do/datos/division_territorial_rd_ley_345_22](geodom.adatar.do/dataset/division_territorial_rd_ley_345_22)