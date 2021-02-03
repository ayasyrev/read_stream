from typing import Optional

import typer

from read_stream import __version__
from read_stream.read_audio_stream import read_audio_stream


app = typer.Typer()


def print_version(version: bool):
    if version:
        typer.echo(f"version: {__version__}")
        raise typer.Exit()


@app.command()
def main(url: str = typer.Argument(None, help='Strem url'),
         save_name: Optional[str] = typer.Argument('stream'),
         version: Optional[bool] = typer.Option(None, '-v', '--version',
                                                help='Show version.', callback=print_version)
         ):
    if url is None:
        url = typer.prompt('Enter url')
    typer.echo(f"{url}")

    if save_name == 'stream':
        save_name = typer.prompt('Enter name for save', default=save_name)
    # save_name = '.'.join([save_name, 'opus'])
    typer.echo(f"url: {url}")
    typer.echo(f"save name: {save_name}")
    read_audio_stream(url=url, stream_name=save_name)


if __name__ == "__main__":
    app()
