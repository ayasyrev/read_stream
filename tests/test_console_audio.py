import pytest
from typer.testing import CliRunner

from read_stream.console_audio import app

from read_stream import __version__

mock_result = {
        "audio_opus": "audio_stream",
        "720p": "video_stream",
    }


@pytest.fixture
def mock_streamlink_streams(mocker):
    mock = mocker.patch("streamlink.streams")
    mock.return_value = mock_result
    return mock


@pytest.fixture
def mock_read_audio_stream(mocker):
    mock = mocker.patch("read_stream.read_audio_stream.read_audio_stream")
    mock.return_value = mock_result
    return mock


def test_mock_streamlonk(mock_streamlink_streams):
    import streamlink
    stream_mocked = streamlink.streams('')
    print('Test stream mock')
    print(stream_mocked)
    assert stream_mocked.keys() == mock_result.keys()
    # assert stream == mock_result
    print(stream_mocked.keys())


def test_mock_read_audio(mock_read_audio_stream):
    from read_stream.read_audio_stream import read_audio_stream
    read_audio_stream_mocked = read_audio_stream('')
    print('Test read_audio mock')
    print(read_audio_stream_mocked)
    assert read_audio_stream_mocked.keys() == mock_result.keys()
    # assert stream == mock_result
    print(read_audio_stream_mocked.keys())


runner = CliRunner()


def test_main_invokes_streamlink_streams(mock_streamlink_streams):
    runner.invoke(app, ['fake_url', 'name'], input='\n')
    assert mock_streamlink_streams.called


def test_main_invokes_read_audio_stream(mock_read_audio_stream):
    runner.invoke(app, ['fake_url', 'name'], input='\n')
    assert mock_read_audio_stream.called


def test_app_use_url(mock_streamlink_streams):
    runner.invoke(app, ['fake_url', 'name'])
    args, _ = mock_streamlink_streams.call_args
    assert 'fake_url' in args


def test_app(mock_streamlink_streams):

    result = runner.invoke(app, ['-v'])
    assert result.exit_code == 0
    assert result.stdout == f"version: {__version__}\n"

    url = 'aaa'
    url_2 = 'bbb'
    save_name_1 = 'stream_1'
    save_name_2 = 'stream_2'

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

    result = runner.invoke(app, [], input=url_2 + "\n")
    assert result.exit_code == 0
    assert url_2 in result.stdout
