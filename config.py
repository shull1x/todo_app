import os

DATA_DIR = "data"
FILE_NAME = "tasks.json"
FILE_PATH = os.path.join(DATA_DIR, FILE_NAME)

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
