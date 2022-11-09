# metafab_python.ExchangesApi

All URIs are relative to *https://api.trymetafab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_exchange**](ExchangesApi.md#create_exchange) | **POST** /v1/exchanges | Create exchange
[**get_exchange_offer**](ExchangesApi.md#get_exchange_offer) | **GET** /v1/exchanges/{exchangeId}/items/{exchangeOfferId} | Get exchange offer
[**get_exchange_offers**](ExchangesApi.md#get_exchange_offers) | **GET** /v1/exchanges/{exchangeId}/offers | Get exchange offers
[**get_exchanges**](ExchangesApi.md#get_exchanges) | **GET** /v1/exchanges | Get exchanges
[**remove_exchange_offer**](ExchangesApi.md#remove_exchange_offer) | **DELETE** /v1/exchanges/{exchangeId}/offers/{exchangeOfferId} | Remove exchange offer
[**set_exchange_offer**](ExchangesApi.md#set_exchange_offer) | **POST** /v1/exchanges/{exchangeId}/offers | Set exchange offer
[**use_exchange_offer**](ExchangesApi.md#use_exchange_offer) | **POST** /v1/exchanges/{exchangeId}/offers/{exchangeOfferId}/uses | Use exchange offer
[**withdraw_from_exchange**](ExchangesApi.md#withdraw_from_exchange) | **POST** /v1/exchanges/{exchangeId}/withdrawals | Withdraw from exchange


# **create_exchange**
> CreateExchange200Response create_exchange(x_authorization, x_password, create_exchange_request)

Create exchange

Creates a new game exchange and deploys a exchange contract on behalf of the authenticating game's primary wallet. The deployed exchange contract allows you to create fixed price rates for players to buy specific items from any item collection or ERC1155 contract. Additionally, an exchange allows you to create exchange offers for some set of item(s) to another set of item(s) or any mix of currency. Exchanges completely supports gasless player transactions.

### Example


```python
import time
import metafab_python
from metafab_python.api import exchanges_api
from metafab_python.model.create_exchange200_response import CreateExchange200Response
from metafab_python.model.create_exchange_request import CreateExchangeRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = exchanges_api.ExchangesApi(api_client)
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    create_exchange_request = CreateExchangeRequest(
        chain="SELECT ONE",
    ) # CreateExchangeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create exchange
        api_response = api_instance.create_exchange(x_authorization, x_password, create_exchange_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ExchangesApi->create_exchange: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_password** | **str**| The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **create_exchange_request** | [**CreateExchangeRequest**](CreateExchangeRequest.md)|  |

### Return type

[**CreateExchange200Response**](CreateExchange200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new exchange and deployed its contract on the chain specified. Returns a exchange object containing a contract property with the deployment transaction. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_offer**
> ExchangeOffer get_exchange_offer(exchange_id, exchange_offer_id)

Get exchange offer

Returns a exchange offer object for the provided exchangeOfferId.

### Example


```python
import time
import metafab_python
from metafab_python.api import exchanges_api
from metafab_python.model.exchange_offer import ExchangeOffer
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = exchanges_api.ExchangesApi(api_client)
    exchange_id = "exchangeId_example" # str | Any exchange id within the MetaFab ecosystem.
    exchange_offer_id = "exchangeOfferId_example" # str | Any offer id for the exchange. Zero, or a positive integer.

    # example passing only required values which don't have defaults set
    try:
        # Get exchange offer
        api_response = api_instance.get_exchange_offer(exchange_id, exchange_offer_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ExchangesApi->get_exchange_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_id** | **str**| Any exchange id within the MetaFab ecosystem. |
 **exchange_offer_id** | **str**| Any offer id for the exchange. Zero, or a positive integer. |

### Return type

[**ExchangeOffer**](ExchangeOffer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved exchange offer. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_offers**
> [ExchangeOffer] get_exchange_offers(exchange_id)

Get exchange offers

Returns all exchange offers as an array of exchange offer objects.

### Example


```python
import time
import metafab_python
from metafab_python.api import exchanges_api
from metafab_python.model.exchange_offer import ExchangeOffer
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = exchanges_api.ExchangesApi(api_client)
    exchange_id = "exchangeId_example" # str | Any exchange id within the MetaFab ecosystem.

    # example passing only required values which don't have defaults set
    try:
        # Get exchange offers
        api_response = api_instance.get_exchange_offers(exchange_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ExchangesApi->get_exchange_offers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_id** | **str**| Any exchange id within the MetaFab ecosystem. |

### Return type

[**[ExchangeOffer]**](ExchangeOffer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved exchange offers. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchanges**
> [GetExchanges200ResponseInner] get_exchanges(x_game_key)

Get exchanges

Returns an array of active exchanges for the game associated with the provided `X-Game-Key`.

### Example


```python
import time
import metafab_python
from metafab_python.api import exchanges_api
from metafab_python.model.get_exchanges200_response_inner import GetExchanges200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = exchanges_api.ExchangesApi(api_client)
    x_game_key = "game_pk_4SOqpDi8pQdnQgfCOBW29qR8YmwOhxVPz5iHoMgUEJLDdPXgwLuHqZf8ewo2GajZ" # str | The `publishedKey` of a specific game. This can be shared or included in game clients, websites, etc.

    # example passing only required values which don't have defaults set
    try:
        # Get exchanges
        api_response = api_instance.get_exchanges(x_game_key)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ExchangesApi->get_exchanges: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_game_key** | **str**| The &#x60;publishedKey&#x60; of a specific game. This can be shared or included in game clients, websites, etc. |

### Return type

[**[GetExchanges200ResponseInner]**](GetExchanges200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved an array of exchanges for the game associated with the provided &#x60;X-Game-Key&#x60; |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_exchange_offer**
> TransactionModel remove_exchange_offer(exchange_id, exchange_offer_id, x_authorization, x_password)

Remove exchange offer

Removes the provided offerId from the provided exchange. Removed offers can no longer be used.

### Example


```python
import time
import metafab_python
from metafab_python.api import exchanges_api
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
    api_instance = exchanges_api.ExchangesApi(api_client)
    exchange_id = "exchangeId_example" # str | Any exchange id within the MetaFab ecosystem.
    exchange_offer_id = "exchangeOfferId_example" # str | Any offer id for the exchange. Zero, or a positive integer.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.

    # example passing only required values which don't have defaults set
    try:
        # Remove exchange offer
        api_response = api_instance.remove_exchange_offer(exchange_id, exchange_offer_id, x_authorization, x_password)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ExchangesApi->remove_exchange_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_id** | **str**| Any exchange id within the MetaFab ecosystem. |
 **exchange_offer_id** | **str**| Any offer id for the exchange. Zero, or a positive integer. |
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
**200** | Successfully removed the provided offer from the provided exchange. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_exchange_offer**
> TransactionModel set_exchange_offer(exchange_id, x_authorization, x_password, set_exchange_offer_request)

Set exchange offer

Sets a new exchange offer or updates an existing one for the provided id. Exchange offers allow currency to item, item to currency or item to item exchanges.  All request fields besides `id` are optional. Any optional fields omitted will not be used for the offer. This allows you to create many different combinations of offers. For example, you can create an offer that may require 3 unique item ids of specified quantities from a given item collection and gives the user 1 new unique item id in exchange.  Another example, you may want to make an exchange offer from one ERC20 token to another. This is also possible - simple set the input and output currency fields and leave the others blank.

### Example


```python
import time
import metafab_python
from metafab_python.api import exchanges_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.set_exchange_offer_request import SetExchangeOfferRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = exchanges_api.ExchangesApi(api_client)
    exchange_id = "exchangeId_example" # str | Any exchange id within the MetaFab ecosystem.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    set_exchange_offer_request = SetExchangeOfferRequest(
        id=1337,
        input_collection_address="input_collection_address_example",
        input_collection_id="input_collection_id_example",
        input_collection_item_ids=[
            3.14,
        ],
        input_collection_item_amounts=[
            3.14,
        ],
        input_currency_address="input_currency_address_example",
        input_currency_id="input_currency_id_example",
        input_currency_amount=3.14,
        output_collection_address="output_collection_address_example",
        output_collection_id="output_collection_id_example",
        output_collection_item_ids=[
            3.14,
        ],
        output_collection_item_amounts=[
            3.14,
        ],
        output_currency_address="output_currency_address_example",
        output_currency_id="output_currency_id_example",
        output_currency_amount=3.14,
        max_uses=3.14,
    ) # SetExchangeOfferRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Set exchange offer
        api_response = api_instance.set_exchange_offer(exchange_id, x_authorization, x_password, set_exchange_offer_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ExchangesApi->set_exchange_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_id** | **str**| Any exchange id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_password** | **str**| The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **set_exchange_offer_request** | [**SetExchangeOfferRequest**](SetExchangeOfferRequest.md)|  |

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
**200** | Successfully created or updated an exchange offer for the provided offer id. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **use_exchange_offer**
> TransactionModel use_exchange_offer(exchange_id, exchange_offer_id, x_authorization, x_password)

Use exchange offer

Uses an exchange offer. The required (input) item(s) and/or currency are removed from the wallet or player wallet using the offer. The given (output) item(s) and/or currency are given to the wallet or player wallet using the offer.

### Example


```python
import time
import metafab_python
from metafab_python.api import exchanges_api
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
    api_instance = exchanges_api.ExchangesApi(api_client)
    exchange_id = "exchangeId_example" # str | Any exchange id within the MetaFab ecosystem.
    exchange_offer_id = "exchangeOfferId_example" # str | Any offer id for the exchange. Zero, or a positive integer.
    x_authorization = "["game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP","player_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP"]" # str | The `secretKey` of a specific game or the `accessToken` of a specific player.
    x_password = "mySecurePassword" # str | The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet.

    # example passing only required values which don't have defaults set
    try:
        # Use exchange offer
        api_response = api_instance.use_exchange_offer(exchange_id, exchange_offer_id, x_authorization, x_password)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ExchangesApi->use_exchange_offer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_id** | **str**| Any exchange id within the MetaFab ecosystem. |
 **exchange_offer_id** | **str**| Any offer id for the exchange. Zero, or a positive integer. |
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
**200** | Successfully used provided exchange offer. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_from_exchange**
> TransactionModel withdraw_from_exchange(exchange_id, x_authorization, x_password, withdraw_from_exchange_request)

Withdraw from exchange

Withdraws native token, currency or items from a exchange. Whenever an exchange offer has input requirements, the native tokens, currencies or items for the requirements of that offer are deposited into the exchange contract when the offer is used. These can be withdrawn to any other address.

### Example


```python
import time
import metafab_python
from metafab_python.api import exchanges_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.withdraw_from_exchange_request import WithdrawFromExchangeRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = exchanges_api.ExchangesApi(api_client)
    exchange_id = "exchangeId_example" # str | Any exchange id within the MetaFab ecosystem.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    withdraw_from_exchange_request = WithdrawFromExchangeRequest(
        address="address_example",
        wallet_id="wallet_id_example",
        currency_address="currency_address_example",
        currency_id="currency_id_example",
        collection_address="collection_address_example",
        collection_id="collection_id_example",
        item_ids=[
            3.14,
        ],
    ) # WithdrawFromExchangeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Withdraw from exchange
        api_response = api_instance.withdraw_from_exchange(exchange_id, x_authorization, x_password, withdraw_from_exchange_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ExchangesApi->withdraw_from_exchange: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_id** | **str**| Any exchange id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_password** | **str**| The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **withdraw_from_exchange_request** | [**WithdrawFromExchangeRequest**](WithdrawFromExchangeRequest.md)|  |

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

