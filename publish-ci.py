
import requests
import json
import os

uri = 'https://zenodo.org/api/deposit/depositions'
access_token = os.environ['ZENODO_API_KEY']
headers = {"Content-Type": "application/json"}
# login
response = requests.get(uri,  params={'access_token': access_token })
# get env
# data will be sent as a parameter to the request
data = { 'filename': 'gmp-6.1.2-generic-sl6-x86_64.tar.gz' }
# TODO - load from file
metadata = {
          'metadata': {
          'upload_type': 'software',
          'publication_type': 'softwaredocumentation',
          'title': 'GMP build for CODE-RADE CI phase',
          'creators': [
            {
              'name': 'Bruce Becker',
              'affiliation': 'EGI Foundation',
              'orcid': '0000-0002-6607-7145'
            }
          ],
          'description': 'See the README',
          'access_right': 'open',
          'license': 'Apache-2.0',
          'prereserve_doi': 'true',
          'communities': 'code-rade'
        }
      }

# check if json is present
if os.path.isfile('zenodo.json'):
  print("file is there")
  # Check that DOI has been registered and that url is valid
  with open('zenodo.json') as deposition:
    zenodo = json.load(deposition)
  id = zenodo['id']
  print 'id is ',id
  # Check that this is the right ID
else:
  # deposit the file
  print("no deposition yet")
  # create deposition
  create = requests.post(uri, params={'access_token': access_token}, json={}, headers=headers)
  create.json()
  with open('zenodo.json', 'w') as deposition:
    json.dump(create.json(), deposition)
  id = create.json['id']


# files is an array of files to be sent as parameters to the request
files = {'file': open('/tmp/gmp-6.1.2-generic-sl6-x86_64.tar.gz', 'rb')}
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
