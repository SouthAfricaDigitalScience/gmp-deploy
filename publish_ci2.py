import sys
import requests
# import json
# import hashlib
import os


def setup():
    '''
    Checks that environment variables are set and if not, aborts
    '''
    try:
        data = {'filename': os.environ['TARBALL']}
    except KeyError:
        print "please set TARBALL environment variable to the file you \
want to upload"
        sys.exit(1)
    try:
        assert(os.environ['TARBALL'] is not None)
    except ValueError:
        sys.exit(1)
    try:
        zenodo_token = os.environ['ZENODO_API_KEY']
    except KeyError:
        sys.exit(1)
    try:
        assert(zenodo_token is not None)
    except ValueError:
        sys.exit(1)
    return zenodo_token, data


def login_to_zenodo(token):
    return requests.get(uri, params={'access_token': token})


def main():
    '''
    The main function that does everything
    '''
    global uri
    global headers
    uri = 'https://zenodo.org/api/deposit/depositions'
    headers = {"Content-Type": "application/json"}

    zenodo_token, data = setup()
    # files = {'file': open(os.environ['TARBALL'], 'rb')}
    print uri
    # response = login_to_zenodo(zenodo_token)


if __name__ == '__main__':
    main()
