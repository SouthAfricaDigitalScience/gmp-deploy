import pytest
import os
import json
import publish_ci2 as p
try:
    import mock
except ImportError:
    from unittest import mock


@mock.patch.dict(os.environ, {'TARBALL': '', 'ZENODO_API_KEY': ''})
def test_setup_empty_env():
    with pytest.raises(Exception) as empty_vars:
        token, data = p.setup()
        print empty_vars


@mock.patch.dict(os.environ, {
                    'TARBALL': 'tarball.tar.gz',
                    'ZENODO_API_KEY': '101010101'})
def test_setup_fake_env():
    zenodo_key, data = p.setup()
    assert zenodo_key == "101010101"
    assert data == {'filename': 'tarball.tar.gz'}


def test_setup_no_tarball(monkeypatch):
    monkeypatch.delenv('TARBALL', raising=True)
    with pytest.raises(SystemExit) as e:
        p.setup()
    assert e.type == SystemExit
    assert e.value.code == 2

def test_setup_no_zenodo(monkeypatch):
    monkeypatch.delenv('ZENODO_API_KEY', raising=True)
    with pytest.raises(SystemExit) as e:
        p.setup()
    assert e.type == SystemExit
    assert e.value.code == 2
    


def test_metadata():
    assert os.path.exists('metadata.json')
    with open('metadata.json') as metadata_file:
        metadata = json.load(metadata_file)
    assert metadata
