import os.path
import zipfile
from find_dir import  CURRENT_DIR
'''
path = '/Users/rollnick/Desktop/QA Guru Projects/QAGuru9_7/tmp'
file_dir = os.listdir(path)

def open_zip():
    with zipfile.ZipFile('test.zip', mode='a') as zf:
        for file in zf.namelist():
            print(file)
'''
def make_zip():
    tmp_dir = os.path.join(CURRENT_DIR, "tmp")
    files = os.listdir(tmp_dir)
    with zipfile.ZipFile("resources/ZZZIPED.zip", mode='w', compression=zipfile.ZIP_DEFLATED, ) as zip_file:
        for file in files:
            add_file = os.path.join("tmp", file)
            zip_file.write(add_file)
            if file == "tmp/.DS_Store":
                continue