import os, zipfile

base = 'mirofish-azimut-mvp'
zip_path = 'output/mirofish-azimut-mvp-latest.zip'
os.makedirs('output', exist_ok=True)

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, dirs, files in os.walk(base):
        for file in files:
            full = os.path.join(root, file)
            arc = os.path.relpath(full, '.')
            z.write(full, arc)

zip_path