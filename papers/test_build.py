import os, subprocess

base_dir = '/home/phrxmaz/Documents/CyberAlchemy/papers'
filename = '21_Quasicrystal_Physics.tex'
wrapper_path = os.path.join(base_dir, f"wrapper_{filename}")
with open(wrapper_path, "w") as f:
    f.write(r"""\documentclass[12pt,oneside]{book}
\input{common_preamble}
\begin{document}
\input{%s}
\end{document}
""" % filename)

print("Running tectonic...")
try:
    subprocess.run(['tectonic', wrapper_path], check=True)
except subprocess.CalledProcessError as e:
    print(f"Failed to build {filename}")
