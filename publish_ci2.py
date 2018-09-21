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
        print "Tarball environment var is missing : TARBALL"
        sys.exit(2)
    try:
        zenodo_token = os.environ['ZENODO_API_KEY']
    except KeyError:
        print "Please set the ZENODO_API_KEY environment variable"
        sys.exit(2)
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
    response = login_to_zenodo(zenodo_token)
    print response.json()


if __name__ == '__main__':
    main()
