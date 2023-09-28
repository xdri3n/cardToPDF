from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def create_pdf_from_images(directory, output_pdf):
    img_width = 63 * 2.83465
    img_height = 88 * 2.83465
    margin = 5 * 2.83465

    total_img_width = 3 * img_width + 2 * margin
    total_img_height = 3 * img_height + 2 * margin

    margin_x = (A4[0] - total_img_width) / 2
    margin_y = (A4[1] - total_img_height) / 2

    images = [f for f in os.listdir(directory) if f.endswith('.jpg')]
    images.sort()

    c = canvas.Canvas(output_pdf, pagesize=A4)

    x = margin_x
    y = A4[1] - margin_y - img_height
    count = 0
    for img_path in images:
        img_path_full = os.path.join(directory, img_path)

        # Assurez-vous que l'image contient des coins arrondis avec un fond transparent
        c.drawImage(img_path_full, x, y, width=img_width, height=img_height, mask='auto')

        count += 1
        x += img_width + margin
        if count % 3 == 0:
            x = margin_x
            y -= img_height + margin
        if count % 9 == 0:
            x = margin_x
            y = A4[1] - margin_y - img_height
            c.showPage()

    c.save()

directory = "./1000"
output_pdf = "exemplaire.pdf"
create_pdf_from_images(directory, output_pdf)