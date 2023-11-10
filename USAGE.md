<!-- Start SDK Example Usage -->
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
<!-- End SDK Example Usage -->