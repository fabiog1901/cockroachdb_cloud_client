# cockroachdb_cloud_client

A client library for accessing CockroachDB Cloud API

## Usage

First, create a client:

```python
from cockroachdb_cloud_client import Client

client = Client(base_url="https://api.example.com")
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

```python
from cockroachdb_cloud_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://api.example.com", token="SuperSecretToken")
```

Now call your endpoint and use your models:

```python
from cockroachdb_cloud_client import AuthenticatedClient
from cockroachdb_cloud_client.models import ListClustersResponse
from cockroachdb_cloud_client.api.cockroach_cloud import cockroach_cloud_list_clusters
from cockroachdb_cloud_client.types import Response
from pprint import pprint
import json


client = AuthenticatedClient(base_url="https://cockroachlabs.cloud", token="CC-xxxx-yyyy-zzzz")

resp: Response[ListClustersResponse] = cockroach_cloud_list_clusters.sync_detailed(client=client)

pprint(json.loads(resp.content))
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken", 
    verify_ssl=False
)
```

Things to know:

1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `cockroachdb_cloud_client.api.default`
