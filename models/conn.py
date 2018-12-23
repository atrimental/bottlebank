import logging
import sys
from google.cloud import datastore

# Following https://code.luasoftware.com/tutorials/google-app-engine/using-datastore-in-app-engine-standard-python37/

IS_DEV = "__DEV__" in sys.argv or __debug__

if IS_DEV:
    import mock
    import google.auth.credentials
    # https://github.com/GoogleCloudPlatform/google-cloud-python/blob/master/datastore/tests/unit/test_client.py
    credentials = mock.Mock(spec=google.auth.credentials.Credentials)
    client = datastore.Client(credentials=credentials) # , _use_grpc=False

    logging.basicConfig(level=logging.INFO)
else:
    client = datastore.Client()