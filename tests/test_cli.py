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
            assert '{"realm": "test-realm"}' in f.read()

def test_cli_handles_file_not_found():
    """
    Tests that the CLI command handles a missing input file gracefully.
    """
    runner = CliRunner()
    result = runner.invoke(main, ["--input", "nonexistent.yaml", "--output", "output.json"])
    
    assert result.exit_code != 0
    assert "Error: Input file not found" in result.output
