from read_stream.stream import AudioStream
from pathlib import Path


dir_to_save = Path('~/Downloads/audio_streams')


def read_audio_stream(url, stream_name):
    stream = AudioStream(url)
    if stream.audio_stream:
        print('audio stream availible')
        if dir_to_save.exists():
            stream.read_audio_stream(dir_to_save / stream_name)
        else:
            print(f"Error: no DATA dir: {dir_to_save}")
    else:
        print('NO audio stream.')
