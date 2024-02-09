# Ionic SDK


## Overview

Ionic Commerce | API: Ionic Commerce API

### Available Operations

* [query](#query) - Product Search

## query

API for searching for products & recommendations.

### Example Usage

```python
import ionic
from ionic.models import components, operations

s = ionic.Ionic()

req = components.QueryAPIRequest(
    query=components.Query(
        query='string',
    ),
    messages=[
        components.Message(
            content='string',
            role=components.MessageRole.SYSTEM,
            type=components.MessageType.TAG,
        ),
    ],
    session=components.Session(),
)

res = s.query(req, operations.QuerySecurity(
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
| errors.SDKError            | 4x-5xx                     | */*                        |
