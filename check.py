from pyzbar.pyzbar import decode
import json
 

def validate(data):
    with open('data.json') as f:
        db = json.load(f)
        
    if data in db['ID']:
        name = db['Names'][db['ID'].index(data)]
        return name, (0, 255, 0)
    else:
        return 'Un-Authorized', (0, 0, 255)