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
        assert(os.environ['TARBALL'] is not None)
    except Exception as tarball_missing:
        print data
        print tarball_missing
        sys.exit(1)
    try:
        zenodo_token = os.environ['ZENODO_API_KEY']
        assert(zenodo_token is not None)
    except Exception as zenodo_token_missing:
        print zenodo_token_missing
        sys.exit(1)

    return zenodo_token, data


def login_to_zenodo(token):
    return requests.get(uri, params={'access_token': access_token})


def main():
    zenodo_token, data = setup()
    response = login_to_zenodo(zenodo_token)



if __name__ == '__main__':
    main()
