<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from ionic_api_sdk import Ionic
from ionic_api_sdk.models import operations

s = Ionic()

res = s.create_product_link(security=operations.CreateProductLinkSecurity(
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from ionic_api_sdk import Ionic
from ionic_api_sdk.models import operations

async def main():
    s = Ionic()
    res = await s.create_product_link_async(security=operations.CreateProductLinkSecurity(
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

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->