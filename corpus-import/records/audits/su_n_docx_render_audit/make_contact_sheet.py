from pathlib import Path
from PIL import Image, ImageDraw

render = Path(r"C:\Users\Alex\Downloads\_audit_su_n_docx_af3a56e7\render")
pages = [3, 6, 9, 13, 16, 21, 22]
thumbs = []
for page in pages:
    image = Image.open(render / f"page-{page:02d}.png").convert("RGB")
    image.thumbnail((500, 650))
    canvas = Image.new("RGB", (520, 690), "white")
    canvas.paste(image, ((520 - image.width) // 2, 30))
    ImageDraw.Draw(canvas).text((10, 8), f"Page {page}", fill="black")
    thumbs.append(canvas)

sheet = Image.new("RGB", (1040, 2760), "#dddddd")
for index, image in enumerate(thumbs):
    sheet.paste(image, ((index % 2) * 520, (index // 2) * 690))
sheet.save(render / "contact-key-pages.jpg", quality=86, optimize=True)
