import requests
import json
import os

uri = 'https://zenodo.org/api/deposit/depositions'
access_token = os.environ['ZENODO_API_KEY']
headers = {"Content-Type": "application/json"}
# login
response = requests.get(uri,  params={'access_token': access_token })
# data will be sent as a parameter to the request
data = { 'filename': os.environ['TARBALL'] }
with open('metadata.json') as metadata_file:
    metadata = json.load(metadata_file)
print os.environ['BUILD_NUMBER']
# check if json is present
if os.path.isfile('zenodo.json'):
  print("file is there")
  # Check that DOI has been registered and that url is valid
  with open('zenodo.json') as deposition:
    zenodo = json.load(deposition)
  id = zenodo['id']
  print 'id is ',id
  # Check that this is the right ID
  # compare md5sums
  print 
  # replace it with a new version
else:
  # deposit the file
  print("no deposition yet")
  # create deposition
  create = requests.post(uri, params={'access_token': access_token}, json={}, headers=headers)
  create.json()
  print create.json()
  id = create.json()['id']
  with open('zenodo.json', 'w') as deposition:
    json.dump(create.json(), deposition)
  

# files is an array of files to be sent as parameters to the request
files = {'file': open(os.environ['TARBALL'], 'rb')}
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
print(meta.json())
