# metafab_python.ItemsApi

All URIs are relative to *https://api.trymetafab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_mint_collection_items**](ItemsApi.md#batch_mint_collection_items) | **POST** /v1/collections/{collectionId}/batchMints | Batch mint collection items
[**batch_transfer_collection_items**](ItemsApi.md#batch_transfer_collection_items) | **POST** /v1/collections/{collectionId}/batchTransfers | Batch transfer collection items
[**burn_collection_item**](ItemsApi.md#burn_collection_item) | **POST** /v1/collections/{collectionId}/items/{collectionItemId}/burns | Burn collection item
[**create_collection**](ItemsApi.md#create_collection) | **POST** /v1/collections | Create collection
[**create_collection_item**](ItemsApi.md#create_collection_item) | **POST** /v1/collections/{collectionId}/items | Create collection item
[**get_collection_approval**](ItemsApi.md#get_collection_approval) | **GET** /v1/collections/{collectionId}/approvals | Get collection approval
[**get_collection_item**](ItemsApi.md#get_collection_item) | **GET** /v1/collections/{collectionId}/items/{collectionItemId} | Get collection item
[**get_collection_item_balance**](ItemsApi.md#get_collection_item_balance) | **GET** /v1/collections/{collectionId}/items/{collectionItemId}/balances | Get collection item balance
[**get_collection_item_balances**](ItemsApi.md#get_collection_item_balances) | **GET** /v1/collections/{collectionId}/balances | Get collection item balances
[**get_collection_item_supplies**](ItemsApi.md#get_collection_item_supplies) | **GET** /v1/collections/{collectionId}/supplies | Get collection item supplies
[**get_collection_item_supply**](ItemsApi.md#get_collection_item_supply) | **GET** /v1/collections/{collectionId}/items/{collectionItemId}/supplies | Get collection item supply
[**get_collection_item_timelock**](ItemsApi.md#get_collection_item_timelock) | **GET** /v1/collections/{collectionId}/items/{collectionItemId}/timelocks | Get collection item timelock
[**get_collection_items**](ItemsApi.md#get_collection_items) | **GET** /v1/collections/{collectionId}/items | Get collection items
[**get_collections**](ItemsApi.md#get_collections) | **GET** /v1/collections | Get collections
[**mint_collection_item**](ItemsApi.md#mint_collection_item) | **POST** /v1/collections/{collectionId}/items/{collectionItemId}/mints | Mint collection item
[**set_collection_approval**](ItemsApi.md#set_collection_approval) | **POST** /v1/collections/{collectionId}/approvals | Set collection approval
[**set_collection_item_timelock**](ItemsApi.md#set_collection_item_timelock) | **POST** /v1/collections/{collectionId}/items/{collectionItemId}/timelocks | Set collection item timelock
[**transfer_collection_item**](ItemsApi.md#transfer_collection_item) | **POST** /v1/collections/{collectionId}/items/{collectionItemId}/transfers | Transfer collection item


# **batch_mint_collection_items**
> TransactionModel batch_mint_collection_items(collection_id, x_authorization, x_password, batch_mint_collection_items_request)

Batch mint collection items

Creates (mints) the provided itemIds of the specified quantities to the provided wallet address or wallet address associated with the provided walletId.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.batch_mint_collection_items_request import BatchMintCollectionItemsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    batch_mint_collection_items_request = BatchMintCollectionItemsRequest(
        address="address_example",
        item_ids=[
            3.14,
        ],
        quantities=[
            3.14,
        ],
        wallet_id="wallet_id_example",
    ) # BatchMintCollectionItemsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Batch mint collection items
        api_response = api_instance.batch_mint_collection_items(collection_id, x_authorization, x_password, batch_mint_collection_items_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->batch_mint_collection_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_password** | **str**| The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **batch_mint_collection_items_request** | [**BatchMintCollectionItemsRequest**](BatchMintCollectionItemsRequest.md)|  |

### Return type

[**TransactionModel**](TransactionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created (minted) the provided items of the provided quantities to the provided wallet address or wallet address of the provided walletId. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_transfer_collection_items**
> TransactionModel batch_transfer_collection_items(collection_id, x_authorization, x_password, batch_transfer_collection_items_request)

Batch transfer collection items

Transfers one or multiple items of specified quantities to the provided wallet addresses or wallet addresses associated with the provided walletIds. You may also provide a combination of addresses and walletIds in one request.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.batch_transfer_collection_items_request import BatchTransferCollectionItemsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.
    x_authorization = "["game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP","player_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP"]" # str | The `secretKey` of a specific game or the `accessToken` of a specific player.
    x_password = "mySecurePassword" # str | The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet.
    batch_transfer_collection_items_request = BatchTransferCollectionItemsRequest(
        addresses=[
            "addresses_example",
        ],
        wallet_ids=[
            "wallet_ids_example",
        ],
        item_ids=[
            12,
        ],
        quantities=[
            1,
        ],
    ) # BatchTransferCollectionItemsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Batch transfer collection items
        api_response = api_instance.batch_transfer_collection_items(collection_id, x_authorization, x_password, batch_transfer_collection_items_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->batch_transfer_collection_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of a specific game or the &#x60;accessToken&#x60; of a specific player. |
 **x_password** | **str**| The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet. |
 **batch_transfer_collection_items_request** | [**BatchTransferCollectionItemsRequest**](BatchTransferCollectionItemsRequest.md)|  |

### Return type

[**TransactionModel**](TransactionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully transferred the itemIds of the provided quantities to each of the provided wallet addresses and/or wallet addresses of the provided walletIds. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **burn_collection_item**
> TransactionModel burn_collection_item(collection_id, collection_item_id, x_authorization, x_password, burn_collection_item_request)

Burn collection item

Removes (burns) the provided quantity of the collectionItemId from the authenticating game or players wallet. The quantity is permanently removed from the circulating supply of the item.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from metafab_python.model.burn_collection_item_request import BurnCollectionItemRequest
from metafab_python.model.transaction_model import TransactionModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.
    collection_item_id = 3.14 # float | Any item id for the collection. Zero, or a positive integer.
    x_authorization = "["game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP","player_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP"]" # str | The `secretKey` of a specific game or the `accessToken` of a specific player.
    x_password = "mySecurePassword" # str | The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet.
    burn_collection_item_request = BurnCollectionItemRequest(
        quantity=3.14,
    ) # BurnCollectionItemRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Burn collection item
        api_response = api_instance.burn_collection_item(collection_id, collection_item_id, x_authorization, x_password, burn_collection_item_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->burn_collection_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |
 **collection_item_id** | **float**| Any item id for the collection. Zero, or a positive integer. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of a specific game or the &#x60;accessToken&#x60; of a specific player. |
 **x_password** | **str**| The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet. |
 **burn_collection_item_request** | [**BurnCollectionItemRequest**](BurnCollectionItemRequest.md)|  |

### Return type

[**TransactionModel**](TransactionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully removed (burned) the quantity of the collectionItemId from the authenticating game or player&#39;s wallet. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_collection**
> CreateCollection200Response create_collection(x_authorization, x_password, create_collection_request)

Create collection

Creates a new game item collection and deploys an extended functionality ERC1155 contract on behalf of the authenticating game's primary wallet. The deployed ERC1155 contract is preconfigured to fully support creating unique item types, item transfer timelocks, custom metadata per item, gasless transactions from player managed wallets, and much more.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from metafab_python.model.create_collection_request import CreateCollectionRequest
from metafab_python.model.create_collection200_response import CreateCollection200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    create_collection_request = CreateCollectionRequest(
        chain="MATIC",
    ) # CreateCollectionRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create collection
        api_response = api_instance.create_collection(x_authorization, x_password, create_collection_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->create_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_password** | **str**| The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **create_collection_request** | [**CreateCollectionRequest**](CreateCollectionRequest.md)|  |

### Return type

[**CreateCollection200Response**](CreateCollection200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new item collection and deployed its associated ERC1155 contract on the chain specified. Returns a collection object containing a contract property with the deployment transaction. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_collection_item**
> TransactionModel create_collection_item(collection_id, x_authorization, x_password, create_collection_item_request)

Create collection item

Creates a new item type. Item type creation associates all of the relevant item data to a specific itemId. Such as item name, image, description, attributes, any arbitrary data such as 2D or 3D model resolver URLs, and more. It is recommended, but not required, that you create a new item type through this endpoint before minting any quantity of the related itemId.  Item type data is uploaded to, and resolved through IPFS for decentralized persistence. Any itemId provided will have its existing item type overriden if it already exists.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.create_collection_item_request import CreateCollectionItemRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    create_collection_item_request = CreateCollectionItemRequest(
        id=1337,
        name="Fire Dagger",
        description="description_example",
        image_base64='YQ==',
        image_url="https://mycdn.mygame.com/example/item1.gif",
        external_url="external_url_example",
        attributes=[
            CreateCollectionItemRequestAttributesInner(
                trait_type="Attack Power",
                value=CreateCollectionItemRequestAttributesInnerValue(None),
            ),
        ],
        data={},
    ) # CreateCollectionItemRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create collection item
        api_response = api_instance.create_collection_item(collection_id, x_authorization, x_password, create_collection_item_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->create_collection_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_password** | **str**| The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **create_collection_item_request** | [**CreateCollectionItemRequest**](CreateCollectionItemRequest.md)|  |

### Return type

[**TransactionModel**](TransactionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new item type and assigned it to the provided item &#x60;id&#x60;. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_approval**
> float get_collection_approval(collection_id, operator_address)

Get collection approval

Returns a boolean (true/false) representing if the provided operatorAddress has approval to transfer and burn items from the current collection owned by the address or address associated with the provided walletId.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.
    operator_address = "0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D" # str | A valid EVM based address. For example, `0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D`.
    address = "0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D" # str | A valid EVM based address. For example, `0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D`. (optional)
    wallet_id = "walletId_example" # str | Any wallet id within the MetaFab ecosystem. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get collection approval
        api_response = api_instance.get_collection_approval(collection_id, operator_address)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->get_collection_approval: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get collection approval
        api_response = api_instance.get_collection_approval(collection_id, operator_address, address=address, wallet_id=wallet_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->get_collection_approval: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |
 **operator_address** | **str**| A valid EVM based address. For example, &#x60;0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D&#x60;. |
 **address** | **str**| A valid EVM based address. For example, &#x60;0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D&#x60;. | [optional]
 **wallet_id** | **str**| Any wallet id within the MetaFab ecosystem. | [optional]

### Return type

**float**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the boolean value representing if the provided operatorAddress can transfer and burn owned items by the provided address or walletId. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_item**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_collection_item(collection_id, collection_item_id)

Get collection item

Returns a metadata object for the provided collectionItemId.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.
    collection_item_id = 3.14 # float | Any item id for the collection. Zero, or a positive integer.

    # example passing only required values which don't have defaults set
    try:
        # Get collection item
        api_response = api_instance.get_collection_item(collection_id, collection_item_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->get_collection_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |
 **collection_item_id** | **float**| Any item id for the collection. Zero, or a positive integer. |

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved collection item metadata. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_item_balance**
> float get_collection_item_balance(collection_id, collection_item_id)

Get collection item balance

Returns the current collection item balance of the provided collectionItemId for the provided wallet address or the wallet address associated with the provided walletId.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.
    collection_item_id = 3.14 # float | Any item id for the collection. Zero, or a positive integer.
    address = "0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D" # str | A valid EVM based address. For example, `0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D`. (optional)
    wallet_id = "walletId_example" # str | Any wallet id within the MetaFab ecosystem. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get collection item balance
        api_response = api_instance.get_collection_item_balance(collection_id, collection_item_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->get_collection_item_balance: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get collection item balance
        api_response = api_instance.get_collection_item_balance(collection_id, collection_item_id, address=address, wallet_id=wallet_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->get_collection_item_balance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |
 **collection_item_id** | **float**| Any item id for the collection. Zero, or a positive integer. |
 **address** | **str**| A valid EVM based address. For example, &#x60;0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D&#x60;. | [optional]
 **wallet_id** | **str**| Any wallet id within the MetaFab ecosystem. | [optional]

### Return type

**float**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved collection item balance of the provided collectionItemId for address or walletId. Balance is returned as a string to handle uint256 numbers. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_item_balances**
> {str: (float,)} get_collection_item_balances(collection_id)

Get collection item balances

Returns the current collection item balances of all collection items for the provided wallet address or the wallet address associated with the provided walletId.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.
    address = "0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D" # str | A valid EVM based address. For example, `0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D`. (optional)
    wallet_id = "walletId_example" # str | Any wallet id within the MetaFab ecosystem. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get collection item balances
        api_response = api_instance.get_collection_item_balances(collection_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->get_collection_item_balances: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get collection item balances
        api_response = api_instance.get_collection_item_balances(collection_id, address=address, wallet_id=wallet_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->get_collection_item_balances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |
 **address** | **str**| A valid EVM based address. For example, &#x60;0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D&#x60;. | [optional]
 **wallet_id** | **str**| Any wallet id within the MetaFab ecosystem. | [optional]

### Return type

**{str: (float,)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved currency balances of all collection items owned by the provided address or walletId. Balances are returned as a an object, mapping key value pairs as itemId -&gt; balance (string to handle uint256 numbers). |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_item_supplies**
> {str: (float,)} get_collection_item_supplies(collection_id)

Get collection item supplies

Returns the currency circulating supply of all collection items.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.

    # example passing only required values which don't have defaults set
    try:
        # Get collection item supplies
        api_response = api_instance.get_collection_item_supplies(collection_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->get_collection_item_supplies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |

### Return type

**{str: (float,)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the circulating supply of all collection items. Supplies are returned as a an object, mapping key value pairs as itemId -&gt; balance (string to handle uint256 numbers). |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_item_supply**
> float get_collection_item_supply(collection_id, collection_item_id)

Get collection item supply

Returns the current circulating supply of the provided collectionItemId.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.
    collection_item_id = 3.14 # float | Any item id for the collection. Zero, or a positive integer.
    address = "0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D" # str | A valid EVM based address. For example, `0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D`. (optional)
    wallet_id = "walletId_example" # str | Any wallet id within the MetaFab ecosystem. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get collection item supply
        api_response = api_instance.get_collection_item_supply(collection_id, collection_item_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->get_collection_item_supply: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get collection item supply
        api_response = api_instance.get_collection_item_supply(collection_id, collection_item_id, address=address, wallet_id=wallet_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->get_collection_item_supply: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |
 **collection_item_id** | **float**| Any item id for the collection. Zero, or a positive integer. |
 **address** | **str**| A valid EVM based address. For example, &#x60;0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D&#x60;. | [optional]
 **wallet_id** | **str**| Any wallet id within the MetaFab ecosystem. | [optional]

### Return type

**float**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved collection item supply. Supply is returned as a string to handle uint256 numbers. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_item_timelock**
> float get_collection_item_timelock(collection_id, collection_item_id)

Get collection item timelock

Returns a timestamp (in seconds) for when the provided collectionItemId's transfer timelock expires. A value of 0 means the provided collectionItemId does not have a timelock set. Timelocks prevent items of a specific collectionItemId from being transferred until the set timelock timestamp has been surpassed.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.
    collection_item_id = 3.14 # float | Any item id for the collection. Zero, or a positive integer.

    # example passing only required values which don't have defaults set
    try:
        # Get collection item timelock
        api_response = api_instance.get_collection_item_timelock(collection_id, collection_item_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->get_collection_item_timelock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |
 **collection_item_id** | **float**| Any item id for the collection. Zero, or a positive integer. |

### Return type

**float**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the collectionItemId&#39;s timelock. The timelock is returned as a unix timestamp in seconds. A return value of 0 means the collectionItemId does not have a timelock set. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_items**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_collection_items(collection_id)

Get collection items

Returns all collection items as an array of metadata objects.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.

    # example passing only required values which don't have defaults set
    try:
        # Get collection items
        api_response = api_instance.get_collection_items(collection_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->get_collection_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved collection items metadata. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collections**
> [GetCollections200ResponseInner] get_collections(x_game_key)

Get collections

Returns an array of active item collections for the game associated with the provided `X-Game-Key`.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from metafab_python.model.get_collections200_response_inner import GetCollections200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    x_game_key = "game_pk_4SOqpDi8pQdnQgfCOBW29qR8YmwOhxVPz5iHoMgUEJLDdPXgwLuHqZf8ewo2GajZ" # str | The `publishedKey` of a specific game. This can be shared or included in game clients, websites, etc.

    # example passing only required values which don't have defaults set
    try:
        # Get collections
        api_response = api_instance.get_collections(x_game_key)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->get_collections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_game_key** | **str**| The &#x60;publishedKey&#x60; of a specific game. This can be shared or included in game clients, websites, etc. |

### Return type

[**[GetCollections200ResponseInner]**](GetCollections200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved an array of item collections for the game associated with the provided &#x60;X-Game-Key&#x60; |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mint_collection_item**
> TransactionModel mint_collection_item(collection_id, collection_item_id, x_authorization, x_password, mint_collection_item_request)

Mint collection item

Creates (mints) the specified quantity of the provided collectionItemId to the provided wallet address or wallet address associated with the provided walletId.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.mint_collection_item_request import MintCollectionItemRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.
    collection_item_id = 3.14 # float | Any item id for the collection. Zero, or a positive integer.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    mint_collection_item_request = MintCollectionItemRequest(
        address="address_example",
        quantity=3.14,
        wallet_id="wallet_id_example",
    ) # MintCollectionItemRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Mint collection item
        api_response = api_instance.mint_collection_item(collection_id, collection_item_id, x_authorization, x_password, mint_collection_item_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->mint_collection_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |
 **collection_item_id** | **float**| Any item id for the collection. Zero, or a positive integer. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_password** | **str**| The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **mint_collection_item_request** | [**MintCollectionItemRequest**](MintCollectionItemRequest.md)|  |

### Return type

[**TransactionModel**](TransactionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created (minted) the item(s) to the provided wallet address or wallet address of the provided walletId. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_collection_approval**
> TransactionModel set_collection_approval(collection_id, x_authorization, x_password, set_collection_approval_request)

Set collection approval

Sets approval for the provided address or wallet address associated with the provided walletId to operate on behalf of the authenticating game or player's owned items for this collection. Setting an approved value of `true` allows the provided address or address associated with the provided walletId to transfer and burn items from this collection on behalf of the authenticated game or player's wallet address.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.set_collection_approval_request import SetCollectionApprovalRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.
    x_authorization = "["game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP","player_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP"]" # str | The `secretKey` of a specific game or the `accessToken` of a specific player.
    x_password = "mySecurePassword" # str | The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet.
    set_collection_approval_request = SetCollectionApprovalRequest(
        approved=True,
        address="address_example",
        wallet_id=[
            "wallet_id_example",
        ],
    ) # SetCollectionApprovalRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Set collection approval
        api_response = api_instance.set_collection_approval(collection_id, x_authorization, x_password, set_collection_approval_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->set_collection_approval: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of a specific game or the &#x60;accessToken&#x60; of a specific player. |
 **x_password** | **str**| The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet. |
 **set_collection_approval_request** | [**SetCollectionApprovalRequest**](SetCollectionApprovalRequest.md)|  |

### Return type

[**TransactionModel**](TransactionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully set approval for the provided address or address associated with the provided walletId to transfer and burn items from this collection on behalf of the authenticated game or player&#39;s wallet. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_collection_item_timelock**
> TransactionModel set_collection_item_timelock(collection_id, collection_item_id, x_authorization, x_password, set_collection_item_timelock_request)

Set collection item timelock

Sets the item timelock for the provided collection itemId. The timelock is a unix timestamp (in seconds) that defines a period in time of when an item may be transferred by players. Until the timelock timestamp has passed, the itemId for the given timelock may not be transferred, sold, traded, etc. A timelock of 0 (default) means that there is no timelock set on the itemId and it can be freely transferred, traded, etc.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.set_collection_item_timelock_request import SetCollectionItemTimelockRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.
    collection_item_id = 3.14 # float | Any item id for the collection. Zero, or a positive integer.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    set_collection_item_timelock_request = SetCollectionItemTimelockRequest(
        timelock=1665786026,
    ) # SetCollectionItemTimelockRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Set collection item timelock
        api_response = api_instance.set_collection_item_timelock(collection_id, collection_item_id, x_authorization, x_password, set_collection_item_timelock_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->set_collection_item_timelock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |
 **collection_item_id** | **float**| Any item id for the collection. Zero, or a positive integer. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_password** | **str**| The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **set_collection_item_timelock_request** | [**SetCollectionItemTimelockRequest**](SetCollectionItemTimelockRequest.md)|  |

### Return type

[**TransactionModel**](TransactionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully set the provided timelock for the provided itemId. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_collection_item**
> TransactionModel transfer_collection_item(collection_id, collection_item_id, x_authorization, x_password, transfer_collection_item_request)

Transfer collection item

Transfers specified quantity of itemId to the provided wallet address or wallet address associated with the provided walletId.

### Example


```python
import time
import metafab_python
from metafab_python.api import items_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.transfer_collection_item_request import TransferCollectionItemRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = items_api.ItemsApi(api_client)
    collection_id = "collectionId_example" # str | Any collection id within the MetaFab ecosystem.
    collection_item_id = 3.14 # float | Any item id for the collection. Zero, or a positive integer.
    x_authorization = "["game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP","player_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP"]" # str | The `secretKey` of a specific game or the `accessToken` of a specific player.
    x_password = "mySecurePassword" # str | The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet.
    transfer_collection_item_request = TransferCollectionItemRequest(
        address="address_example",
        wallet_id=[
            "wallet_id_example",
        ],
        quantity=3.14,
    ) # TransferCollectionItemRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Transfer collection item
        api_response = api_instance.transfer_collection_item(collection_id, collection_item_id, x_authorization, x_password, transfer_collection_item_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ItemsApi->transfer_collection_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Any collection id within the MetaFab ecosystem. |
 **collection_item_id** | **float**| Any item id for the collection. Zero, or a positive integer. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of a specific game or the &#x60;accessToken&#x60; of a specific player. |
 **x_password** | **str**| The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet. |
 **transfer_collection_item_request** | [**TransferCollectionItemRequest**](TransferCollectionItemRequest.md)|  |

### Return type

[**TransactionModel**](TransactionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully transferred the provided quantity of the collectionItemId to the provided wallet address or wallet address of the provided walletId. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

