# Ionic Python SDK

## Setup

## Dev

## Run

## Test

## Deploy (Publish)

https://python-poetry.org/docs/libraries/

bump version in `pyproject.toml`

`poetry publish --build` (or do it separately)

<!-- No SDK Installation -->
<!-- No SDK Example Usage -->
<!-- No SDK Available Operations -->


<!-- Start Error Handling -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

### Example

```python
import ionic_api
from ionic_api.models import components

s = ionic_api.IonicAPI()

req = components.QueryAPIRequest(
    queries=[
        components.Query(
            query='string',
        ),
    ],
)

res = None
try:
    res = s.query(req)
except (errors.HTTPValidationError) as e:
    print(e) # handle exception

except (errors.SDKError) as e:
    print(e) # handle exception


if res.query_api_response is not None:
    # handle response
    pass
```

<!-- End Error Handling -->



<!-- Start Server Selection -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.ionicapi.com` | None |

#### Example

```python
import ionic_api
from ionic_api.models import components

s = ionic_api.IonicAPI(
    server_idx=0,
)

req = components.QueryAPIRequest(
    queries=[
        components.Query(
            query='string',
        ),
    ],
)

res = s.query(req)

if res.query_api_response is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import ionic_api
from ionic_api.models import components

s = ionic_api.IonicAPI(
    server_url="https://api.ionicapi.com",
)

req = components.QueryAPIRequest(
    queries=[
        components.Query(
            query='string',
        ),
    ],
)

res = s.query(req)

if res.query_api_response is not None:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import ionic_api
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = ionic_api.IonicAPI(client: http_client)
```
<!-- End Custom HTTP Client -->

<!-- Placeholder for Future Speakeasy SDK Sections -->


