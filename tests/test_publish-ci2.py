import pytest
import os
import json
import jmespath
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
    '''
    Generic tests of the correctness of the metadata file which will be sent
    to Zenodo after upload to describe the product.
    '''
    assert os.path.exists('metadata.json')
    with open('metadata.json') as metadata_file:
        metadata = json.load(metadata_file)
    access_right = jmespath.search('metadata.access_right', metadata)
    lic = jmespath.search('metadata.license', metadata)
    upload_type = jmespath.search('metadata.publication_type', metadata)
    communities = jmespath.search('metadata.communities[*].identifier', metadata)
    assert access_right == 'open'
    assert lic == 'Apache-2.0'
    assert upload_type == 'softwaredocumentation'
    assert 'code-rade' in communities


def test_login(monkeypatch):
    assert True