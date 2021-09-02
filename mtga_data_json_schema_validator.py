import sys
import glob
import json
from jsonschema import validate, ValidationError

if len(sys.argv) >= 2:
    json_dir = sys.argv[1]
else:
    json_dir = r'C:\\Program Files\\Wizards of the Coast\\MTGA\\MTGA_Data\\Downloads\\Data'

if len(sys.argv) >= 3:
    schema_dir = sys.argv[2]
else:
    schema_dir = r'json-schema'

mtga_files = glob.glob(json_dir+"\\*.mtga")
for mtga_file in mtga_files:
    mtga_file_name = mtga_file.split("\\")[-1]
    print("Validating {} ...".format(mtga_file_name))
    prefix = "_".join(mtga_file_name.split("_")[:2])
    schema_file_name = prefix+"_schema.json"

    with open(mtga_file, encoding="utf_8_sig") as json_file:
        try:
            json_obj = json.load(json_file)
        except json.JSONDecodeError as e:
            print(e.msg)
            continue

    with open(schema_dir+"\\"+schema_file_name, encoding="utf_8_sig") as schema_file:
        schema_obj = json.load(schema_file)

    try:
        validate(json_obj, schema_obj)
    except ValidationError as e:
        print(e.message)
    print("done.")
