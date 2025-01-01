import yaml

with open('config.yaml', 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

SAVE_MD = config["debug"]["save-md"]
IMAGE_DIR = config["image-path"]
OUTPUT_DIR = config["output"]["dir"]
OUTPUT_FILE = config["output"]["file"]