# GeoDOM - Contribución de Datasets

**Bienvenido al repositorio de contribuciones de datasets para [GeoDOM](geodom.adatar.do), una iniciativa de [Adatar](adatar.do).** Este espacio está dedicado a la comunidad interesada en aportar datasets relevantes para el análisis geoespacial y socioeconómico de la República Dominicana. Tu contribución ayudará a enriquecer el ecosistema de datos abiertos y estandarizados de GeoDOM.

## ¿Por qué contribuir?

* **Impacto:** Tus datos pueden ser utilizados por investigadores, planificadores, estudiantes y el público general para entender mejor la realidad dominicana.
* **Visibilidad:** Tu contribución será reconocida en la plataforma GeoDOM.
* **Colaboración:** Forma parte de una comunidad que busca fortalecer la infraestructura de datos del país.
* **Estandarización:** Ayúdanos a crear un conjunto de datos coherente y fácil de usar.

## Cómo contribuir un dataset

Para asegurar la calidad y consistencia de los datos en GeoDOM, te pedimos seguir estos pasos:

**1. Prepara tus archivos:**

Por cada dataset que desees contribuir, necesitarás dos archivos principales:

* **a) El archivo de datos:**
    * **Formatos preferidos:**
        * **JSON (.json):** Este es el único formato aceptado para los datasets. El archivo debe contener tanto los datos como los metadatos en un solo objeto JSON. Los datos tabulares deben ir en el atributo `data`, y los metadatos relevantes en otros atributos. En el futuro, podríamos requerir ciertos campos de metadatos específicos.
    * **Nomenclatura:** Nombra tu archivo de datos de forma descriptiva, usando guiones bajos o guiones para separar palabras (ej. `precipitacion_anual_estaciones_2023.json`).
    * **Metadatos mínimos requeridos en el archivo JSON:**
        * `title`: Título descriptivo del dataset.
        * `description`: Breve resumen del contenido y propósito del dataset.
        * `author`: Nombre de la persona u organización que creó/compiló los datos.
        * `dateCreated`: Fecha de creación o compilación del dataset.
        * `license`: Licencia bajo la cual se comparten los datos.
        * `tags`: Palabras clave relevantes (array de strings).
        * `spatialCoverage` y/o `temporalCoverage`: Cobertura geográfica y/o temporal.

* **b) El archivo README acompañante (`README.md`):**
    * Este archivo debe describir tu dataset en detalle, incluyendo todos los metadatos relevantes, contexto, fuente, cobertura, licencia, y cualquier otra información útil para los usuarios.
    * Incluye ejemplos de cómo utilizar el archivo JSON para análisis (por ejemplo, fragmentos de código en Python, R, etc.).
    * El objetivo es que cualquier persona pueda entender y reutilizar el dataset fácilmente solo leyendo este README.

**2. Proceso de Contribución en GitHub:**

* **a. Fork del repositorio:**
    * Haz un "Fork" de este repositorio (`https://github.com/GeoDOMProject/geodom-data-contributions`) a tu propia cuenta de GitHub.

* **b. Clona tu fork localmente:**
    ```bash
    git clone https://github.com/<TU_USUARIO_GITHUB>/geodom-data-contributions.git
    cd geodom-data-contributions
    ```

* **c. Crea una nueva rama:**
    * Crea una rama descriptiva para tu contribución:
        ```bash
        git checkout -b feature/dataset-<NOMBRE_DESCRIPTIVO_DEL_DATASET>
        ```

* **d. Añade tus archivos:**
    * Crea una nueva carpeta dentro del repositorio para tu dataset (ej. `datasets/nombre_descriptivo_del_dataset/`).
    * Coloca tu archivo de datos (`.json`) y tu archivo `README.md` en esa carpeta.
    * Asegúrate de que el archivo `README.md` esté bien documentado y explique claramente el contenido del dataset, su origen, y cómo utilizarlo.

* **e. Confirma tus cambios (commit y push):**
    ```bash
    git add .
    git commit -m "feat: Añade dataset [NOMBRE CORTO DEL DATASET]"
    git push origin feature/dataset-nombre-descriptivo-del-dataset
    ```

* **f. Crea una Pull Request (PR):**
    * Ve a tu fork en GitHub. Verás una opción para crear un "Pull Request" desde tu nueva rama.
    * Dirige el PR hacia la rama `main` del repositorio original (`GeoDOMProject/geodom-data-contributions`).
    * En la descripción del PR, proporciona un resumen de tu contribución y cualquier información adicional relevante para los revisores.

**3. Revisión y fusión:**

* El equipo de GeoDOM (Adatar) revisará tu Pull Request. Podemos hacer preguntas o sugerir cambios.
* Una vez aprobado, tu PR será fusionada.
* Un proceso automatizado (GitHub Action) se encargará de:
    1.  Validar los archivos (básico).
    2.  Subir tu dataset a nuestro almacenamiento en Cloudflare R2.
    3.  (Eventualmente) Actualizar el listado de datasets en el [geodom.adatar.do](geodom.adatar.do/dataset).

## ⚠️ Importante: Nombres únicos de datasets

> **Todos los archivos JSON de datasets deben tener un nombre único a nivel global en el repositorio.**
> 
> - El nombre del archivo `.json` y el de su carpeta deben coincidir (ejemplo: `datasets/mi_dataset/mi_dataset.json`).
> - No puede haber dos archivos `.json` con el mismo nombre, aunque estén en carpetas distintas.
> - Esto es necesario porque todos los datasets se almacenan juntos en la carpeta `datasets/` del almacenamiento en la nube (Cloudflare R2), sin subcarpetas.
> - Si subes un archivo con un nombre ya existente, sobrescribirás el dataset anterior.

Asegúrate de elegir nombres descriptivos y únicos para tus datasets.

## Criterios de aceptación (Generales)

* **Relevancia:** El dataset debe ser pertinente para la República Dominicana.
* **Calidad:** Aunque entendemos que los datos pueden tener limitaciones, se espera un esfuerzo razonable en la limpieza y documentación.
* **Metadatos:** El archivo JSON debe contener metadatos claros y completos, y el archivo `README.md` debe proporcionar contexto adicional.
* **Formato:** El dataset debe estar en formato JSON, como se especifica anteriormente.
* **Licencia:** Se prefieren licencias abiertas, pero se considerarán otras si están claramente especificadas y permiten la redistribución en GeoDOM.
* **Originalidad/Fuente:** Se debe indicar claramente la fuente original de los datos si no eres el autor primario.

## Código de conducta

Esperamos que todos los colaboradores sigan nuestro [Código de conducta](./CODE_OF_CONDUCT.md) para mantener un ambiente respetuoso y colaborativo.

## Licenciamiento de las contribuciones

Al contribuir un dataset, se espera que la licencia del mismo esté claramente especificada en los archivos correspondientes. GeoDOM simplemente actúa como una plataforma para alojar y dar visibilidad a estos datos bajo los términos que tú, como contribuidor, establezcas.

## ¿Preguntas o ayuda?

* Si tienes dudas sobre el proceso de contribución o necesitas ayuda técnica (especialmente si no estás familiarizado con Git/GitHub), abre un "issue" en [este repositorio](https://github.com/GeoDOMProject/geodom-data-contributions/issues).
* También puedes contactar al equipo de GeoDOM en [geodom@adatar.do](mailto:geodom@adatar.do).

**¡Gracias por considerar contribuir a GeoDOM!**