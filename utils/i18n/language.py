import glob
import json
import re


# from pydantic_i18n import JsonLoader, PydanticI18n

from global_var import LANG_FILE_PATH, templates

default_fallback = 'en'
languages = {}


language_list = glob.glob(LANG_FILE_PATH + "/*.json")
for lang in language_list:
    filename = lang.split('/')
    # TODO fins the real filename in the array
    r = re.compile(".+json")
    json_file = list(filter(r.match, filename))  # Read Note below
    lang_code = json_file[0].split('.')[0]

    with open(lang, 'r', encoding='utf8') as file:
        languages[lang_code] = json.load(file)



# for pydantic
# loader = JsonLoader(LANG_FILE_PATH)
# tr = PydanticI18n(loader)
