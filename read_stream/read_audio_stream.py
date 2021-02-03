from read_stream.stream import AudioStream
from pathlib import Path


def read_audio_stream(url, stream_name):
    stream = AudioStream(url)
    if stream.audio_stream:
        print('audio stream availible')
        dir_to_save = Path('data')
        if dir_to_save.exists():
            stream.read_audio_stream('data/' + stream_name)
        else:
            print("Error: no DATA dir.")
    else:
        print('NO audio stream.')
