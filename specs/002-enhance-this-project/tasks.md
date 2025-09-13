# Tasks: Enhance Realm Configuration

**Input**: Design documents from `/specs/002-enhance-this-project/`
**Prerequisites**: plan.md, research.md, data-model.md, quickstart.md

## Execution Flow (main)
```
1. Load plan.md from feature directory
   → If not found: ERROR "No implementation plan found"
   → Extract: tech stack, libraries, structure
2. Load optional design documents:
   → data-model.md: Extract entities → model tasks
   → contracts/: Each file → contract test task
   → research.md: Extract decisions → setup tasks
3. Generate tasks by category:
   → Setup: project init, dependencies, linting
   → Tests: contract tests, integration tests
   → Core: models, services, CLI commands
   → Integration: DB, middleware, logging
   → Polish: unit tests, performance, docs
4. Apply task rules:
   → Different files = mark [P] for parallel
   → Same file = sequential (no [P])
   → Tests before implementation (TDD)
5. Number tasks sequentially (T001, T002...)
6. Generate dependency graph
7. Create parallel execution examples
8. Validate task completeness:
   → All contracts have tests?
   → All entities have models?
   → All endpoints implemented?
9. Return: SUCCESS (tasks ready for execution)
```

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project structure as defined in `plan.md`.

## Phase 3.1: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.2
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [x] T001: [P] Write failing tests for the `Group` data model in `tests/test_models.py`.
- [x] T002: [P] Write failing tests for the `UserFederationProvider` data model in `tests/test_models.py`.
- [x] T003: [P] Write failing tests for the `IdentityProvider` data model in `tests/test_models.py`.
- [x] T004: [P] Write failing tests for the `AuthenticationExecution` and `AuthenticationFlow` data models in `tests/test_models.py`.
- [x] T005: Update the integration test in `tests/test_generator.py` to include assertions for groups, user federation, identity providers, auth flows, and extended realm settings, using the `enhanced-realm.yaml` from the quickstart. This test must fail.

## Phase 3.2: Core Implementation (ONLY after tests are failing)
- [ ] T006: [P] Implement the `Group` data model in `src/keycloak_generator/models.py`.
- [ ] T007: [P] Implement the `UserFederationProvider` data model in `src/keycloak_generator/models.py`.
- [ ] T008: [P] Implement the `IdentityProvider` data model in `src/keycloak_generator/models.py`.
- [ ] T009: [P] Implement the `AuthenticationExecution` and `AuthenticationFlow` data models in `src/keycloak_generator/models.py`.
- [ ] T010: Update the `Realm` data model in `src/keycloak_generator/models.py` to include the new entities and the extended realm settings.
- [ ] T011: Update the generator logic in `src/keycloak_generator/generator.py` to process the new configuration sections and include them in the final JSON output.

## Phase 3.3: Polish
- [ ] T012: [P] Update the `YAML_GUIDE.md` to document the new configuration options for groups, user federation, identity providers, authentication flows, and realm settings.

## Dependencies
- Model tests (T001-T004) must be done before model implementation (T006-T009).
- Integration test (T005) must be done before updating the generator logic (T011).
- Model implementation (T006-T010) must be done before updating the generator logic (T011).
- Core implementation (T006-T011) must be done before Polish (T012).

## Parallel Example
```
# The following model tests can be run in parallel:
Task: "T001: [P] Write failing tests for the Group data model in tests/test_models.py."
Task: "T002: [P] Write failing tests for the UserFederationProvider data model in tests/test_models.py."
Task: "T003: [P] Write failing tests for the IdentityProvider data model in tests/test_models.py."
Task: "T004: [P] Write failing tests for the AuthenticationExecution and AuthenticationFlow data models in tests/test_models.py."

# The following model implementations can be run in parallel after their tests are written:
Task: "T006: [P] Implement the Group data model in src/keycloak_generator/models.py."
Task: "T007: [P] Implement the UserFederationProvider data model in src/keycloak_generator/models.py."
Task: "T008: [P] Implement the IdentityProvider data model in src/keycloak_generator/models.py."
Task: "T009: [P] Implement the AuthenticationExecution and AuthenticationFlow data models in src/keycloak_generator/models.py."
```
