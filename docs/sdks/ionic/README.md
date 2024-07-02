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
import ionic
from ionic.models import components, operations

s = ionic.Ionic()


res = s.create_product_link(request=components.ProductLinkRequest(
    client_details=components.ClientDetails(
        ip='185.113.33.24',
    ),
    product=components.ProductDetails(
        identifiers=components.ProductIdentifiers(),
        link='http://negative-wording.biz',
    ),
    query=components.QueryDetails(
        q='<value>',
    ),
    user_details=components.UserDetails(
        email='Mitchell_DAmore49@hotmail.com',
        id='<id>',
    ),
), security=operations.CreateProductLinkSecurity(
    api_key_header="<YOUR_API_KEY_HERE>",
))

if res.product_link_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.ProductLinkRequest](../../models/components/productlinkrequest.md)               | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.CreateProductLinkSecurity](../../models/operations/createproductlinksecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.CreateProductLinkResponse](../../models/operations/createproductlinkresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## query

API for searching for products & recommendations.

### Example Usage

```python
import ionic
from ionic.models import components, operations

s = ionic.Ionic()


res = s.query(request=components.QueryAPIRequest(
    query=components.Query(
        query='<value>',
    ),
), security=operations.QuerySecurity(
    api_key_header="<YOUR_API_KEY_HERE>",
))

if res.query_api_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [components.QueryAPIRequest](../../models/components/queryapirequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `security`                                                               | [operations.QuerySecurity](../../models/operations/querysecurity.md)     | :heavy_check_mark:                                                       | The security requirements to use for the request.                        |


### Response

**[operations.QueryResponse](../../models/operations/queryresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |
