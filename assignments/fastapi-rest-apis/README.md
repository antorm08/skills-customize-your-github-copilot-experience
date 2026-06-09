# 📘 Asignación: Construyendo REST APIs con FastAPI

## 🎯 Objetivo

Aprender a diseñar e implementar una API REST usando el framework FastAPI. Los estudiantes crearán un servicio CRUD simple para gestionar recursos `items`, con validación, manejo de errores y documentación automática.

## 📝 Requisitos previos

- Conocimientos básicos de Python (funciones, tipos, estructuras de datos)
- Entorno con Python 3.8+

## 🛠️ Preparación

Instalar dependencias:

```bash
pip install -r assignments/fastapi-rest-apis/requirements.txt
```

Ejecutar la aplicación de desarrollo:

```bash
python assignments/fastapi-rest-apis/starter_code.py
```

La API quedará disponible en `http://127.0.0.1:8000`. La documentación automática estará en `http://127.0.0.1:8000/docs`.

## 📝 Tareas

### 🛠️ Tarea 1 — Implementar la API CRUD básica

#### Descripción
Crear y completar los endpoints para gestionar `items` con los métodos:
- `GET /items` — listar todos los items
- `GET /items/{item_id}` — obtener un item por id
- `POST /items` — crear un nuevo item
- `PUT /items/{item_id}` — actualizar un item
- `DELETE /items/{item_id}` — eliminar un item

#### Requisitos
- Usar modelos `pydantic` para validación de entrada/salida.
- Responder con códigos HTTP apropiados (200, 201, 204, 404, 400).
- Mantener datos en memoria (diccionario) para simplificar.

### 🛠️ Tarea 2 — Validación y documentación

#### Descripción
Asegurar que los campos requeridos son validados y aprovechar la documentación automática de FastAPI.

#### Requisitos
- Campos obligatorios: `name: str`, `description: Optional[str]`, `price: float`.
- Documentar ejemplos de request/response en el README.

### 🛠️ Tarea 3 — Manejo de errores y pruebas (opcional)

#### Descripción
Agregar manejo de errores y algunas pruebas unitarias simples.

#### Requisitos
- Devolver `404` si el `item_id` no existe.
- Escribir al menos 3 pruebas que verifiquen creación, lectura y borrado.

## ✅ Criterios de evaluación

- API funcional con todos los endpoints descritos.
- Validación correcta y códigos HTTP adecuados.
- Documentación mínima para ejecutar y probar la API.

---

Si quieres, puedo añadir pruebas unitarias, un archivo `Dockerfile` o integrarlo con GitHub Actions. ¿Qué prefieres como siguiente paso?