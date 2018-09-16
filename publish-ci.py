import requests
import json
import hashlib
import os

uri = 'https://zenodo.org/api/deposit/depositions'
access_token = os.environ['ZENODO_API_KEY']
headers = {"Content-Type": "application/json"}
# login
response = requests.get(uri,  params={'access_token': access_token})
# data will be sent in the headers with the request
data = {'filename': os.environ['TARBALL']}
# files is an array of files to be sent as parameters to the request
files = {'file': open(os.environ['TARBALL'], 'rb')}


with open('metadata.json') as metadata_file:
    metadata = json.load(metadata_file)

# If the project has already been published, we should check if anything has
# changed and if so, update the project
# If the project not yet been published, then create a deposition for it.
if os.path.isfile('zenodo.json'):
    print("This build has been published before")
    with open('zenodo.json') as deposition:
        zenodo = json.load(deposition)
    id = zenodo['id']
    print 'id is ', id
    # get the files path
    files_url = zenodo['links']['files']
    print files_url
    published_checksum =  requests.get(
                            files_url,
                            params={'access_token': access_token}).json()[0]['checksum']
    checksum = hashlib.md5(open(os.environ['TARBALL'], 'rb').read()).hexdigest()
    # assert checksum == published_checksum
    if (checksum == published_checksum):
        print "no need to publish this, the file is the same"
    else:
        print "we need to update the file"
else:
    # The project has not yet been published
    # deposit the file
    print("no deposition yet")
    # create deposition and write the publication
    create = requests.post(uri,
                           params={'access_token': access_token},
                           json={},
                           headers=headers)
    id = create.json()['id']
    deposit = requests.post(uri + '/%s/files' % id,
                            params={'access_token': access_token},
                            data=data,
                            files=files)
    print(deposit.json())

    # update with metadata
    meta = requests.put(uri + '/%s' % id,
                        params={'access_token': access_token},
                        data=json.dumps(metadata),
                        headers=headers)
    with open('zenodo.json', 'w') as deposition:
        json.dump(create.json(), deposition)
