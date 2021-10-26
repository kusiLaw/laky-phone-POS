import json
# from jsonschema import Draft4Valid



def custom_deserializer():
    # READ JSON FILE
    with open("dbsettings.json", "r", encoding='utf-8') as reader:
        return json.loads(reader.read())

def custom_serializer(obj):
    # WRITE JSON FILE
    with open("dbsettings.json", "w", encoding='utf-8') as writer:
        # json.dump(obj, writer,indent=2)
        writer.write(json.dumps(obj, indent=2))
        # My_db.deserialize()


__all__ = ['custom_deserializer','custom_serializer']
