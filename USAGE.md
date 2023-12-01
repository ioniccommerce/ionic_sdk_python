<!-- Start SDK Example Usage [usage] -->
```python
import ionic
from ionic.models import components, operations

s = ionic.Ionic()

req = components.QueryAPIRequest(
    queries=[
        components.Query(
            query='string',
        ),
    ],
)

res = s.query(req, operations.QuerySecurity(
    api_key_header="",
))

if res.query_api_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->