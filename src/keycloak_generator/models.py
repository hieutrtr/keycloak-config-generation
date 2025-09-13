from typing import List, Optional, Dict, Any
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
    credentials: List['Credential'] = []
    realm_roles: List[str] = Field([], alias="realmRoles")


class Role(BaseModel):
    name: str
    description: Optional[str] = None


class Client(BaseModel):
    client_id: str = Field(..., alias="clientId")
    secret: str
    public_client: bool = Field(False, alias="publicClient")
    redirect_uris: List[str] = Field([], alias="redirectUris")


class Group(BaseModel):
    name: str
    realm_roles: List[str] = Field([], alias="realmRoles")


class UserFederationProvider(BaseModel):
    provider_name: str = Field(..., alias="providerName")
    config: Dict[str, Any]


class IdentityProvider(BaseModel):
    alias: str
    provider_id: str = Field(..., alias="providerId")
    enabled: bool = True
    config: Dict[str, Any]


class AuthenticationExecution(BaseModel):
    authenticator: str
    requirement: str


class AuthenticationFlow(BaseModel):
    alias: str
    provider_id: str = Field(..., alias="providerId")
    description: Optional[str] = None
    authentication_executions: List[AuthenticationExecution] = Field([], alias="authenticationExecutions")


class Realm(BaseModel):
    realm: str
    enabled: bool = True
    access_token_lifespan: Optional[int] = Field(None, alias="accessTokenLifespan")
    sso_session_idle_timeout: Optional[int] = Field(None, alias="ssoSessionIdleTimeout")
    clients: List[Client] = []
    roles: List[Role] = []
    users: List[User] = []
    groups: List[Group] = []
    user_federation_providers: List[UserFederationProvider] = Field([], alias="userFederationProviders")
    identity_providers: List[IdentityProvider] = Field([], alias="identityProviders")
    authentication_flows: List[AuthenticationFlow] = Field([], alias="authenticationFlows")
