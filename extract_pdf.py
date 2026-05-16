import fitz, os

pdf_path = r'C:\Users\01dar\Downloads\HOME.pdf'
out_dir  = r'C:\Users\01dar\wordpress_website\design-refs'
os.makedirs(out_dir, exist_ok=True)

doc  = fitz.open(pdf_path)
page = doc[0]

# Full page at 4x zoom for pixel-perfect detail
mat = fitz.Matrix(4, 4)
pix = page.get_pixmap(matrix=mat, alpha=False)
full_path = os.path.join(out_dir, 'full-page.png')
pix.save(full_path)
print("Full page: {}x{}px saved to {}".format(pix.width, pix.height, full_path))

# Extract all embedded images
imgs = page.get_images(full=True)
print("Embedded images: {}".format(len(imgs)))
for i, img in enumerate(imgs):
    xref    = img[0]
    base    = doc.extract_image(xref)
    ext     = base['ext']
    w, h    = base['width'], base['height']
    imgdata = base['image']
    path    = os.path.join(out_dir, 'img-{:02d}.{}'.format(i, ext))
    with open(path, 'wb') as f:
        f.write(imgdata)
    print("  [{}] {}x{} {} -> {}".format(i, w, h, ext, path))

doc.close()
print("Done.")
