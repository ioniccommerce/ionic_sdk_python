<!-- Start SDK Example Usage -->
```python
import ionic

s = ionic.Ionic()


res = s.pets.create_pets()

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage -->