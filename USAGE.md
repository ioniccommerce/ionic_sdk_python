<!-- Start SDK Example Usage -->
```python
import ionic
from ionic.models import components

s = ionic.Ionic()

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
<!-- End SDK Example Usage -->