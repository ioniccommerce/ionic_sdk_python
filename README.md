# Ionic-SDK-Python

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/ioniccommerce/ionic_sdk_python/actions"><img src="https://img.shields.io/github/actions/workflow/status/ioniccommerce/ionic_sdk_python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install Ionic-API-SDK
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import ionic
from ionic.models import components, operations

s = ionic.Ionic()

req = components.QueryAPIRequest(
    messages=[
        components.Message(
            content='string',
            role=components.MessageRole.SYSTEM,
            type=components.MessageType.TAG,
        ),
    ],
    queries=[
        components.Query(
            query='string',
        ),
    ],
    session=components.Session(
        locale='zu_ZA',
        session_id='string',
        user_id='string',
    ),
)

res = s.query(req, operations.QuerySecurity(
    api_key_header="<YOUR_API_KEY_HERE>",
))

if res.query_api_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [Ionic SDK](docs/sdks/ionic/README.md)

* [query](docs/sdks/ionic/README.md#query) - Multi-Query Product Search.
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4x-5xx                     | */*                        |

### Example

```python
import ionic
from ionic.models import components, operations

s = ionic.Ionic()

req = components.QueryAPIRequest(
    messages=[
        components.Message(
            content='string',
            role=components.MessageRole.SYSTEM,
            type=components.MessageType.TAG,
        ),
    ],
    queries=[
        components.Query(
            query='string',
        ),
    ],
    session=components.Session(
        locale='zu_ZA',
        session_id='string',
        user_id='string',
    ),
)

res = None
try:
    res = s.query(req, operations.QuerySecurity(
    api_key_header="<YOUR_API_KEY_HERE>",
))
except errors.HTTPValidationError as e:
    print(e)  # handle exception
    raise(e)
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.query_api_response is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.ionicapi.com` | None |

#### Example

```python
import ionic
from ionic.models import components, operations

s = ionic.Ionic(
    server_idx=0,
)

req = components.QueryAPIRequest(
    messages=[
        components.Message(
            content='string',
            role=components.MessageRole.SYSTEM,
            type=components.MessageType.TAG,
        ),
    ],
    queries=[
        components.Query(
            query='string',
        ),
    ],
    session=components.Session(
        locale='zu_ZA',
        session_id='string',
        user_id='string',
    ),
)

res = s.query(req, operations.QuerySecurity(
    api_key_header="<YOUR_API_KEY_HERE>",
))

if res.query_api_response is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import ionic
from ionic.models import components, operations

s = ionic.Ionic(
    server_url="https://api.ionicapi.com",
)

req = components.QueryAPIRequest(
    messages=[
        components.Message(
            content='string',
            role=components.MessageRole.SYSTEM,
            type=components.MessageType.TAG,
        ),
    ],
    queries=[
        components.Query(
            query='string',
        ),
    ],
    session=components.Session(
        locale='zu_ZA',
        session_id='string',
        user_id='string',
    ),
)

res = s.query(req, operations.QuerySecurity(
    api_key_header="<YOUR_API_KEY_HERE>",
))

if res.query_api_response is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import ionic
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = ionic.Ionic(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name             | Type             | Scheme           |
| ---------------- | ---------------- | ---------------- |
| `api_key_header` | apiKey           | API key          |

To authenticate with the API the `api_key_header` parameter must be set when initializing the SDK client instance. For example:


### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import ionic
from ionic.models import components, operations

s = ionic.Ionic()

req = components.QueryAPIRequest(
    messages=[
        components.Message(
            content='string',
            role=components.MessageRole.SYSTEM,
            type=components.MessageType.TAG,
        ),
    ],
    queries=[
        components.Query(
            query='string',
        ),
    ],
    session=components.Session(
        locale='zu_ZA',
        session_id='string',
        user_id='string',
    ),
)

res = s.query(req, operations.QuerySecurity(
    api_key_header="<YOUR_API_KEY_HERE>",
))

if res.query_api_response is not None:
    # handle response
    pass
```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
