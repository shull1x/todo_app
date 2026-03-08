import json
import os
from config import FILE_PATH

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)
