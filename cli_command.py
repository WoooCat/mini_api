from typing import Optional

import typer

from src.db.db_tools import to_create_tables, to_insert_data
from src.db.models import db_tables_list

cli_app = typer.Typer()


@cli_app.callback()
def before_commands():
    pass


@cli_app.command("create_database")
def _create_database(
    create_tables: Optional[bool] = typer.Option(default=True),
    init_database: Optional[bool] = typer.Option(default=False, prompt=True),
) -> None:
    """Initialize the app_database.db, required creating tables and optionally inserting data."""
    if create_tables:
        to_create_tables()
    if init_database:
        to_insert_data(db_tables_list)


if __name__ == "__main__":
    cli_app()
