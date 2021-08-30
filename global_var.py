from starlette.templating import Jinja2Templates
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LANG_FILE_PATH = os.path.join(ROOT_DIR, 'languages')
templates = Jinja2Templates(directory="templates")
