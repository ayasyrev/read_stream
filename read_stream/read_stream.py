from read_stream.stream import Stream
from pathlib import Path


dir_to_save = Path.home() / 'Downloads' / 'streams'
DEFAULT_QUALITY = 'best'
VIDEO_EXT = 'mp4'


def read_stream(url, name_to_save, quality=DEFAULT_QUALITY):
    stream = Stream(url)
    if quality in stream.streams:
        if dir_to_save.exists():
            print(f'loading {quality} stream to {dir_to_save}.')
            name_to_save = dir_to_save / (name_to_save + '.' + VIDEO_EXT)
            print(f"name to save: {name_to_save}")
            stream.read_stream(stream_name=quality, fn=name_to_save)
        else:
            print(f"Error: no DATA dir: {dir_to_save}")
    else:
        print(f'NO {quality} stream.')
