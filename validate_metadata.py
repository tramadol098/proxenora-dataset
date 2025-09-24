import json
import jsonschema
from jsonschema import validate

schema = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["id", "filename", "type", "category", "risk_level", "usage", "description"],
        "properties": {
            "id": {"type": "string"},
            "filename": {"type": "string"},
            "type": {"type": "string"},
            "category": {"type": "string"},
            "risk_level": {"type": "string"},
            "usage": {"type": "string"},
            "description": {"type": "string"}
        }
    }
}

with open("metadata.json") as f:
    data = json.load(f)

validate(instance=data, schema=schema)
print("✅ Metadata validation passed.") 
