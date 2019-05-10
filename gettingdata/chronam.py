import json

with open('nc-tenantfarmer.json') as json_file:  
    data = json.load(json_file)
    for p in data['items']:
        file = open(p['date']+p['title']+"pg"+p['page']+".txt", "w")
        file.write(p['ocr_eng'])
file.close()