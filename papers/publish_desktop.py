import os
import shutil

src_build = '/home/phrxmaz/Documents/CyberAlchemy/papers/build'
dest_desktop = '/home/phrxmaz/Desktop/LaRue_Research_Publications'

if os.path.exists(dest_desktop):
    shutil.rmtree(dest_desktop)

os.makedirs(os.path.join(dest_desktop, 'Master_Books'), exist_ok=True)
os.makedirs(os.path.join(dest_desktop, 'Volumes'), exist_ok=True)
os.makedirs(os.path.join(dest_desktop, 'Standalone_Papers'), exist_ok=True)

# Copy Master Books
for master in ['01_Principia_Psychedelia_Master.pdf', '01_Principia_Psychedelia_Full.pdf']:
    src = os.path.join(src_build, master)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(dest_desktop, 'Master_Books', master))
        print(f"Copied Master Book: {master}")

# Copy Volumes
vol_src = os.path.join(src_build, 'Volumes')
if os.path.exists(vol_src):
    for f in sorted(os.listdir(vol_src)):
        if f.endswith('.pdf'):
            shutil.copy2(os.path.join(vol_src, f), os.path.join(dest_desktop, 'Volumes', f))
            print(f"Copied Volume: {f}")

# Copy Standalone Papers
papers_src = os.path.join(src_build, 'papers')
if os.path.exists(papers_src):
    for f in sorted(os.listdir(papers_src)):
        if f.endswith('.pdf'):
            shutil.copy2(os.path.join(papers_src, f), os.path.join(dest_desktop, 'Standalone_Papers', f))
            print(f"Copied Paper: {f}")

print("\nSuccessfully published clean, canonical PDFs to ~/Desktop/LaRue_Research_Publications/")
