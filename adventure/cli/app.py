import rich
import typer
from tibia import Pipeline

from adventure.cli import level_generation
from adventure.cli.common import mount

app = (
    Pipeline(
        typer.Typer(
            name="adventure",
            add_completion=False,
        )
    )
    .map(mount(level_generation.app))
    .unwrap()
)


@app.command(name="ping")
def ping():
    rich.print("PONG!")
