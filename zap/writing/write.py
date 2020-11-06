from metrics.metric import sessionamento_browser
from metrics.metric import sessionamento_device
from metrics.metric import sessionamento_os
import json
from pyspark.sql.functions import to_json, struct

path = "./arquivos_json/"

def write_browser():
    browser = sessionamento_browser()
    browser = browser.toJSON().collect()
    with open(path+'browser_family.json', 'w') as json_file:
        json.dump(browser, json_file)
    return 'Arquivo browser_family.json criado'

def write_device():
    device = sessionamento_device()
    device = device.toJSON().collect()
    with open(path+'device_family.json', 'w') as json_file:
        json.dump(device, json_file)
    return 'Arquivo device_family.json criado'

def write_os():
    os = sessionamento_os()
    os = os.toJSON().collect()
    with open(path+'os_family.json', 'w') as json_file:
        json.dump(os, json_file)
    return 'Arquivo os_family.json criado'
