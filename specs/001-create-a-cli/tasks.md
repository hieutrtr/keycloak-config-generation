# Tasks: Keycloak Config Generation CLI

**Input**: Design documents from `/specs/001-create-a-cli/`
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

## Phase 3.1: Setup
- [x] T001: Create the directory structure: `src/keycloak_generator`, `tests/`.
- [x] T002: Create a `pyproject.toml` file defining the project metadata and dependencies: `click`, `PyYAML`, and `pytest`.
- [x] T003: [P] Configure `ruff` for linting in `pyproject.toml`.

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [x] T004: [P] Write failing tests for the `Credential` data model in `tests/test_models.py`.
- [x] T005: [P] Write failing tests for the `User` data model in `tests/test_models.py`.
- [x] T006: [P] Write failing tests for the `Role` data model in `tests/test_models.py`.
- [x] T007: [P] Write failing tests for the `Client` data model in `tests/test_models.py`.
- [x] T008: [P] Write failing tests for the `Realm` data model in `tests/test_models.py`.
- [x] T009: Write a failing integration test in `tests/test_generator.py` that uses a sample YAML file and asserts that the generated JSON is correct.
- [x] T010: Write a failing test for the CLI in `tests/test_cli.py` using `click.testing.CliRunner`.

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [x] T011: [P] Implement the `Credential` data model in `src/keycloak_generator/models.py`.
- [x] T012: [P] Implement the `User` data model in `src/keycloak_generator/models.py`.
- [x] T013: [P] Implement the `Role` data model in `src/keycloak_generator/models.py`.
- [x] T014: [P] Implement the `Client` data model in `src/keycloak_generator/models.py`.
- [x] T015: [P] Implement the `Realm` data model in `src/keycloak_generator/models.py`.
- [x] T016: Implement the YAML to JSON conversion logic in `src/keycloak_generator/generator.py`.
- [x] T017: Implement the CLI command in `src/keycloak_generator/cli.py` using `click`.

## Phase 3.4: Polish
- [ ] T018: [P] Create the `YAML_GUIDE.md` documentation file.
- [ ] T019: Add error handling to the CLI for file not found and invalid YAML errors.
- [ ] T020: [P] Write unit tests for error handling in `tests/test_cli.py`.
- [ ] T021: Finalize the `README.md` with updated usage instructions.

## Dependencies
- Setup (T001-T003) must be done first.
- Model tests (T004-T008) must be done before model implementation (T011-T015).
- Generator integration test (T009) must be done before generator implementation (T016).
- CLI test (T010) must be done before CLI implementation (T017).
- Core implementation (T011-T017) must be done before Polish (T018-T021).

## Parallel Example
```
# The following model tests can be run in parallel:
Task: "T004: [P] Write failing tests for the Credential data model in tests/test_models.py."
Task: "T005: [P] Write failing tests for the User data model in tests/test_models.py."
Task: "T006: [P] Write failing tests for the Role data model in tests/test_models.py."
Task: "T007: [P] Write failing tests for the Client data model in tests/test_models.py."
Task: "T008: [P] Write failing tests for the Realm data model in tests/test_models.py."

# The following model implementations can be run in parallel after their tests are written:
Task: "T011: [P] Implement the Credential data model in src/keycloak_generator/models.py."
Task: "T012: [P] Implement the User data model in src/keycloak_generator/models.py."
Task: "T013: [P] Implement the Role data model in src/keycloak_generator/models.py."
Task: "T014: [P] Implement the Client data model in src/keycloak_generator/models.py."
Task: "T015: [P] Implement the Realm data model in src/keycloak_generator/models.py."
```
