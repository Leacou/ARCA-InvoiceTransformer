import streamlit as st
import pandas as pd
import PyPDF2
import re
import io
import logging


# Función para extraer el CUIL del texto
def extract_cuil(text):
    match = re.search(r'CUIL:\s*(\d+-\d+-\d+)', text)
    if match:
        return match.group(1)
    return None

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
    return None

# Función para extraer la fecha de inicio del texto
def extract_start_date(text):
    match = re.search(r'Fecha Inicio:\s*([0-9]{2}/[0-9]{2}/[0-9]{4})', text, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def convert_pdf_to_excel(pdf_file):
    try:
        # Usa el contenido del archivo subido directamente
        reader = PyPDF2.PdfReader(pdf_file)

        # Extrae texto solo de la primera página
        first_page = reader.pages[0]
        full_text = first_page.extract_text()

        # Extraer los datos
        cuil = extract_cuil(full_text)
        document_number = extract_document_number(cuil)
        name = extract_name(full_text)
        start_date = extract_start_date(full_text)

        # Procesar el nombre para dividir en apellido y nombre
        if name:
            name_parts = name.split()
            apellido = name_parts[0] if name_parts else ""
            nombre = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""
        else:
            apellido = ""
            nombre = ""

        # Crear el DataFrame con los datos requeridos
        data = {
            "Nro. Legajo": [0],
            "Apellido": [apellido],
            "Nombre": [nombre],
            "Sexo": [0],
            "Nacionalidad": ["argentina"],
            "Tipo Documento": ["dni"],
            "CUIL": [cuil],
            "Fecha Nacimiento": ["01/01/2000"],
            "Nro. Documento": [document_number],
            "Estado Civil": ["soltero"],
            "Calle": ["Mitre"],
            "Nro. Calle": [1000],
            "Código Postal": [1400],
            "Provincia": ["Prov. Bs As"],
            "Fecha de Antigüedad Rec.": [start_date],
            "Fecha de Ingreso": [start_date],
            "Forma de Pago": ["efectivo"]
        }

        df = pd.DataFrame(data)

        # Guardar el DataFrame en un archivo en memoria
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        output.seek(0)
        
        return output
    except Exception as e:
        logging.error(f"Error al convertir PDF a Excel: {e}")
        return None

# Título de la aplicación
st.title("Conversor de PDF a Excel 2")

# Subir archivo PDF
uploaded_file = st.file_uploader("Selecciona un archivo PDF", type="pdf")

# Botón para iniciar la conversión
if uploaded_file is not None:
    # Llama a tu función de conversión
    excel_data = convert_pdf_to_excel(uploaded_file)

    # Descarga el archivo Excel
    st.download_button(
        label="Descargar Excel",
        data=excel_data,
        file_name="datos_extraidos.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
