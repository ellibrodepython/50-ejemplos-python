# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install pypdf
# 2. Ejecuta el script: python 20_unir_pdfs.py
# 3. Observa el resultado en el archivo unidos.pdf

from pypdf import PdfWriter

pdf_writer = PdfWriter()
pdf_merger = PdfWriter()

pdf_writer.add_blank_page(595.28, 841.89)

with open("pdf1.pdf", "wb") as f:
    pdf_writer.write(f)

with open("pdf2.pdf", "wb") as f:
    pdf_writer.write(f)

with open("pdf1.pdf", 'rb') as file1:
    pdf_merger.append(file1)

with open("pdf2.pdf", 'rb') as file2:
    pdf_merger.append(file2)

with open("unidos.pdf", 'wb') as output_file:
    pdf_merger.write(output_file)