import typer
from tibia import Pipeline

from . import voronoi

app = Pipeline(typer.Typer(name="generate-level")).map(voronoi.add).unwrap()
