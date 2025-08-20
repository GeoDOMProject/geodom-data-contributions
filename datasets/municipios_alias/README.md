# Alias de Municipios de la República Dominicana

## Descripción

Este dataset contiene un listado completo de los municipios de la República Dominicana junto con sus códigos oficiales y variaciones de nombres (alias) comúnmente utilizados.

## Estructura de Datos

Cada registro contiene:

- **MUN_ID**: Código numérico del municipio en formato PPDD donde:
  - PP = Código de la provincia (01-32)
  - DD = Código del municipio dentro de la provincia (01-99)
- **MUN_NAME**: Nombre del municipio o alias

## Características Principales

- **158 municipios**: Incluye todos los municipios oficiales de la República Dominicana
- **Múltiples alias**: Muchos registros incluyen variaciones del nombre oficial
  - Ejemplos: "Santo Domingo de Guzmán" / "Distrito Nacional"
  - "Santiago" / "Santiago de los Caballeros"
  - "Las Matas de Santa Cruz" / "Las Matas"
- **Códigos jerárquicos**: Los primeros dos dígitos corresponden al código de provincia
- **Manejo de valores nulos**: Incluye registro especial con ID "0000" para valores NA

## Ejemplos de Alias Comunes

| Nombre Oficial | Alias Comunes |
|----------------|---------------|
| Santo Domingo de Guzmán | Distrito Nacional |
| Santiago de los Caballeros | Santiago |
| San Pedro de Macorís | SPM |
| Las Yayas de Viajama | Las Yayas |
| San José de los Llanos | Los Llanos |

## Ejemplos de Uso

```r
# Cargar datos desde geodomR (función a implementar)
library(geodomR)

# Limpiar nombres de municipios
municipios_limpios <- gd_clean_municipality_name(c("santiago", "moca", "bonao"))

# Obtener datos de municipios con geometría
municipios_sf <- gd_municipalities()
```

## Relación con Provincias

Los códigos de municipio están directamente relacionados con las provincias:

- **01xx**: Distrito Nacional
- **25xx**: Santiago
- **32xx**: Santo Domingo
- Etc.

Esta estructura permite una fácil agregación y análisis por provincia.

## Metadatos

- **Autor**: Daniel E. de la Rosa
- **Fecha de creación**: 2025-08-20
- **Última modificación**: 2025-08-20
- **Licencia**: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
- **Cobertura espacial**: República Dominicana
- **Cobertura temporal**: 2025 - Presente

## Validación

Este dataset ha sido validado usando el script `validate_geodom_dataset.py` y cumple con todos los estándares del proyecto GeoDOM. Además, se ha verificado la consistencia de códigos de provincia con el dataset `provincias_alias`.

## Enlaces Relacionados

- [Alias de provincias](../provincias_alias/)
- [Datos de geometría de división territorial](../division_territorial_rd_ley_345_22/)
- [Alias de regiones](../regiones_alias/)
