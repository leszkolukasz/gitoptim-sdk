import typer

from . import subcommands

app = typer.Typer()

app.add_typer(subcommands.memlab.app, name="memlab")


@app.callback()
def main():
    """
    Gitoptim SDK
    """
