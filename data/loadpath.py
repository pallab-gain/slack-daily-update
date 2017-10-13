import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def load_path():
    return os.path.join(ROOT_DIR,"data.txt")