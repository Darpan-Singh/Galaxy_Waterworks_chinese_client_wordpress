import shutil, os

src = r'C:\Users\01dar\wordpress_website\design-refs'
dst = r'C:\Users\01dar\wordpress_website\wp-content\themes\galaxy-waterproof\assets\images'
os.makedirs(dst, exist_ok=True)

mapping = {
    'img-18.jpeg': 'hero-bg.jpg',
    'img-14.jpeg': 'adv-1.jpg',    # inspector with thermal cam, apartment
    'img-20.jpeg': 'adv-2.jpg',    # engineer + client with tablet
    'img-13.jpeg': 'adv-3.jpg',    # window sealing caulk gun
    'img-11.jpeg': 'prob-rooftop.jpg',   # flooded rooftop
    'img-10.jpeg': 'prob-concrete.jpg',  # concrete spalling
    'img-09.jpeg': 'prob-window.jpg',    # cracked window mold
    'img-05.jpeg': 'prob-bathroom.jpg',  # bathroom mold tiles
    'img-06.jpeg': 'tech-polyurea.jpg',  # white rooftop (polyurea result)
    'img-22.jpeg': 'tech-insulation.jpg',# hazy white rooftop HK skyline
    'img-15.jpeg': 'svc-1.jpg',    # worker applying waterproofing rooftop
    'img-16.jpeg': 'svc-2.jpg',    # exterior wall plastering
    'img-04.jpeg': 'svc-3.jpg',    # modern rooftop drainage (insulation)
    'img-17.jpeg': 'svc-4.jpg',    # bathroom waterproofing work
    'img-19.jpeg': 'svc-5.jpg',    # clean window interior
    'img-12.jpeg': 'svc-6.jpg',    # injection grouting
    'img-07.jpeg': 'worker.jpg',   # FLIR camera man (stats section)
    'img-08.jpeg': 'faq-worker.jpg', # FAQ man with tablet + toolkit
    'img-00.jpeg': 'case-1.jpg',   # 翠擁華庭
    'img-01.jpeg': 'case-2.jpg',   # 盈翠半島
    'img-02.jpeg': 'case-3.jpg',   # 御凱
    'img-03.jpeg': 'case-4.jpg',   # 帝寶城
    'img-21.jpeg': 'cta-bg.jpg',   # rainy HK window
}

for src_file, dst_name in mapping.items():
    s = os.path.join(src, src_file)
    d = os.path.join(dst, dst_name)
    shutil.copy2(s, d)
    print('Copied {} -> {}'.format(src_file, dst_name))

print('Done. {} images copied.'.format(len(mapping)))
