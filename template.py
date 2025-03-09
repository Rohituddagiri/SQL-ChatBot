import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    ".env",
    "src/app.py",
]

for fp in list_of_files:
    fp = Path(fp)
    fileDir, fileName = os.path.split(fp)
    
    if fileDir != "":
        os.makedirs(fileDir, exist_ok=True)
        logging.info(f"Creating directory; {fileDir} for the file: {fileName}")
        
    if (not os.path.exists(fp)) or (os.path.getsize(fp) == 0):
        with open(fp, "w") as f:
            pass
            logging.info(f"Creating empty file: {fp}")
            
    else:
        logging.info(f"{fileName} already exists")