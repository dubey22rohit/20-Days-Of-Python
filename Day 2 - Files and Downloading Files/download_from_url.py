import requests
import os
import shutil
THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOADS_DIR = os.path.join(BASE_DIR,"downloads")
os.makedirs(DOWNLOADS_DIR,exist_ok=True)

downloaded_img_path = os.path.join(DOWNLOADS_DIR,"1.jpg")
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Classic_view_of_a_cloudfree_Peyto_Lake%2C_Banff_National_Park%2C_Alberta%2C_Canada_%284110933448%29.jpg/240px-Classic_view_of_a_cloudfree_Peyto_Lake%2C_Banff_National_Park%2C_Alberta%2C_Canada_%284110933448%29.jpg"

#For small files
r = requests.get(url,stream = True)
r.raise_for_status()
with open(downloaded_img_path,'wb') as f:
    f.write(r.content)

#For large files
dl_filename = os.path.basename(url)
new_dl_path = os.path.join(DOWNLOADS_DIR,dl_filename)
with requests.get(url,stream = True) as r:
    with open(new_dl_path,'wb') as file_obj:
        shutil.copyfileobj(r.raw,file_obj)