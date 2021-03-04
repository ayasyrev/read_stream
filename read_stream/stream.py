import streamlink
from pathlib import PosixPath
from tqdm import tqdm

DEFAULT_AUDIO = 'audio_opus'


class Stream:
    """Base class - open Stream
    """
    def __init__(self, url: str) -> None:
        self.url = url
        self.streams = None
        # self.audio_stream = None
        # self.audio_extension = None
        try:
            self._streams = streamlink.streams(url)
            self.streams = self._streams.keys()
        except Exception as error:
            print('Error read Url', error)
            raise RuntimeError(error)

    def read_stream(self, stream_name, fn: PosixPath):
        stream = self._streams[stream_name]
        with stream.open() as fd:
            with open(fn, 'wb') as file:
                total = 100
                pbar = tqdm(total=total)
                data_loaded = 0
                while True:
                    data = fd.read(1024)    # raise IOError("Read timeout")
                    if data:
                        file.write(data)
                        data_loaded += 1
                        if data_loaded % 1024 == 0:
                            pbar.update(1)
                            pbar.set_description(f"loaded: {data_loaded // 1024}Mb")
                            if data_loaded // 1024 == total - 1:
                                total += 100
                                pbar.total = total
                    else:
                        break
        file_size = fn.stat().st_size
        print(f"loaded file: {fn}, size: {file_size // 1024 // 1024}Mb")

    def __repr__(self) -> str:
        return f"Streams: {', '.join(self.streams)}"


class AudioStream(Stream):
    def __init__(self, url: str) -> None:
        super().__init__(url)
        self.audio_stream = None
        self.audio_extension = None

        if self.streams:
            self.audio_streams = [stream for stream in self.streams if stream.startswith('audio')]
            if len(self.audio_streams) > 0:
                self.audio_stream = DEFAULT_AUDIO if DEFAULT_AUDIO in self.audio_streams else self.audio_streams[0]
                self.audio_extension = self.audio_stream.split('_')[-1]

    def read_audio_stream(self, name_to_save: PosixPath):
        if self.audio_stream:
            print(self.audio_stream)
            name_to_save = name_to_save.parent / (name_to_save.name + '.' + self.audio_extension)
            print('Loading audio stream to ', name_to_save)
            self.read_stream(self.audio_stream, name_to_save)
        else:
            raise RuntimeError('audio stream unavailible')

    def __repr__(self) -> str:
        return f"Audio streams: {', '.join(list[self.audio_streams])}"
