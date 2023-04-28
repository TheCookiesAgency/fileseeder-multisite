import os
from delete_dir import delete_dir

fs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
web_path = os.path.join(fs_path, 'web')
backo_path = os.path.join(fs_path, 'backoffice')
prueba1_path = os.path.join(fs_path, 'prueba1')
prueba2_path = os.path.join(fs_path, 'prueba2')
prueba3_path = os.path.join(fs_path, 'prueba3')
prueba4_path = os.path.join(fs_path, 'prueba4')
desyst_path = os.path.join(fs_path, 'design-system')

if os.path.exists(web_path):
    delete_dir(web_path)

if os.path.exists(backo_path):
    delete_dir(backo_path)

if os.path.exists(prueba1_path):
    delete_dir(prueba1_path)

if os.path.exists(prueba2_path):
    delete_dir(prueba2_path)

if os.path.exists(prueba3_path):
    delete_dir(prueba3_path)

if os.path.exists(prueba4_path):
    delete_dir(prueba4_path)

if os.path.exists(desyst_path):
    delete_dir(desyst_path)