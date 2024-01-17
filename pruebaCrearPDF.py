import aspose.pdf as ap

# Inicializar objeto de documento
document = ap.Document()

# Añadir página
page = document.pages.add()

# Inicializar objeto fragmento de texto
text_fragment = ap.text.TextFragment("Hello, Joshua!")

# Agregar fragmento de texto a la nueva página
page.paragraphs.add(text_fragment)

# Guardar PDF actualizado
document.save("output.pdf")
