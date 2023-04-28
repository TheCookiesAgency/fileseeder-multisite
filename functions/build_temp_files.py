import os


def build_temp_files( md_path, element ):

    root_path = os.getcwd()
    layout_path = os.path.join(root_path, 'temp_layout_fs.tsx')
    imports_path = os.path.join(root_path, 'temp_imports_fs.tsx')

    with open(md_path, "r") as file:

        organismos = []

        for line in file:
            if line.strip().startswith('# **'+element+'**'):
                for line in file:
                    if line.startswith('## '):
                        organismos.append(line[2:].strip())
                    elif line.strip() == "":
                        break
    

    with open(layout_path, 'w') as f:
        for organismo in organismos:
            f.write('      <'+organismo+' />\n')

    organismos.sort()

    with open(imports_path, 'w') as f:
        f.write('import Layout from "@thecookies/design-system/src/modules/Layout/Layout";\nimport { SEO } from "@thecookies/design-system/src/modules/SEO/SEO";\n')
        for organismo in organismos:
            f.write('import { '+organismo+' } from "@thecookies/design-system/src/sections/'+organismo+'/'+organismo+';"\n')