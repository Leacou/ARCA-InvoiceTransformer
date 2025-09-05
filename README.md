# 🎈 A web app that transforms ARCA certificates into personalized excel sheets

### How to run it on your own machine# ARCA-InvoiceTransformer

Transformador automático de certificados ARCA a planillas Excel personalizadas.  
Ideal para contadores, administradores y equipos que necesitan agilizar la carga y análisis de datos de certificados ARCA.

---

## Descripción

**ARCA-InvoiceTransformer** es una aplicación web construida con Python y Streamlit que permite cargar archivos de certificados ARCA, procesarlos automáticamente y generar planillas Excel listas para usar en gestión contable, reportes o análisis.

---

## Tecnologías utilizadas

- **Python 3.8+**
- **Streamlit:** Framework para aplicaciones web interactivas en Python.
- **Pandas:** Manipulación y análisis de datos.
- **Openpyxl / xlsxwriter:** Generación y edición de archivos Excel.
- **HTML/CSS/JS:** Para el frontend generado por Streamlit.
- **Visual Studio Code:** Recomendado para edición y ejecución en Mac.

---

## Estructura del proyecto

```
ARCA-InvoiceTransformer/
├── streamlit_app.py       # Archivo principal de la app
├── requirements.txt       # Dependencias Python
├── README.md              # Este archivo
├── src/                   # (Opcional) Módulos y scripts auxiliares
├── data/                  # (Opcional) Archivos de ejemplo o test
├── out/                   # (Opcional) Carpeta de salida para los Excel generados
```

---

## Instalación y uso

### 1. Requisitos previos

- Tener **Python 3.8 o superior** instalado.
- Tener **pip** para instalar dependencias.
- Tener **Visual Studio Code** (recomendado).

### 2. Clona el repositorio

```sh
git clone https://github.com/Leacou/ARCA-InvoiceTransformer.git
cd ARCA-InvoiceTransformer
```

### 3. Instala las dependencias

```sh
pip install -r requirements.txt
```

### 4. Ejecuta la aplicación

```sh
streamlit run streamlit_app.py
```

- Se abrirá una ventana en tu navegador (usualmente: [http://localhost:8501](http://localhost:8501))
- Desde allí puedes cargar tus archivos ARCA y descargar el Excel generado.

---

## ¿Cómo funciona?

- **Carga:** El usuario selecciona un archivo de certificado ARCA (PDF, Excel o formato soportado).
- **Procesamiento:** El backend Python extrae los datos relevantes usando Pandas y los formatea según la lógica contable.
- **Exportación:** Se genera una planilla Excel personalizada y descargable.
- **Interfaz:** Streamlit proporciona botones, formularios y vistas amigables para el usuario.

---

## Personalización y desarrollo

- Puedes editar el archivo `streamlit_app.py` para cambiar el formato de salida.
- Para agregar nuevos tipos de certificado, adapta la lógica de procesamiento en los módulos correspondientes.
- Revisa la carpeta `src/` si quieres extender las funcionalidades.

---

## Contribuciones

¿Te gustaría mejorar la app?  
- Realiza un fork y abre un Pull Request.
- Sugiere mejoras o reporta bugs en el apartado Issues.

---

## Licencia

Este proyecto está bajo licencia Apache 2.0.  
Consulta el archivo LICENSE para más detalles.

---

## Contacto

¿Dudas o sugerencias?  
- Email: leacou@gmail.com
- GitHub: [Leacou](https://github.com/Leacou)

---
