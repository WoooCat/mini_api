from unittest.mock import patch

from cli_command import cli_app


@patch("cli_command.to_insert_data")
@patch("cli_command.to_create_tables")
def test_create_database_db_init_confirm(mock_to_create_tables, mock_to_insert_data, runner):
    result = runner.invoke(cli_app, ["create_database"], input="y")
    assert result.exit_code == 0
    assert result.exception is None
    mock_to_create_tables.assert_called_once()
    mock_to_insert_data.assert_called_once()


@patch("cli_command.to_insert_data")
@patch("cli_command.to_create_tables")
def test_create_database_db_init_not_confirm(mock_to_create_tables, mock_to_insert_data, runner):
    result = runner.invoke(cli_app, ["create_database"], input="n")
    assert result.exit_code == 0
    assert result.exception is None
    mock_to_create_tables.assert_called_once()
    mock_to_insert_data.assert_not_called()


@patch("cli_command.to_insert_data")
@patch("cli_command.to_create_tables")
def test_create_database_db_init_invalid_input(mock_to_create_tables, mock_to_insert_data, runner):
    result = runner.invoke(cli_app, ["create_database"], input="invalid_input")
    assert result.exit_code == 0
    assert result.exception is None
    mock_to_create_tables.assert_called_once()
    mock_to_insert_data.assert_not_called()


@patch("cli_command.to_insert_data")
@patch("cli_command.to_create_tables")
def test_create_database_without_commands(mock_to_create_tables, mock_to_insert_data, runner):
    result = runner.invoke(cli_app, [], input="y")
    assert result.exit_code == 2
    assert result.exception.args == (2,)
    mock_to_create_tables.assert_not_called()
    mock_to_insert_data.assert_not_called()
