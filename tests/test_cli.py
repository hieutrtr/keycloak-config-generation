import json
from click.testing import CliRunner
from keycloak_generator.cli import main


def test_cli_generates_output_file():
    """
    Tests that the CLI command generates an output file from an input file.
    """
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("input.yaml", "w") as f:
            f.write("realm: test-realm")

        result = runner.invoke(main, ["--input", "input.yaml", "--output", "output.json"])

        assert result.exit_code == 0
        assert "Generated Keycloak configuration" in result.output

        with open("output.json", "r") as f:
            output_data = json.load(f)
            assert output_data["realm"] == "test-realm"


def test_cli_handles_file_not_found():
    """
    Tests that the CLI command handles a missing input file gracefully.
    """
    runner = CliRunner()
    result = runner.invoke(main, ["--input", "nonexistent.yaml", "--output", "output.json"])

    assert result.exit_code != 0
    assert "does not exist" in result.output


def test_cli_handles_invalid_yaml():
    """
    Tests that the CLI command handles a syntactically incorrect YAML file.
    """
    runner = CliRunner()
    with runner.isolated_filesystem():
        # This is an invalid YAML structure that will cause a YAMLError
        with open("input.yaml", "w") as f:
            f.write("key1: value1\nkey2: value2:\n  subkey: subvalue")

        result = runner.invoke(main, ["--input", "input.yaml", "--output", "output.json"])

        assert result.exit_code != 0
        assert "Error: Could not parse YAML file" in result.output



def test_cli_handles_schema_validation_error():
    """
    Tests that the CLI command handles a semantically incorrect YAML file.
    """
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Missing the required 'realm' field
        with open("input.yaml", "w") as f:
            f.write("enabled: true")

        result = runner.invoke(main, ["--input", "input.yaml", "--output", "output.json"])

        assert result.exit_code != 0
        assert "Error: Invalid configuration schema" in result.output
        assert "Field required" in result.output  # Pydantic's error message
