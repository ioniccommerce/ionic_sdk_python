# Pets
(*pets*)

### Available Operations

* [create_pets](#create_pets) - Create a pet
* [list_pets](#list_pets) - List all pets
* [show_pet_by_id](#show_pet_by_id) - Info for a specific pet

## create_pets

Create a pet

### Example Usage

```python
import ionic

s = ionic.Ionic()


res = s.pets.create_pets()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.CreatePetsResponse](../../models/operations/createpetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_pets

List all pets

### Example Usage

```python
import ionic
from ionic.models import operations

s = ionic.Ionic()


res = s.pets.list_pets(limit=21453)

if res.pets is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                      | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `limit`                                        | *Optional[int]*                                | :heavy_minus_sign:                             | How many items to return at one time (max 100) |


### Response

**[operations.ListPetsResponse](../../models/operations/listpetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## show_pet_by_id

Info for a specific pet

### Example Usage

```python
import ionic
from ionic.models import operations

s = ionic.Ionic()


res = s.pets.show_pet_by_id(pet_id='string')

if res.pet is not None:
    # handle response
    pass
```

### Parameters

| Parameter                     | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `pet_id`                      | *str*                         | :heavy_check_mark:            | The id of the pet to retrieve |


### Response

**[operations.ShowPetByIDResponse](../../models/operations/showpetbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
