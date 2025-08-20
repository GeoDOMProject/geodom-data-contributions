# Alias de Provincias de la República Dominicana

## Descripción

Este dataset contiene un listado completo de las provincias de la República Dominicana junto con sus códigos oficiales y variaciones de nombres (alias) comúnmente utilizados.

## Estructura de Datos

Cada registro contiene:

- **PROV_ID**: Código numérico de la provincia (01-32, más 00 para valores NA)
- **PROV_CODE**: Código alfabético de la provincia  
- **PROV_NAME**: Nombre de la provincia o alias

## Características Principales

- **32 provincias**: Incluye las 31 provincias oficiales más el Distrito Nacional
- **Múltiples alias**: Algunos registros incluyen variaciones del nombre (ej: "Azua" y "Azua de Compostela")
- **Códigos estándar**: Utiliza la codificación oficial del sistema administrativo dominicano
- **Manejo de valores nulos**: Incluye registro especial con ID "00" para valores NA

## Ejemplos de Uso

```r
# Cargar datos desde geodomR
library(geodomR)

# Limpiar nombres de provincias
provincias_limpias <- gd_clean_prov_name(c("santo domingo", "azua", "barahona"))

# Obtener datos de provincias con geometría
provincias_sf <- gd_provinces()
```

## Metadatos

- **Autor**: Daniel E. de la Rosa
- **Fecha de creación**: 2025-07-21
- **Última modificación**: 2025-07-24
- **Licencia**: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
- **Cobertura espacial**: República Dominicana
- **Cobertura temporal**: 2025 - Presente

## Validación

Este dataset ha sido validado usando el script `validate_geodom_dataset.py` y cumple con todos los estándares del proyecto GeoDOM.

## Enlaces Relacionados

- [Datos de geometría de provincias](../division_territorial_rd_ley_345_22/)
- [Alias de municipios](../municipios_alias/)
- [Alias de regiones](../regiones_alias/)
