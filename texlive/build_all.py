import os
import shutil
import subprocess as sp

def copy(f, d):
    ret = []
    for file_name in os.listdir(f):
        full_file_name = os.path.join(f, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, d)
            ret.append(file_name)
    return ret
def build(d):
    for a in os.listdir(d):
        pt = os.path.join(d, a)
        if a.endswith('.tex'):
            print(f'Compiling {pt}...')
            extra_files = copy(d, '.')
            out_dir = os.path.abspath(os.path.join('_build', d[d.index('/') + 1:])) #cut src/ from output dir
            os.makedirs(os.path.join(out_dir), exist_ok=True)
            sp.call(['pdflatex', '-output-directory', out_dir, a])
            for out in os.listdir(out_dir):
                if not out.endswith('.pdf'):
                    os.remove(os.path.join(out_dir, out))
            for ff in extra_files:
                os.remove(ff)
        else:
            if os.path.isdir(pt):
                build(pt)


build('src/')
