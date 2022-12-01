# metafab_python.ShopsApi

All URIs are relative to *https://api.trymetafab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shop**](ShopsApi.md#create_shop) | **POST** /v1/shops | Create shop
[**get_shop_offer**](ShopsApi.md#get_shop_offer) | **GET** /v1/shops/{shopId}/items/{shopOfferId} | Get shop offer
[**get_shop_offers**](ShopsApi.md#get_shop_offers) | **GET** /v1/shops/{shopId}/offers | Get shop offers
[**get_shops**](ShopsApi.md#get_shops) | **GET** /v1/shops | Get shops
[**remove_shop_offer**](ShopsApi.md#remove_shop_offer) | **DELETE** /v1/shops/{shopId}/offers/{shopOfferId} | Remove shop offer
[**set_shop_offer**](ShopsApi.md#set_shop_offer) | **POST** /v1/shops/{shopId}/offers | Set shop offer
[**use_shop_offer**](ShopsApi.md#use_shop_offer) | **POST** /v1/shops/{shopId}/offers/{shopOfferId}/uses | Use shop offer
[**withdraw_from_shop**](ShopsApi.md#withdraw_from_shop) | **POST** /v1/shops/{shopId}/withdrawals | Withdraw from shop


# **create_shop**
> CreateShop200Response create_shop(x_authorization, x_password, create_shop_request)

Create shop

Creates a new game shop and deploys a shop contract on behalf of the authenticating game's primary wallet. The deployed shop contract allows you to create fixed price rates for players to buy specific items from any item collection or ERC1155 contract. Additionally, a shop allows you to create shop offers for some set of item(s) to another set of item(s) or any mix of currency. Shops completely support gasless player transactions.

### Example


```python
import time
import metafab_python
from metafab_python.api import shops_api
from metafab_python.model.create_shop_request import CreateShopRequest
from metafab_python.model.create_shop200_response import CreateShop200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = shops_api.ShopsApi(api_client)
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    create_shop_request = CreateShopRequest(
        chain="SELECT ONE",
    ) # CreateShopRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create shop
        api_response = api_instance.create_shop(x_authorization, x_password, create_shop_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ShopsApi->create_shop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_password** | **str**| The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **create_shop_request** | [**CreateShopRequest**](CreateShopRequest.md)|  |

### Return type

[**CreateShop200Response**](CreateShop200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new shop and deployed its contract on the chain specified. Returns a shop object containing a contract property with the deployment transaction. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shop_offer**
> ShopOffer get_shop_offer(shop_id, shop_offer_id)

Get shop offer

Returns a shop offer object for the provided shopOfferId.

### Example


```python
import time
import metafab_python
from metafab_python.api import shops_api
from metafab_python.model.shop_offer import ShopOffer
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = shops_api.ShopsApi(api_client)
    shop_id = "shopId_example" # str | Any shop id within the MetaFab ecosystem.
    shop_offer_id = "shopOfferId_example" # str | Any offer id for the shop. Zero, or a positive integer.

    # example passing only required values which don't have defaults set
    try:
        # Get shop offer
        api_response = api_instance.get_shop_offer(shop_id, shop_offer_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ShopsApi->get_shop_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **str**| Any shop id within the MetaFab ecosystem. |
 **shop_offer_id** | **str**| Any offer id for the shop. Zero, or a positive integer. |

### Return type

[**ShopOffer**](ShopOffer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved shop offer. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shop_offers**
> [ShopOffer] get_shop_offers(shop_id)

Get shop offers

Returns all shop offers as an array of shop offer objects.

### Example


```python
import time
import metafab_python
from metafab_python.api import shops_api
from metafab_python.model.shop_offer import ShopOffer
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = shops_api.ShopsApi(api_client)
    shop_id = "shopId_example" # str | Any shop id within the MetaFab ecosystem.

    # example passing only required values which don't have defaults set
    try:
        # Get shop offers
        api_response = api_instance.get_shop_offers(shop_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ShopsApi->get_shop_offers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **str**| Any shop id within the MetaFab ecosystem. |

### Return type

[**[ShopOffer]**](ShopOffer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved shop offers. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shops**
> [GetShops200ResponseInner] get_shops(x_game_key)

Get shops

Returns an array of active shops for the game associated with the provided `X-Game-Key`.

### Example


```python
import time
import metafab_python
from metafab_python.api import shops_api
from metafab_python.model.get_shops200_response_inner import GetShops200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = shops_api.ShopsApi(api_client)
    x_game_key = "game_pk_4SOqpDi8pQdnQgfCOBW29qR8YmwOhxVPz5iHoMgUEJLDdPXgwLuHqZf8ewo2GajZ" # str | The `publishedKey` of a specific game. This can be shared or included in game clients, websites, etc.

    # example passing only required values which don't have defaults set
    try:
        # Get shops
        api_response = api_instance.get_shops(x_game_key)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ShopsApi->get_shops: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_game_key** | **str**| The &#x60;publishedKey&#x60; of a specific game. This can be shared or included in game clients, websites, etc. |

### Return type

[**[GetShops200ResponseInner]**](GetShops200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved an array of shops for the game associated with the provided &#x60;X-Game-Key&#x60; |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_shop_offer**
> TransactionModel remove_shop_offer(shop_id, shop_offer_id, x_authorization, x_password)

Remove shop offer

Removes the provided offer by offerId from the provided shop. Removed offers can no longer be used.

### Example


```python
import time
import metafab_python
from metafab_python.api import shops_api
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
    api_instance = shops_api.ShopsApi(api_client)
    shop_id = "shopId_example" # str | Any shop id within the MetaFab ecosystem.
    shop_offer_id = "shopOfferId_example" # str | Any offer id for the shop. Zero, or a positive integer.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.

    # example passing only required values which don't have defaults set
    try:
        # Remove shop offer
        api_response = api_instance.remove_shop_offer(shop_id, shop_offer_id, x_authorization, x_password)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ShopsApi->remove_shop_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **str**| Any shop id within the MetaFab ecosystem. |
 **shop_offer_id** | **str**| Any offer id for the shop. Zero, or a positive integer. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_password** | **str**| The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |

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
**200** | Successfully removed the provided offer from the provided shop. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_shop_offer**
> TransactionModel set_shop_offer(shop_id, x_authorization, x_password, set_shop_offer_request)

Set shop offer

Sets a new shop offer or updates an existing one for the provided id. Shop offers allow currency to item, item to currency or item to item exchanges.  All request fields besides `id` are optional. Any optional fields omitted will not be used for the offer. This allows you to create many different combinations of offers. For example, you can create an offer that may require 3 unique item ids of specified quantities from a given item collection and gives the user 1 new unique item id in exchange.  Another example, you may want to make a shop offer from one ERC20 token to another. This is also possible - simple set the input and output currency fields and leave the others blank.

### Example


```python
import time
import metafab_python
from metafab_python.api import shops_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.set_shop_offer_request import SetShopOfferRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = shops_api.ShopsApi(api_client)
    shop_id = "shopId_example" # str | Any shop id within the MetaFab ecosystem.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    set_shop_offer_request = SetShopOfferRequest(
        id=1337,
        input_collection_address="input_collection_address_example",
        input_collection_id="input_collection_id_example",
        input_collection_item_ids=[
            1,
        ],
        input_collection_item_amounts=[
            1,
        ],
        input_currency_address="input_currency_address_example",
        input_currency_id="input_currency_id_example",
        input_currency_amount=3.14,
        output_collection_address="output_collection_address_example",
        output_collection_id="output_collection_id_example",
        output_collection_item_ids=[
            1,
        ],
        output_collection_item_amounts=[
            1,
        ],
        output_currency_address="output_currency_address_example",
        output_currency_id="output_currency_id_example",
        output_currency_amount=3.14,
        max_uses=1,
    ) # SetShopOfferRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Set shop offer
        api_response = api_instance.set_shop_offer(shop_id, x_authorization, x_password, set_shop_offer_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ShopsApi->set_shop_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **str**| Any shop id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_password** | **str**| The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **set_shop_offer_request** | [**SetShopOfferRequest**](SetShopOfferRequest.md)|  |

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
**200** | Successfully created or updated a shop offer for the provided offer id. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **use_shop_offer**
> TransactionModel use_shop_offer(shop_id, shop_offer_id, x_authorization, x_password)

Use shop offer

Uses a shop offer. The required (input) item(s) and/or currency are removed from the wallet or player wallet using the offer. The given (output) item(s) and/or currency are given to the wallet or player wallet using the offer.

### Example


```python
import time
import metafab_python
from metafab_python.api import shops_api
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
    api_instance = shops_api.ShopsApi(api_client)
    shop_id = "shopId_example" # str | Any shop id within the MetaFab ecosystem.
    shop_offer_id = "shopOfferId_example" # str | Any offer id for the shop. Zero, or a positive integer.
    x_authorization = "["game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP","player_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP"]" # str | The `secretKey` of a specific game or the `accessToken` of a specific player.
    x_password = "mySecurePassword" # str | The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet.

    # example passing only required values which don't have defaults set
    try:
        # Use shop offer
        api_response = api_instance.use_shop_offer(shop_id, shop_offer_id, x_authorization, x_password)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ShopsApi->use_shop_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **str**| Any shop id within the MetaFab ecosystem. |
 **shop_offer_id** | **str**| Any offer id for the shop. Zero, or a positive integer. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of a specific game or the &#x60;accessToken&#x60; of a specific player. |
 **x_password** | **str**| The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet. |

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
**200** | Successfully used provided shop offer. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_from_shop**
> TransactionModel withdraw_from_shop(shop_id, x_authorization, x_password, withdraw_from_shop_request)

Withdraw from shop

Withdraws native token, currency or items from a shop. Whenever a shop offer has input requirements, the native tokens, currencies or items for the requirements of that offer are deposited into the shop contract when the offer is used. These can be withdrawn to any other address.

### Example


```python
import time
import metafab_python
from metafab_python.api import shops_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.withdraw_from_shop_request import WithdrawFromShopRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = shops_api.ShopsApi(api_client)
    shop_id = "shopId_example" # str | Any shop id within the MetaFab ecosystem.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    withdraw_from_shop_request = WithdrawFromShopRequest(
        address="address_example",
        wallet_id="wallet_id_example",
        currency_address="currency_address_example",
        currency_id="currency_id_example",
        collection_address="collection_address_example",
        collection_id="collection_id_example",
        item_ids=[
            1,
        ],
    ) # WithdrawFromShopRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Withdraw from shop
        api_response = api_instance.withdraw_from_shop(shop_id, x_authorization, x_password, withdraw_from_shop_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ShopsApi->withdraw_from_shop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **str**| Any shop id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_password** | **str**| The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **withdraw_from_shop_request** | [**WithdrawFromShopRequest**](WithdrawFromShopRequest.md)|  |

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
**200** | Successfully performed a withdrawal to the provided wallet address or wallet address of the provided walletId. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

