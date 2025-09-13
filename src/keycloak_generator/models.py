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
    client_role: bool = Field(False, alias="clientRole")
    composites: Optional[Dict[str, Any]] = None


class Client(BaseModel):
    client_id: str = Field(..., alias="clientId")
    secret: str
    public_client: bool = Field(False, alias="publicClient")
    redirect_uris: List[str] = Field([], alias="redirectUris")
    default_client_scopes: List[str] = Field([], alias="defaultClientScopes")
    optional_client_scopes: List[str] = Field([], alias="optionalClientScopes")


class Group(BaseModel):
    name: str
    realm_roles: List[str] = Field([], alias="realmRoles")


class UserFederationProvider(BaseModel):
    provider_name: str = Field(..., alias="providerName")
    config: Dict[str, Any]


class IdentityProviderMapper(BaseModel):
    name: str
    identity_provider_mapper: str = Field(..., alias="identityProviderMapper")
    config: Dict[str, Any]


class IdentityProvider(BaseModel):
    alias: str
    provider_id: str = Field(..., alias="providerId")
    enabled: bool = True
    config: Dict[str, Any]
    mappers: List[IdentityProviderMapper] = []


class AuthenticationExecution(BaseModel):
    authenticator: str
    requirement: str


class AuthenticationFlow(BaseModel):
    alias: str
    provider_id: str = Field(..., alias="providerId")
    description: Optional[str] = None
    authentication_executions: List[AuthenticationExecution] = Field([], alias="authenticationExecutions")


class ProtocolMapper(BaseModel):
    name: str
    protocol: str
    protocol_mapper: str = Field(..., alias="protocolMapper")
    config: Dict[str, Any]


class ClientScope(BaseModel):
    name: str
    protocol: str = "openid-connect"
    protocol_mappers: List[ProtocolMapper] = Field([], alias="protocolMappers")


class RequiredAction(BaseModel):
    alias: str
    enabled: bool = True
    default_action: bool = Field(False, alias="defaultAction")


class Realm(BaseModel):
    realm: str
    enabled: bool = True
    access_token_lifespan: Optional[int] = Field(None, alias="accessTokenLifespan")
    sso_session_idle_timeout: Optional[int] = Field(None, alias="ssoSessionIdleTimeout")
    sso_session_max_lifespan: Optional[int] = Field(None, alias="ssoSessionMaxLifespan")
    offline_session_idle_timeout: Optional[int] = Field(None, alias="offlineSessionIdleTimeout")
    first_broker_login_flow_alias: Optional[str] = Field(None, alias="firstBrokerLoginFlowAlias")
    browser_flow: Optional[str] = Field(None, alias="browserFlow")
    registration_flow: Optional[str] = Field(None, alias="registrationFlow")
    direct_grant_flow: Optional[str] = Field(None, alias="directGrantFlow")
    reset_credentials_flow: Optional[str] = Field(None, alias="resetCredentialsFlow")
    client_authentication_flow: Optional[str] = Field(None, alias="clientAuthenticationFlow")
    brute_force_protected: Optional[bool] = Field(None, alias="bruteForceProtected")
    clients: List[Client] = []
    roles: List[Role] = []
    users: List[User] = []
    groups: List[Group] = []
    user_federation_providers: List[UserFederationProvider] = Field([], alias="userFederationProviders")
    identity_providers: List[IdentityProvider] = Field([], alias="identityProviders")
    authentication_flows: List[AuthenticationFlow] = Field([], alias="authenticationFlows")
    client_scopes: List[ClientScope] = Field([], alias="clientScopes")
    required_actions: List[RequiredAction] = Field([], alias="requiredActions")
    smtp_server: Dict[str, Any] = Field({}, alias="smtpServer")
    components: Optional[Dict[str, Any]] = None
    attributes: Optional[Dict[str, Any]] = None
    browser_security_headers: Optional[Dict[str, Any]] = Field(None, alias="browserSecurityHeaders")
