import streamlit as st
import fitz  # PyMuPDF
import io
import requests

st.title("Comandos de Linux")

opcion = st.radio("¿Cómo deseas cargar el PDF?", ["Desde GitHub", "Subir archivo PDF"])

def extraer_texto(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    texto = ""
    for page in doc:
        texto += page.get_text()
    return texto

texto_pdf = ""

if opcion == "Desde GitHub":
    url = st.text_input("Pega la URL RAW del PDF en GitHub:", "https://raw.githubusercontent.com/inefable12/comandos_basicos_linux/src/main/LinuxCommandReferenceFOSSwire.pdf")
    if url:
        try:
            response = requests.get(url)
            response.raise_for_status()
            texto_pdf = extraer_texto(response.content)
            st.success("PDF cargado exitosamente desde GitHub.")
        except Exception as e:
            st.error(f"No se pudo cargar el PDF desde la URL. Detalles: {e}")
else:
    archivo = st.file_uploader("Sube tu archivo PDF", type="pdf")
    if archivo:
        try:
            texto_pdf = extraer_texto(archivo.read())
            st.success("PDF cargado exitosamente desde archivo.")
        except Exception as e:
            st.error(f"No se pudo procesar el PDF. Detalles: {e}")

# Búsqueda si el PDF ya fue cargado
if texto_pdf:
    palabra = st.text_input("Escribe el comando o palabra a buscar:")
    if palabra:
        st.markdown(f"### Resultados para: `{palabra}`")
        lineas = texto_pdf.split("\n")
        resultados = [linea for linea in lineas if palabra.lower() in linea.lower()]
        if resultados:
            for r in resultados:
                st.write(f"- {r}")
        else:
            st.warning("No se encontraron coincidencias.")
