# 📘 Assignment: Interfaz web interactiva con Streamlit

## 🎯 Objective

Construir una aplicación web interactiva usando Streamlit para explorar y visualizar un conjunto de datos. El objetivo es aprender a diseñar interfaces simples, usar widgets para entrada del usuario y crear visualizaciones reactivas — todo con Python.

## 📝 Tasks

### 🛠️ Diseñar la interfaz básica

#### Description
Crear la estructura de la app con un título, sidebar para controles y una zona principal para visualizaciones y tablas.

#### Requirements
Completed program should:

- Mostrar un título y texto de ayuda en la página principal.
- Incluir un `sidebar` con al menos dos controles interactivos (por ejemplo: selector de columna, rango de fechas o slider).
- Manejar carga de datos mediante un uploader de archivos (CSV) y usar un dataset de ejemplo si no se proporciona uno.

### 🛠️ Filtrado y exploración de datos

#### Description
Permitir al usuario filtrar las filas y explorar estadísticas resumidas del dataset cargado.

#### Requirements
Completed program should:

- Mostrar un resumen (número de filas, columnas, tipos de datos) del dataset.
- Aplicar los filtros seleccionados en el `sidebar` y mostrar una vista previa de los datos filtrados.
- Mostrar al menos una métrica o estadística calculada (media, mediana o conteo) basada en los filtros.

### 🛠️ Visualizaciones interactivas

#### Description
Agregar dos visualizaciones interactivas (por ejemplo: gráfico de líneas, barras o dispersión) que respondan a los controles del `sidebar`.

#### Requirements
Completed program should:

- Incluir al menos dos tipos de gráficos (p. ej., barras y dispersión) usando `altair` o `streamlit`.
- Los gráficos deben actualizarse cuando se cambian los controles del `sidebar`.
- Añadir opciones de personalización básicas (por ejemplo: cambiar columnas usadas en los ejes).

---

### Entregables

- `starter-code.py` con una plantilla funcional de Streamlit.
- `requirements.txt` con dependencias necesarias.
- `README.md` (este archivo) con instrucciones y criterios de evaluación.

### Evaluación (Criterios)

- Interfaz limpia y funcional: 30%
- Filtrado y estadísticas correctas: 30%
- Visualizaciones interactivas y reactivas: 30%
- Código legible y modular: 10%
