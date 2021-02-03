from read_stream.stream import AudioStream


def read_audio_stream(url, stream_name):
    stream = AudioStream(url)
    if stream.audio_stream:
        print('audio stream availible')
        stream.read_audio_stream('data/' + stream_name)
    else:
        print('NO audio stream.')
