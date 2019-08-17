"""
Python command line script to automate git project creation
"""
import click

@click.command()
@click.option('--name', required=True, prompt=True, help="Provide a name for your repo")
def cli(name):
    click.echo(name)
