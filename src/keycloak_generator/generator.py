import json
from .models import (
    Realm,
    Client,
    Credential,
    User,
    Role,
    Group,
    UserFederationProvider,
    IdentityProvider,
    AuthenticationFlow,
    AuthenticationExecution,
)


def generate_json(data: dict) -> str:
    """
    Converts a dictionary parsed from YAML into a Keycloak JSON structure.

    The function relies on Pydantic models to perform the validation and
    structuring. The top-level `Realm` model encompasses all other models,
    so simply parsing the data into the `Realm` model is sufficient.
    """
    realm = Realm(**data)
    return realm.model_dump_json(by_alias=True, indent=2, exclude_none=True)
