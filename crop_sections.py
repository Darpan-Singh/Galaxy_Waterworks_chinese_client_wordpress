import fitz, os

pdf_path = r'C:\Users\01dar\Downloads\HOME.pdf'
out_dir  = r'C:\Users\01dar\wordpress_website\design-refs\sections'
os.makedirs(out_dir, exist_ok=True)

doc  = fitz.open(pdf_path)
page = doc[0]
pw   = page.rect.width   # PDF points width
ph   = page.rect.height  # PDF points height
print("PDF page size: {}x{} pts".format(pw, ph))

# Crop sections as % of page height (estimated from design)
sections = [
    ('01-header',      0.000, 0.025),
    ('02-hero',        0.025, 0.130),
    ('03-trust',       0.130, 0.165),
    ('04-advantages',  0.165, 0.290),
    ('05-problems',    0.290, 0.430),
    ('06-technology',  0.430, 0.555),
    ('07-services',    0.555, 0.665),
    ('08-stats',       0.665, 0.775),
    ('09-appointment', 0.775, 0.850),
    ('10-cases',       0.850, 0.910),
    ('11-faq',         0.910, 0.960),
    ('12-cta',         0.960, 0.980),
    ('13-footer',      0.980, 1.000),
]

zoom = 2.5  # render at 2.5x for readability
mat  = fitz.Matrix(zoom, zoom)

for name, y0_pct, y1_pct in sections:
    y0 = ph * y0_pct
    y1 = ph * y1_pct
    clip = fitz.Rect(0, y0, pw, y1)
    pix  = page.get_pixmap(matrix=mat, clip=clip, alpha=False)
    path = os.path.join(out_dir, '{}.png'.format(name))
    pix.save(path)
    print("Saved {}: {}x{}px".format(name, pix.width, pix.height))

doc.close()
print("All sections saved to: {}".format(out_dir))
