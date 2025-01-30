# Ionic-SDK-Python

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/ioniccommerce/ionic_sdk_python/actions"><img src="https://img.shields.io/github/actions/workflow/status/ioniccommerce/ionic_sdk_python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>

<!-- Start Summary [summary] -->
## Summary

Ionic Commerce | Core API: Ionic Commerce API
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [Ionic-SDK-Python](#ionic-sdk-python)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Authentication](#authentication)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install Ionic-API-SDK
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add Ionic-API-SDK
```
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from ionic_api_sdk import Ionic
from ionic_api_sdk.models import operations

with Ionic() as ionic:

    res = ionic.create_product_link(security=operations.CreateProductLinkSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), request={
        "client_details": {
            "ip": "2aff:3f6d:613d:ecab:e464:1568:83ab:a3e3",
        },
        "product": {
            "identifiers": {},
            "link": "https://gentle-hello.name/",
        },
        "query": {
            "q": "<value>",
        },
        "user_details": {
            "email": "Vivian.Waters87@gmail.com",
            "id": "<id>",
        },
        "log_only": False,
    })

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from ionic_api_sdk import Ionic
from ionic_api_sdk.models import operations

async def main():
    async with Ionic() as ionic:

        res = await ionic.create_product_link_async(security=operations.CreateProductLinkSecurity(
            api_key_header="<YOUR_API_KEY_HERE>",
        ), request={
            "client_details": {
                "ip": "2aff:3f6d:613d:ecab:e464:1568:83ab:a3e3",
            },
            "product": {
                "identifiers": {},
                "link": "https://gentle-hello.name/",
            },
            "query": {
                "q": "<value>",
            },
            "user_details": {
                "email": "Vivian.Waters87@gmail.com",
                "id": "<id>",
            },
            "log_only": False,
        })

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Ionic SDK](docs/sdks/ionic/README.md)

* [create_product_link](docs/sdks/ionic/README.md#create_product_link) - Ionic Commerce | Create Product Link
* [query](docs/sdks/ionic/README.md#query) - Product Search

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from ionic_api_sdk import Ionic
from ionic_api_sdk.models import operations
from ionic_api_sdk.utils import BackoffStrategy, RetryConfig

with Ionic() as ionic:

    res = ionic.create_product_link(security=operations.CreateProductLinkSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), request={
        "client_details": {
            "ip": "2aff:3f6d:613d:ecab:e464:1568:83ab:a3e3",
        },
        "product": {
            "identifiers": {},
            "link": "https://gentle-hello.name/",
        },
        "query": {
            "q": "<value>",
        },
        "user_details": {
            "email": "Vivian.Waters87@gmail.com",
            "id": "<id>",
        },
        "log_only": False,
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res is not None

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from ionic_api_sdk import Ionic
from ionic_api_sdk.models import operations
from ionic_api_sdk.utils import BackoffStrategy, RetryConfig

with Ionic(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
) as ionic:

    res = ionic.create_product_link(security=operations.CreateProductLinkSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), request={
        "client_details": {
            "ip": "2aff:3f6d:613d:ecab:e464:1568:83ab:a3e3",
        },
        "product": {
            "identifiers": {},
            "link": "https://gentle-hello.name/",
        },
        "query": {
            "q": "<value>",
        },
        "user_details": {
            "email": "Vivian.Waters87@gmail.com",
            "id": "<id>",
        },
        "log_only": False,
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `create_product_link_async` method may raise the following exceptions:

| Error Type                 | Status Code | Content Type     |
| -------------------------- | ----------- | ---------------- |
| errors.HTTPValidationError | 422         | application/json |
| errors.SDKError            | 4XX, 5XX    | \*/\*            |

### Example

```python
from ionic_api_sdk import Ionic
from ionic_api_sdk.models import errors, operations

with Ionic() as ionic:
    res = None
    try:

        res = ionic.create_product_link(security=operations.CreateProductLinkSecurity(
            api_key_header="<YOUR_API_KEY_HERE>",
        ), request={
            "client_details": {
                "ip": "2aff:3f6d:613d:ecab:e464:1568:83ab:a3e3",
            },
            "product": {
                "identifiers": {},
                "link": "https://gentle-hello.name/",
            },
            "query": {
                "q": "<value>",
            },
            "user_details": {
                "email": "Vivian.Waters87@gmail.com",
                "id": "<id>",
            },
            "log_only": False,
        })

        assert res is not None

        # Handle response
        print(res)

    except errors.HTTPValidationError as e:
        # handle e.data: errors.HTTPValidationErrorData
        raise(e)
    except errors.SDKError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from ionic_api_sdk import Ionic
from ionic_api_sdk.models import operations

with Ionic(
    server_url="https://api.ioniccommerce.com",
) as ionic:

    res = ionic.create_product_link(security=operations.CreateProductLinkSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), request={
        "client_details": {
            "ip": "2aff:3f6d:613d:ecab:e464:1568:83ab:a3e3",
        },
        "product": {
            "identifiers": {},
            "link": "https://gentle-hello.name/",
        },
        "query": {
            "q": "<value>",
        },
        "user_details": {
            "email": "Vivian.Waters87@gmail.com",
            "id": "<id>",
        },
        "log_only": False,
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from ionic_api_sdk import Ionic
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Ionic(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from ionic_api_sdk import Ionic
from ionic_api_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Ionic(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name             | Type   | Scheme  |
| ---------------- | ------ | ------- |
| `api_key_header` | apiKey | API key |

To authenticate with the API the `api_key_header` parameter must be set when initializing the SDK client instance. For example:


### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
from ionic_api_sdk import Ionic
from ionic_api_sdk.models import operations

with Ionic() as ionic:

    res = ionic.create_product_link(security=operations.CreateProductLinkSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), request={
        "client_details": {
            "ip": "2aff:3f6d:613d:ecab:e464:1568:83ab:a3e3",
        },
        "product": {
            "identifiers": {},
            "link": "https://gentle-hello.name/",
        },
        "query": {
            "q": "<value>",
        },
        "user_details": {
            "email": "Vivian.Waters87@gmail.com",
            "id": "<id>",
        },
        "log_only": False,
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Ionic` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from ionic_api_sdk import Ionic
def main():
    with Ionic() as ionic:
        # Rest of application here...


# Or when using async:
async def amain():
    async with Ionic() as ionic:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from ionic_api_sdk import Ionic
import logging

logging.basicConfig(level=logging.DEBUG)
s = Ionic(debug_logger=logging.getLogger("ionic_api_sdk"))
```
<!-- End Debugging [debug] -->

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
