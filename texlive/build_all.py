import os
import subprocess as sp

def build(d):
    for a in os.listdir(d):
        pt = os.path.join(d, a)
        if a.endswith('.tex'):
            print(f'Compiling {pt}...')
            out_dir = os.path.abspath(os.path.join('_build', d[d.index('/') + 1:])) #cut src/ from output dir
            os.makedirs(os.path.join(out_dir), exist_ok=True)
            sp.call(['pdflatex', '-output-directory', out_dir, a], cwd=d)
            for out in os.listdir(out_dir):
                if not out.endswith('.pdf'):
                    os.remove(os.path.join(out_dir, out))
        else:
            if os.path.isdir(pt):
                build(pt)


build('src/')
