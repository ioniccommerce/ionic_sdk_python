# IonicAPI SDK


## Overview

Ionic Shopping API: Product Search & Recommendation API

### Available Operations

* [query](#query) - Multi-Query Product Search.

## query

API for searching for products & recommendations. Accepts multiple query objects.

### Example Usage

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

res = s.query(req)

if res.query_api_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [components.QueryAPIRequest](../../models/components/queryapirequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.QueryResponse](../../models/operations/queryresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |
