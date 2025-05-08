import streamlit as st
import fitz  # PyMuPDF

# URL del PDF en GitHub
PDF_URL = "https://github.com/inefable12/comandos_basicos_linux/blob/main/LinuxCommandReferenceFOSSwire.pdf"

st.title("Buscador de Comandos en PDF de Linux")

# Descargar y leer el PDF desde el enlace
def leer_pdf(url):
    # Cargar PDF desde URL
    doc = fitz.open(stream=fitz.open(url=url).write(), filetype="pdf")
    texto_total = ""
    for page in doc:
        texto_total += page.get_text()
    return texto_total

texto_pdf = leer_pdf(PDF_URL)

# Entrada de palabra clave
palabra_clave = st.text_input("Introduce una palabra o comando a buscar:")

# Mostrar resultados si se introduce una palabra
if palabra_clave:
    st.markdown(f"### Resultados para: `{palabra_clave}`")
    lineas = texto_pdf.split("\n")
    resultados = [linea for linea in lineas if palabra_clave.lower() in linea.lower()]
    
    if resultados:
        for res in resultados:
            st.write(f"- {res}")
    else:
        st.warning("No se encontraron coincidencias.")
