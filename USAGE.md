<!-- Start SDK Example Usage [usage] -->
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
<!-- End SDK Example Usage [usage] -->