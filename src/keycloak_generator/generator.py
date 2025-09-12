import json
from .models import Realm

def generate_json(data: dict) -> str:
    """
    Converts a dictionary to a Keycloak JSON structure.
    """
    realm = Realm(**data)
    return realm.model_dump_json(by_alias=True, indent=2)
