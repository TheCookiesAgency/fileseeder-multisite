import os
import glob
import re
import argparse
import sys
from functions.build_temp_files import build_temp_files
from functions.fileseeder import fileseeder
import subprocess

root_path = os.getcwd()
fs_path = os.path.dirname(os.path.abspath(__file__))
stc_path = os.path.join(root_path, 'structure/structure_*.md')
his_path = os.path.join(root_path, 'historial_fs.txt')
rs_path = os.path.join(fs_path, 'functions/read_history.py')

md_files = glob.glob(stc_path)

if len(md_files) > 0:
    md_paths = md_files
else:
    raise FileNotFoundError(f"No se encontró ningún archivo structure.md")

parser = argparse.ArgumentParser()
parser.add_argument('--force', help='Ejecutar una operación forzada', action='store_true')
parser.add_argument('--show', help='Muestra toda la salida', action='store_true')
parser.add_argument('--web', help='Crea solo los archivos que se crean en web', action='store_true')
parser.add_argument('--backoffice', help='Crea solo los archivos que se crean en backoffice', action='store_true')
args = parser.parse_args()

if args.web == False and args.backoffice == False:
    args.web = True
    args.backoffice = True

sys.stdout = open(his_path, 'w')

for md_path in md_paths:

    web = md_path.split('/')[-1].split('_')[1].split('.')[0]

    with open(md_path, 'r') as structure:
        for linea in structure:
            page_match = re.search(r'^# \*\*(\w+)\*\*', linea)
            page_match_default = re.search(r'^# \*\*(\w+)\*\*$', linea)
            page_match_traduccion = re.search(r'^# \*\*(\w+)\*\* - ', linea)
            if page_match:
                camelName = page_match.group(1)
                if page_match_traduccion:
                    kebabTraduccion = linea.split(' - ')[1]
                if args.web:
                    build_temp_files(md_path, camelName)
                    if args.force:
                        if page_match_traduccion:
                            fileseeder( web, "gpag", camelName, kebabTraduccion, True, True)
                        if page_match_default:
                            fileseeder( web, "gpag", camelName, None, True)
                        fileseeder( web, "land", camelName, None, True)
                    if page_match_traduccion:
                        fileseeder( web, "gpag", camelName, kebabTraduccion, False, True)
                    if page_match_default:
                        fileseeder( web, "gpag", camelName)
                    fileseeder( web, "land", camelName)
                if args.backoffice:
                    if args.force:
                        fileseeder( web, "sdoc", camelName, None, True)
                    fileseeder( web, "sdoc", camelName)
            template_match = re.search(r'^# (\w+)', linea)
            template_match_default = re.search(r'^# (\w+)$', linea)
            template_match_traduccion = re.search(r'^# (\w+) - ', linea)
            if template_match:
                camelName = template_match.group(1)
                if template_match_traduccion:
                    kebabTraduccion = linea.split(' - ')[1]
                if args.web:
                    build_temp_files(md_path, camelName)
                    if args.force:
                        if page_match_traduccion:
                            fileseeder( web, "gtemp", camelName, kebabTraduccion, True, True)
                        if page_match_default:
                            fileseeder( web, "gtemp", camelName, None, True)
                        fileseeder( web, "land", camelName, None, True)
                    if template_match_traduccion:
                        fileseeder( web, "gtemp", camelName, kebabTraduccion, False, True)
                    if template_match_default:
                        fileseeder( web, "gtemp", camelName)
                    fileseeder( web, "land", camelName)
                if args.backoffice:
                    if args.force:
                        fileseeder( web, "sdoc", camelName, None, True)
                    fileseeder( web, "sdoc", camelName)
            organism_match = re.search(r'^## (\w+)$', linea)
            if organism_match:
                camelName = organism_match.group(1)
                if args.web:
                    if args.force:
                        fileseeder( web, "org", camelName, None, True)
                    fileseeder( web, "org", camelName)
                if args.backoffice:
                    if args.force:
                        fileseeder( web, "sobj", camelName, None, True)
                    fileseeder( web, "sobj", camelName)
            molecule_match = re.search(r'^### (\w+)$', linea)
            if molecule_match:
                camelName = molecule_match.group(1)
                if args.web:
                    if args.force:
                        fileseeder( web, "mol", camelName, None, True)
                    fileseeder( web, "mol", camelName)

sys.stdout.close()

if args.show:
    subprocess.call(["python3", rs_path , "--show" ])
else:
    subprocess.call(["python3", rs_path ])