from typing import Any, Callable

import typer
from tibia import curried


@curried
def mount(root: typer.Typer, sub: typer.Typer) -> typer.Typer:
    root.add_typer(sub)
    return root


@curried
def add_command(
    app: typer.Typer,
    command: Callable,
    *,
    name: str | None = None,
    help: str | None = None,
    context_settings: dict[Any, Any] | None = None,
    epilog: str | None = None,
    short_help: str | None = None,
    options_metavar: str = "[OPTIONS]",
    add_help_option: bool = True,
    no_args_is_help: bool = False,
    hidden: bool = False,
    deprecated: bool = False,
):
    app.command(
        name=name,
        help=help,
        context_settings=context_settings,
        epilog=epilog,
        short_help=short_help,
        options_metavar=options_metavar,
        add_help_option=add_help_option,
        no_args_is_help=no_args_is_help,
        hidden=hidden,
        deprecated=deprecated,
    )(command)

    return app
