import glob
import re

masters = glob.glob('*Master.tex')
for m in masters:
    with open(m, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove local_bibs input
    content = re.sub(r'\\input\{local_bibs/local_bib_[^}]+\}\n?', '', content)
    # They should use unified_bibliography.tex or nothing (wait, they include the papers which now have their own bibs? 
    # Actually if a Master file compiles other chapters, each chapter now has \begin{thebibliography}. 
    # LaTeX allows multiple bibliographies if using chapterbib, but standard article/book might throw an error. 
    # We will just remove the input for now).
    
    with open(m, 'w', encoding='utf-8') as f:
        f.write(content)
