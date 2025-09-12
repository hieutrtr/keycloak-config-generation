from typing import List, Optional
from pydantic import BaseModel, Field


class Credential(BaseModel):
    type: str
    value: str
    temporary: bool = False


class User(BaseModel):
    username: str
    enabled: bool = True
    email: Optional[str] = None
    first_name: Optional[str] = Field(None, alias="firstName")
    last_name: Optional[str] = Field(None, alias="lastName")
    credentials: List[Credential] = []
    realm_roles: List[str] = Field([], alias="realmRoles")


class Role(BaseModel):
    name: str
    description: Optional[str] = None


class Client(BaseModel):
    client_id: str = Field(..., alias="clientId")
    secret: str
    public_client: bool = Field(False, alias="publicClient")
    redirect_uris: List[str] = Field([], alias="redirectUris")


class Realm(BaseModel):
    realm: str
    enabled: bool = True
    clients: List[Client] = []
    roles: List[Role] = []
    users: List[User] = []
