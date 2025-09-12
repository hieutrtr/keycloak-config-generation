import click
import yaml
import json
from .generator import generate_json

@click.command()
@click.option("--input", "-i", type=click.Path(exists=True), required=True, help="Path to the input YAML file.")
@click.option("--output", "-o", type=click.Path(), required=True, help="Path to the output JSON file.")
def main(input, output):
    """
    Generates a Keycloak realm configuration file from a YAML input.
    """
    try:
        with open(input, 'r') as f:
            data = yaml.safe_load(f)
        
        json_output = generate_json(data)
        
        with open(output, 'w') as f:
            f.write(json_output)
            
        click.echo(f"Generated Keycloak configuration at {output}")

    except FileNotFoundError:
        click.echo("Error: Input file not found.", err=True)
        raise click.Abort()
    except yaml.YAMLError as e:
        click.echo(f"Error parsing YAML file: {e}", err=True)
        raise click.Abort()

if __name__ == '__main__':
    main()
