import streamlit as st
import pandas as pd
import PyPDF2
import re

# Función para extraer el CUIL del texto
def extract_cuil(text):
    match = re.search(r'CUIL:\s*(\d+-\d+-\d+)', text)
    if match:
        return match.group(1)
    else:
        return None  # Cambiar a None para manejarlo más adelante

# Función para extraer el número de documento del CUIL
def extract_document_number(cuil):
    if cuil:
        return cuil.split('-')[1]  # Extraer el número entre los guiones
    return None

# Función para extraer el nombre completo del texto
def extract_name(text):
    match = re.search(r'Apellido y nombre:\s*([A-Za-zÁÉÍÓÚÑáéíóúñ\s]+)\s*CUIL:', text)
    if match:
        return match.group(1).strip()
    else:
        return None  # Cambiar a None para manejarlo más adelante

# Función para extraer la fecha de inicio del texto
def extract_start_date(text):
    match = re.search(r'Fecha Inicio:\s*([0-9]{2}/[0-9]{2}/[0-9]{4})', text, re.IGNORECASE)
    if match:
        return match.group(1)
    else:
        return None  # Cambiar a None para manejarlo más adelante

# Función para convertir PDF a Excel
def convert_pdf_to_excel(pdf_file):
    # Abre el archivo PDF en modo lectura binaria
    with open(pdf_file, 'rb') as file:
        # Crea un lector de PyPDF2
        reader = PyPDF2.PdfReader(file)

        # Extrae texto solo de la primera página
        first_page = reader.pages[0]
        full_text = first_page.extract_text()

        # Extraer los datos
        cuil = extract_cuil(full_text)
        # ... (resto de tus extracciones)

        # Crear el DataFrame
        data = {
            # ... (tus datos)
        }
        df = pd.DataFrame(data)

    # Guardar el DataFrame en un archivo .xlsx
    return df.to_excel("output.xlsx", index=False)

# Título de la aplicación
st.title("Conversor de PDF a Excel")

# Subir archivo PDF
uploaded_file = st.file_uploader("Selecciona un archivo PDF", type="pdf")

# Botón para iniciar la conversión
if uploaded_file is not None:
    # Guarda el archivo subido temporalmente
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Llama a tu función de conversión
    convert_pdf_to_excel("temp.pdf")

    # Descarga el archivo Excel
    with open("output.xlsx", "rb") as f:
        st.download_button(
            label="Descargar Excel",
            data=f,
            file_name="datos_extraidos.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )