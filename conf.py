import json
import uuid

def add_ident(json_data):
    if isinstance(json_data, list):
        for item in json_data:
            add_ident(item)
    elif isinstance(json_data, dict):
        if "ident" not in json_data:
            json_data["ident"] = str(uuid.uuid4())
        for value in json_data.values():
            add_ident(value)
file_path = r'C:\Users\345567\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\QGISWeblink\config\config.json'
with open(file_path, encoding='windows-1252') as json_file:
    data = json.load(json_file)
add_ident(data)
with open(file_path, 'w', encoding='windows-1252') as json_file:
    json.dump(data, json_file, indent=2, ensure_ascii=False)

print("JSON file updated successfully.")
