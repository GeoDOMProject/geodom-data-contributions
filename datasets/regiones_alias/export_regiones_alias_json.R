library(dplyr)
library(jsonlite)

dr_region <- tribble(
    ~REG_ID, ~REG_CODE, ~REG_NAME,
    # Región NA (para valores faltantes)
    "00", "NA", "_NA_",
    
    # Cibao Norte (01)
    "01", "CNT", "Cibao Norte",
    "01", "CNT", "Región Cibao Norte",
    "01", "CNT", "Norte",
    "01", "CNT", "Cibao del Norte",
    
    # Cibao Sur (02)
    "02", "CSR", "Cibao Sur",
    "02", "CSR", "Región Cibao Sur",
    "02", "CSR", "Sur",
    "02", "CSR", "Cibao Central", # Alias histórico común
    "02", "CSR", "Central",
    
    # Cibao Nordeste (03)
    "03", "CND", "Cibao Nordeste",
    "03", "CND", "Región Cibao Nordeste",
    "03", "CND", "Nordeste",
    "03", "CND", "Cibao del Nordeste",
    
    # Cibao Noroeste (04)
    "04", "CNO", "Cibao Noroeste",
    "04", "CNO", "Región Cibao Noroeste",
    "04", "CNO", "Noroeste",
    "04", "CNO", "Cibao del Noroeste",
    
    # Valdesia (05)
    "05", "VAL", "Valdesia",
    "05", "VAL", "Región Valdesia",
    "05", "VAL", "Valle de San Juan",
    
    # Enriquillo (06)
    "06", "ENR", "Enriquillo",
    "06", "ENR", "Región Enriquillo",
    "06", "ENR", "Barahona",
    "06", "ENR", "Región Sur",
    
    # El Valle (07)
    "07", "EVA", "El Valle",
    "07", "EVA", "Región El Valle",
    "07", "EVA", "Valle",
    "07", "EVA", "San Juan",
    
    # Del Yuma (08)
    "08", "YUM", "Del Yuma",
    "08", "YUM", "Región Del Yuma",
    "08", "YUM", "Yuma",
    "08", "YUM", "Este",
    "08", "YUM", "Región Este",
    
    # Higuamo (09)
    "09", "HIG", "Higuamo",
    "09", "HIG", "Región Higuamo",
    "09", "HIG", "Monte Plata",
    
    # Ozama (10)
    "10", "OZM", "Ozama",
    "10", "OZM", "Región Ozama",
    "10", "OZM", "Distrito Nacional",
    "10", "OZM", "Gran Santo Domingo",
    "10", "OZM", "Metropolitana"
)

# Convert to JSON
json_data <- toJSON(dr_region, dataframe = "rows", pretty = TRUE, auto_unbox = TRUE)

# Adjust JSON structure to include metadata and data keys
metadata <- list(
    title = "Listado de aliases de las regiones de la República Dominicana",
    description = "Este archivo contiene un listado de las regiones de la República Dominicana junto con sus alias y códigos según la Ley 345-22.",
    author = "Daniel E. de la Rosa",
    dateCreated = "2025-07-21",
    dateModified = Sys.Date(),
    tags = c("regiones", "alias", "república dominicana", "ley 345-22"),
    spatialCoverage = "República Dominicana", 
    temporalCoverage = "2025 - Presente",
    license = "CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"
)

output <- list(
    metadata = metadata,
    data = dr_region
)

# Write to a JSON file
write_json(output, "regiones_alias.json", pretty = TRUE, auto_unbox = TRUE)
