"""
Python command line script to automate git project creation
"""
import click
from src.functions.handler import create_repo

@click.command()
@click.option('-d', '--description', type=str, required=False, help="A short description of the repository")
@click.option('--private', required=False, is_flag=True, flag_value=True, default=False, show_default="False", help="Enable to create a private repository")
@click.option('--has-issues', type=bool, required=False, default=True, show_default="True", help="Either true to enable issues for this repository or false to disable them")
@click.option('--has-projects', type=bool, required=False, default=True, show_default="True", help="Either true to enable projects for this repository or false to disable them")
@click.option('--has-wiki', type=bool, required=False, default=True, show_default="True", help="Either true to enable the wiki for this repository or false to disable it")
@click.option('--is-template', type=bool, required=False, default=False, show_default="False", help="Either true to make this repo available as a template repository or false to prevent it")
@click.option('--auto-init', type=bool, required=False, default=False, show_default="False", help="Pass true to create an initial commit with empty README")
@click.option('--gitignore_template', required=False, help="Desired language or platform .gitignore template to apply. Use the name of the template without the extension")
@click.option('--license_template', required=False, help="Choose an open source license template that best suits your needs, and then use the license keyword as the license_template string")
@click.option('--allow-squash-merge', type=bool, required=False, default=True, show_default="True", help="Either true to allow squash-merging pull requests, or false to prevent squash-merging")
@click.option('--allow-merge-commit', type=bool, required=False, default=True, show_default="True", help="Either true to allow merging pull requests with a merge commit, or false to prevent merging pull requests with merge commits")
@click.option('--allow-rebase-merge', type=bool, required=False, default=True, show_default="True", help="Either true to allow rebase-merging pull requests, or false to prevent rebase-merging")
@click.argument('name', required=True)
@click.argument('token', required=True)
def cli(token, **kwargs):
    #After cleaning all data, pass to handler for POST request
    response = create_repo(token, kwargs)
