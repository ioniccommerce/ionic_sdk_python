# Ionic SDK

## Overview

Ionic Commerce | Core API: Ionic Commerce API

### Available Operations

* [create_product_link](#create_product_link) - Ionic Commerce | Create Product Link
* [query](#query) - Product Search

## create_product_link

Creates and returns a tagged affiliate link

### Example Usage

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
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.ProductLinkRequest](../../models/components/productlinkrequest.md)               | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.CreateProductLinkSecurity](../../models/operations/createproductlinksecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[components.ProductLinkResponse](../../models/components/productlinkresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## query

API for searching for products & recommendations.

### Example Usage

```python
from ionic_api_sdk import Ionic
from ionic_api_sdk.models import operations

with Ionic() as ionic:
    res = ionic.query(security=operations.QuerySecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), request={
        "query": {
            "query": "<value>",
        },
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [components.QueryAPIRequest](../../models/components/queryapirequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `security`                                                               | [operations.QuerySecurity](../../models/operations/querysecurity.md)     | :heavy_check_mark:                                                       | The security requirements to use for the request.                        |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |

### Response

**[components.QueryAPIResponse](../../models/components/queryapiresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |