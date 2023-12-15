<!-- Start SDK Example Usage [usage] -->
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