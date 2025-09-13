# Tasks: Advanced Realm Configuration

**Input**: Design documents from `/specs/003-advanced-realm-configuration/`
**Prerequisites**: plan.md, research.md, data-model.md, quickstart.md

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project structure as defined in `plan.md`.

## Phase 3.1: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.2
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [ ] T001: [P] Write failing tests for the `ClientScope` and `ProtocolMapper` data models in `tests/test_models.py`.
- [ ] T002: [P] Write failing tests for the `RequiredAction` data model in `tests/test_models.py`.
- [ ] T003: [P] Write failing tests for the `IdentityProviderMapper` data model in `tests/test_models.py`.
- [ ] T004: Update the tests for the `Role` data model in `tests/test_models.py` to include assertions for composite roles (`clientRole` and `composites` fields). This test must fail.
- [ ] T005: Update the tests for the `IdentityProvider` data model in `tests/test_models.py` to include assertions for the new `mappers` field. This test must fail.
- [ ] T006: Create a new, failing integration test in `tests/test_generator.py` named `test_advanced_realm_generation`. This test must use the `production-realm.yaml` from the quickstart guide and assert that the generated JSON correctly includes all advanced features (composite roles, client scopes, mappers, brute force settings, required actions, SMTP config, etc.).

## Phase 3.2: Core Implementation (ONLY after tests are failing)
- [ ] T007: [P] Implement the `ClientScope` and `ProtocolMapper` data models in `src/keycloak_generator/models.py`.
- [ ] T008: [P] Implement the `RequiredAction` data model in `src/keycloak_generator/models.py`.
- [ ] T009: [P] Implement the `IdentityProviderMapper` data model in `src/keycloak_generator/models.py`.
- [ ] T010: Modify the existing `Role` data model in `src/keycloak_generator/models.py` to support composite roles by adding the `clientRole` and `composites` fields.
- [ ] T011: Modify the existing `IdentityProvider` data model in `src/keycloak_generator/models.py` to include the `mappers` list.
- [ ] T012: Update the main `Realm` data model in `src/keycloak_generator/models.py` to include all the new top-level fields: `clientScopes`, `requiredActions`, `browserFlow`, `registrationFlow`, `directGrantFlow`, `resetCredentialsFlow`, `clientAuthenticationFlow`, `bruteForceProtected`, `ssoSessionMaxLifespan`, `offlineSessionIdleTimeout`, `smtpServer`, `components`, `attributes`, and `browserSecurityHeaders`. Note that the `roles` list in the `Realm` model will now also accept the extended `Role` objects.
- [ ] T013: Update the generator logic in `src/keycloak_generator/generator.py` to process all the new and extended configuration sections and include them in the final JSON output.

## Phase 3.3: Polish
- [ ] T014: [P] Update the `YAML_GUIDE.md` to document all the new advanced configuration options, including composite roles, client scopes, protocol mappers, IdP mappers, required actions, and all new realm-level settings.

## Dependencies
- Model tests (T001-T005) must be done before model implementation (T007-T011).
- Integration test (T006) must be done before updating the generator logic (T013).
- Model implementation (T007-T012) must be done before updating the generator logic (T013).
- Core implementation (T007-T013) must be done before Polish (T014).

## Parallel Example
```
# The following model tests can be run in parallel:
Task: "T001: [P] Write failing tests for the ClientScope and ProtocolMapper data models in tests/test_models.py."
Task: "T002: [P] Write failing tests for the RequiredAction data model in tests/test_models.py."
Task: "T003: [P] Write failing tests for the IdentityProviderMapper data model in tests/test_models.py."

# The following model implementations can be run in parallel after their tests are written:
Task: "T007: [P] Implement the ClientScope and ProtocolMapper data models in src/keycloak_generator/models.py."
Task: "T008: [P] Implement the RequiredAction data model in src/keycloak_generator/models.py."
Task: "T009: [P] Implement the IdentityProviderMapper data model in src/keycloak_generator/models.py."
```