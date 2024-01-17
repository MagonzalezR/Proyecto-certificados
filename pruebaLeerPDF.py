# Import the necessary libraries 
from PIL import Image 
import pytesseract 
from pdf2image import convert_from_path
import aspose.pdf as ap

pdf_images = convert_from_path('C:/Users/Miguel/Downloads/Certificado_Habilidades_programacin_Web.pdf')

for idx in range(len(pdf_images)):
    pdf_images[idx].save('pdf_page_'+ str(idx+1) +'.png', 'PNG')
print("Successfully converted PDF to images")

# If you're on windows, you will need to point pytesseract to the path 
# where you installed Tesseract 
# pytesseract.pytesseract.tesseract_cmd = r'C:/path/to/tesseract.exe'
 
# Open the image file 
# replace 'test.png' with your image file 
img = Image.open('pdf_page_1.png')
 
# Use pytesseract to convert the image data to text 
text = pytesseract.image_to_string(img)
 
# Print the text print(text)
print(text)
document = ap.Document()

# Añadir página
page = document.pages.add()

# Inicializar objeto fragmento de texto
text_fragment = ap.text.TextFragment(text)

# Agregar fragmento de texto a la nueva página
page.paragraphs.add(text_fragment)

# Guardar PDF actualizado
document.save("output.pdf")
