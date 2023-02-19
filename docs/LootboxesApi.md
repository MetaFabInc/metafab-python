# metafab_python.LootboxesApi

All URIs are relative to *https://api.trymetafab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lootbox_manager**](LootboxesApi.md#create_lootbox_manager) | **POST** /v1/lootboxManagers | Create lootbox manager
[**get_lootbox_manager_lootbox**](LootboxesApi.md#get_lootbox_manager_lootbox) | **GET** /v1/lootboxManagers/{lootboxManagerId}/lootboxes/{lootboxManagerLootboxId} | Get lootbox manager lootbox
[**get_lootbox_manager_lootboxes**](LootboxesApi.md#get_lootbox_manager_lootboxes) | **GET** /v1/lootboxManagers/{lootboxManagerId}/lootboxes | Get lootbox manager lootboxes
[**get_lootbox_managers**](LootboxesApi.md#get_lootbox_managers) | **GET** /v1/lootboxManagers | Get lootbox managers
[**open_lootbox_manager_lootbox**](LootboxesApi.md#open_lootbox_manager_lootbox) | **POST** /v1/lootboxManagers/{lootboxManagerId}/lootboxes/{lootboxManagerLootboxId}/opens | Open lootbox manager lootbox
[**remove_lootbox_manager_lootbox**](LootboxesApi.md#remove_lootbox_manager_lootbox) | **DELETE** /v1/lootboxManagers/{lootboxManagerId}/lootboxes/{lootboxManagerLootboxId} | Remove lootbox manager lootbox
[**set_lootbox_manager_lootbox**](LootboxesApi.md#set_lootbox_manager_lootbox) | **POST** /v1/lootboxManagers/{lootboxManagerId}/lootboxes | Set lootbox manager lootbox


# **create_lootbox_manager**
> CreateLootboxManager200Response create_lootbox_manager(x_authorization, x_wallet_decrypt_key, create_lootbox_manager_request)

Create lootbox manager

Creates a new game lootbox manager and deploys a lootbox manager contract on behalf of the authenticating game's primary wallet. The deployed lootbox manager contract allows you to create lootbox behavior for existing items. For example, you can define item id(s) from one of your item collections as the requirement(s) to open a \"lootbox\". The required item(s) would be burned from the interacting player's wallet and the player would receive item(s) from a weighted randomized set of possible items the lootbox can contain.

### Example


```python
import time
import metafab_python
from metafab_python.api import lootboxes_api
from metafab_python.model.create_lootbox_manager200_response import CreateLootboxManager200Response
from metafab_python.model.create_lootbox_manager_request import CreateLootboxManagerRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lootboxes_api.LootboxesApi(api_client)
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_wallet_decrypt_key = "AXNP8MKb+5SbBtHWrZu5KHh5/BomXY/dMRG/BDUn7a4=" # str | The `walletDecryptKey` of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    create_lootbox_manager_request = CreateLootboxManagerRequest(
        name="name_example",
        chain="SELECT ONE",
    ) # CreateLootboxManagerRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create lootbox manager
        api_response = api_instance.create_lootbox_manager(x_authorization, x_wallet_decrypt_key, create_lootbox_manager_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling LootboxesApi->create_lootbox_manager: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_wallet_decrypt_key** | **str**| The &#x60;walletDecryptKey&#x60; of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **create_lootbox_manager_request** | [**CreateLootboxManagerRequest**](CreateLootboxManagerRequest.md)|  |

### Return type

[**CreateLootboxManager200Response**](CreateLootboxManager200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new lootbox manager and deployed its contract on the chain specified. Returns a lootbox manager object containing a contract property with the deployment transaction. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lootbox_manager_lootbox**
> LootboxManagerLootbox get_lootbox_manager_lootbox(lootbox_manager_id, lootbox_manager_lootbox_id)

Get lootbox manager lootbox

Returns a lootbox manager lootbox object for the provided lootboxManagerLootboxId.

### Example


```python
import time
import metafab_python
from metafab_python.api import lootboxes_api
from metafab_python.model.lootbox_manager_lootbox import LootboxManagerLootbox
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lootboxes_api.LootboxesApi(api_client)
    lootbox_manager_id = "lootboxManagerId_example" # str | Any lootbox manager id within the MetaFab platform.
    lootbox_manager_lootbox_id = "lootboxManagerLootboxId_example" # str | Any lootbox manager lootbox id within the MetaFab platform.

    # example passing only required values which don't have defaults set
    try:
        # Get lootbox manager lootbox
        api_response = api_instance.get_lootbox_manager_lootbox(lootbox_manager_id, lootbox_manager_lootbox_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling LootboxesApi->get_lootbox_manager_lootbox: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lootbox_manager_id** | **str**| Any lootbox manager id within the MetaFab platform. |
 **lootbox_manager_lootbox_id** | **str**| Any lootbox manager lootbox id within the MetaFab platform. |

### Return type

[**LootboxManagerLootbox**](LootboxManagerLootbox.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved lootbox manager lootbox. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lootbox_manager_lootboxes**
> [LootboxManagerLootbox] get_lootbox_manager_lootboxes(lootbox_manager_id)

Get lootbox manager lootboxes

Returns all lootbox manager lootboxes as an array of lootbox objects.

### Example


```python
import time
import metafab_python
from metafab_python.api import lootboxes_api
from metafab_python.model.lootbox_manager_lootbox import LootboxManagerLootbox
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lootboxes_api.LootboxesApi(api_client)
    lootbox_manager_id = "lootboxManagerId_example" # str | Any lootbox manager id within the MetaFab platform.

    # example passing only required values which don't have defaults set
    try:
        # Get lootbox manager lootboxes
        api_response = api_instance.get_lootbox_manager_lootboxes(lootbox_manager_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling LootboxesApi->get_lootbox_manager_lootboxes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lootbox_manager_id** | **str**| Any lootbox manager id within the MetaFab platform. |

### Return type

[**[LootboxManagerLootbox]**](LootboxManagerLootbox.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved lootbox manager lootboxes. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lootbox_managers**
> [GetLootboxManagers200ResponseInner] get_lootbox_managers(x_game_key)

Get lootbox managers

Returns an array of active lootbox managers for the game associated with the provided `X-Game-Key`.

### Example


```python
import time
import metafab_python
from metafab_python.api import lootboxes_api
from metafab_python.model.get_lootbox_managers200_response_inner import GetLootboxManagers200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lootboxes_api.LootboxesApi(api_client)
    x_game_key = "game_pk_4SOqpDi8pQdnQgfCOBW29qR8YmwOhxVPz5iHoMgUEJLDdPXgwLuHqZf8ewo2GajZ" # str | The `publishedKey` of a specific game. This can be shared or included in game clients, websites, etc.

    # example passing only required values which don't have defaults set
    try:
        # Get lootbox managers
        api_response = api_instance.get_lootbox_managers(x_game_key)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling LootboxesApi->get_lootbox_managers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_game_key** | **str**| The &#x60;publishedKey&#x60; of a specific game. This can be shared or included in game clients, websites, etc. |

### Return type

[**[GetLootboxManagers200ResponseInner]**](GetLootboxManagers200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved an array of lootbox managers for the game associated with the provided &#x60;X-Game-Key&#x60; |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_lootbox_manager_lootbox**
> [TransactionModel] open_lootbox_manager_lootbox(lootbox_manager_id, lootbox_manager_lootbox_id, x_authorization, x_wallet_decrypt_key)

Open lootbox manager lootbox

Opens a lootbox manager lootbox. The required input item(s) are burned from the wallet or player wallet opening the lootbox. The given output item(s) are given to the wallet or player wallet opening the lootbox.

### Example


```python
import time
import metafab_python
from metafab_python.api import lootboxes_api
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
    api_instance = lootboxes_api.LootboxesApi(api_client)
    lootbox_manager_id = "lootboxManagerId_example" # str | Any lootbox manager id within the MetaFab platform.
    lootbox_manager_lootbox_id = "lootboxManagerLootboxId_example" # str | Any lootbox manager lootbox id within the MetaFab platform.
    x_authorization = "["game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP","player_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP"]" # str | The `secretKey` of a specific game or the `accessToken` of a specific player.
    x_wallet_decrypt_key = "AXNP8MKb+5SbBtHWrZu5KHh5/BomXY/dMRG/BDUn7a4=" # str | The `walletDecryptKey` of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet.

    # example passing only required values which don't have defaults set
    try:
        # Open lootbox manager lootbox
        api_response = api_instance.open_lootbox_manager_lootbox(lootbox_manager_id, lootbox_manager_lootbox_id, x_authorization, x_wallet_decrypt_key)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling LootboxesApi->open_lootbox_manager_lootbox: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lootbox_manager_id** | **str**| Any lootbox manager id within the MetaFab platform. |
 **lootbox_manager_lootbox_id** | **str**| Any lootbox manager lootbox id within the MetaFab platform. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of a specific game or the &#x60;accessToken&#x60; of a specific player. |
 **x_wallet_decrypt_key** | **str**| The &#x60;walletDecryptKey&#x60; of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet. |

### Return type

[**[TransactionModel]**](TransactionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully opened provided lootbox manager lootbox. Returns an array of transaction objects. The first transaction object being for the lootbox opening, the second for claiming its contents. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_lootbox_manager_lootbox**
> TransactionModel remove_lootbox_manager_lootbox(lootbox_manager_id, lootbox_manager_lootbox_id, x_authorization, x_wallet_decrypt_key)

Remove lootbox manager lootbox

Removes the provided lootbox by lootboxId from the provided lootbox manager. Removed lootboxes can no longer be used.

### Example


```python
import time
import metafab_python
from metafab_python.api import lootboxes_api
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
    api_instance = lootboxes_api.LootboxesApi(api_client)
    lootbox_manager_id = "lootboxManagerId_example" # str | Any lootbox manager id within the MetaFab platform.
    lootbox_manager_lootbox_id = "lootboxManagerLootboxId_example" # str | Any lootbox manager lootbox id within the MetaFab platform.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_wallet_decrypt_key = "AXNP8MKb+5SbBtHWrZu5KHh5/BomXY/dMRG/BDUn7a4=" # str | The `walletDecryptKey` of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.

    # example passing only required values which don't have defaults set
    try:
        # Remove lootbox manager lootbox
        api_response = api_instance.remove_lootbox_manager_lootbox(lootbox_manager_id, lootbox_manager_lootbox_id, x_authorization, x_wallet_decrypt_key)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling LootboxesApi->remove_lootbox_manager_lootbox: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lootbox_manager_id** | **str**| Any lootbox manager id within the MetaFab platform. |
 **lootbox_manager_lootbox_id** | **str**| Any lootbox manager lootbox id within the MetaFab platform. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_wallet_decrypt_key** | **str**| The &#x60;walletDecryptKey&#x60; of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |

### Return type

[**TransactionModel**](TransactionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully removed the provided lootbox from the provided lootbox manager. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_lootbox_manager_lootbox**
> TransactionModel set_lootbox_manager_lootbox(lootbox_manager_id, x_authorization, x_wallet_decrypt_key, set_lootbox_manager_lootbox_request)

Set lootbox manager lootbox

Sets a new lootbox manager lootbox or updates an existing one for the provided id. Lootboxes allow item(s) to be burned to receive a random set of possible item(s) based on probability weight.  Lootboxes can require any number of unique types of items and quantities to open a created lootbox type within the system. A common pattern with lootboxes is to create a lootbox item type within an item collection, and require it as the input item type.

### Example


```python
import time
import metafab_python
from metafab_python.api import lootboxes_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.set_lootbox_manager_lootbox_request import SetLootboxManagerLootboxRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lootboxes_api.LootboxesApi(api_client)
    lootbox_manager_id = "lootboxManagerId_example" # str | Any lootbox manager id within the MetaFab platform.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_wallet_decrypt_key = "AXNP8MKb+5SbBtHWrZu5KHh5/BomXY/dMRG/BDUn7a4=" # str | The `walletDecryptKey` of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    set_lootbox_manager_lootbox_request = SetLootboxManagerLootboxRequest(
        id=1337,
        input_collection_address="input_collection_address_example",
        input_collection_id="input_collection_id_example",
        input_collection_item_ids=[
            1,
        ],
        input_collection_item_amounts=[
            1,
        ],
        output_collection_address="output_collection_address_example",
        output_collection_id="output_collection_id_example",
        output_collection_item_ids=[
            1,
        ],
        output_collection_item_amounts=[
            1,
        ],
        output_collection_item_weights=[
            1,
        ],
        output_total_items=1,
    ) # SetLootboxManagerLootboxRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Set lootbox manager lootbox
        api_response = api_instance.set_lootbox_manager_lootbox(lootbox_manager_id, x_authorization, x_wallet_decrypt_key, set_lootbox_manager_lootbox_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling LootboxesApi->set_lootbox_manager_lootbox: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lootbox_manager_id** | **str**| Any lootbox manager id within the MetaFab platform. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_wallet_decrypt_key** | **str**| The &#x60;walletDecryptKey&#x60; of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **set_lootbox_manager_lootbox_request** | [**SetLootboxManagerLootboxRequest**](SetLootboxManagerLootboxRequest.md)|  |

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
**200** | Successfully created or updated an lootbox manager lootbox for the provided lootbox id. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

