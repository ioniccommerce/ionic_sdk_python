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
        "ip": "185.113.33.24",
    },
    "product": {
        "identifiers": {},
        "link": "http://negative-wording.biz",
    },
    "query": {
        "q": "<value>",
    },
    "user_details": {
        "email": "Mitchell_DAmore49@hotmail.com",
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
            "ip": "77.243.224.51",
        },
        "product": {
            "identifiers": {},
            "link": "http://grumpy-bird.net",
        },
        "query": {
            "q": "<value>",
        },
        "user_details": {
            "email": "Lorena67@gmail.com",
            "id": "<id>",
        },
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->