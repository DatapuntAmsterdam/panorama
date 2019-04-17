import os

# OBJECT_STORE SETTINGS

RUNNING_OS_INTERNALLY = bool(os.getenv('RUNNING_OS_INTERNALLY', False))

OBJECTSTORE_USER = os.getenv('OBJECTSTORE_USER', 'panorama')
OBJECTSTORE_PASSWORD = os.getenv('OBJECTSTORE_PASSWORD', 'insecure')

AUTH_VERSION = '2.0'
AUTHURL = 'https://identity.stack.cloudvps.com/v2.0'

DATAPUNT_TENANT_NAME = 'BGE000081 Datapunt'
DATAPUNT_TENANT_ID = 'ffb7a5a57dd34cc49436abc510cad162'
PANORAMA_TENANT_NAME = 'BGE000081 Panorama'
PANORAMA_TENANT_ID = '3206eec333a04cc980799f75a593505a'

#   wait for new years to be uploaded:
PANORAMA_CONTAINERS = ['2016', '2017', '2018', '2019']

DATAPUNT_CONTAINER = 'panorama'

REGION_NAME = 'NL'
