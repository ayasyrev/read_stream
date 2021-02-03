from typer.testing import CliRunner

from read_stream.console import app

from read_stream import __version__

runner = CliRunner()


def test_app():
    url = 'aaa'
    url_2 = 'bbb'
    # default_save_name = 'stream'
    save_name_1 = 'stream_1'
    save_name_2 = 'stream_2'
    # result = runner.invoke(app, ['-v'])
    result = runner.invoke(app, [url], input=save_name_2 + '\n')
    assert result.exit_code == 0
    # assert result.stdout == url + '\n'
    assert url in result.stdout and save_name_2 in result.stdout

    result = runner.invoke(app, [url, save_name_1])
    assert result.exit_code == 0
    assert save_name_1 in result.stdout

    result = runner.invoke(app, [url, save_name_2])
    assert result.exit_code == 0
    assert save_name_2 in result.stdout

    result = runner.invoke(app, ['-v'])
    assert result.exit_code == 0
    assert result.stdout == f"version: {__version__}\n"

    result = runner.invoke(app, [], input=url_2 + "\n")
    assert result.exit_code == 0
    assert url_2 in result.stdout
