library(dplyr)
library(jsonlite)

dr_province <- tribble(
    ~PROV_CODE, ~PROV_NAME, ~PROV_ID,
    "NA", "_NA_", "00",
    "DN", "Distrito Nacional", "01",
    "AZU", "Azua", "02",
    "AZU", "Azua de Compostela", "02",
    "BAH", "Bahoruco", "03",
    "BAH", "Baoruco", "03",
    "BAR", "Barahona", "04",
    "DAJ", "Dajabón", "05",
    "DUA", "Duarte", "06",
    "EP", "Elías Piña", "07",
    "ES", "El Seibo", "08",
    "ES", "El Seybo", "08",
    "ESP", "Espaillat", "09",
    "IND", "Independencia", "10",
    "LA", "La Altagracia", "11",
    "LR", "La Romana", "12",
    "LV", "La Vega", "13",
    "MTS", "María Trinidad Sánchez", "14",
    "MC", "Monte Cristi", "15",
    "MC", "Montecristi", "15",
    "PED", "Pedernales", "16",
    "PER", "Peravia", "17",
    "PP", "Puerto Plata", "18",
    "HMI", "Hermanas Mirabal", "19",
    "SAL", "Salcedo", "19",
    "SAM", "Samaná", "20",
    "SC", "San Cristóbal", "21",
    "SJ", "San Juan", "22",
    "SJ", "San Juan de la Maguana", "22",
    "SPM", "San Pedro de Macorís", "23",
    "SRA", "Sánchez Ramírez", "24",
    "SAN", "Santiago", "25",
    "SAN", "Santiago de los Caballeros", "25",
    "SRO", "Santiago Rodríguez", "26",
    "VAL", "Valverde", "27",
    "MN", "Monseñor Nouel", "28",
    "MP", "Monte Plata", "29",
    "HMA", "Hato Mayor", "30",
    "SJO", "San José de Ocoa", "31",
    "SD", "Santo Domingo", "32"
) %>%
    relocate(PROV_ID, PROV_CODE, PROV_NAME)

# Convert to JSON
json_data <- toJSON(dr_province, dataframe = "rows", pretty = TRUE, auto_unbox = TRUE)

# Adjust JSON structure to include metadata and data keys
metadata <- list(
    title = "Listado de alias de las provincias de la República Dominicana",
    description = "Este archivo contiene un listado de las provincias de la República Dominicana junto con sus alias y códigos.",
    author = "Daniel E. de la Rosa",
    dateCreated = "2025-07-21",
    dateModified = Sys.Date(),
    tags = c("provincias", "alias", "república dominicana"),
    spatialCoverage = "República Dominicana",
    temporalCoverage = "2025 - Presente",
    license = "CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"
)

output <- list(
    metadata = metadata,
    data = dr_province
)

# Write to a JSON file
write_json(output, here::here("geodom-data-contributions", "datasets", "provincias_alias", "provincias_alias.json"), pretty = TRUE, auto_unbox = TRUE)
