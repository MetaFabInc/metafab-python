# metafab_python.CurrenciesApi

All URIs are relative to *https://api.trymetafab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_transfer_currency**](CurrenciesApi.md#batch_transfer_currency) | **POST** /v1/currencies/{currencyId}/batchTransfers | Batch transfer currency
[**burn_currency**](CurrenciesApi.md#burn_currency) | **POST** /v1/currencies/{currencyId}/burns | Burn currency
[**create_currency**](CurrenciesApi.md#create_currency) | **POST** /v1/currencies | Create currency
[**get_currencies**](CurrenciesApi.md#get_currencies) | **GET** /v1/currencies | Get currencies
[**get_currency_balance**](CurrenciesApi.md#get_currency_balance) | **GET** /v1/currencies/{currencyId}/balances | Get currency balance
[**get_currency_fees**](CurrenciesApi.md#get_currency_fees) | **GET** /v1/currencies/{currencyId}/fees | Get currency fees
[**get_currency_role**](CurrenciesApi.md#get_currency_role) | **GET** /v1/currencies/{currencyId}/roles | Get currency role
[**grant_currency_role**](CurrenciesApi.md#grant_currency_role) | **POST** /v1/currencies/{currencyId}/roles | Grant currency role
[**mint_currency**](CurrenciesApi.md#mint_currency) | **POST** /v1/currencies/{currencyId}/mints | Mint currency
[**revoke_currency_role**](CurrenciesApi.md#revoke_currency_role) | **DELETE** /v1/currencies/{currencyId}/roles | Revoke currency role
[**set_currency_fees**](CurrenciesApi.md#set_currency_fees) | **POST** /v1/currencies/{currencyId}/fees | Set currency fees
[**transfer_currency**](CurrenciesApi.md#transfer_currency) | **POST** /v1/currencies/{currencyId}/transfers | Transfer currency


# **batch_transfer_currency**
> TransactionModel batch_transfer_currency(currency_id, x_authorization, x_password, batch_transfer_currency_request)

Batch transfer currency

Transfers multiple amounts of currency to multiple provided wallet addresses or wallet addresses associated with the provided walletIds. You may also provide a combination of addresses and walletIds in one request, the proper receipients will be automatically determined, with `addresses` getting `amounts` order priority first.  Optional references may be included for the transfer. References are useful for identifying transfers intended to pay for items, trades, services and more.

### Example


```python
import time
import metafab_python
from metafab_python.api import currencies_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.batch_transfer_currency_request import BatchTransferCurrencyRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = currencies_api.CurrenciesApi(api_client)
    currency_id = "currencyId_example" # str | Any currency id within the MetaFab ecosystem.
    x_authorization = "["game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP","player_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP"]" # str | The `secretKey` of a specific game or the `accessToken` of a specific player.
    x_password = "mySecurePassword" # str | The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet.
    batch_transfer_currency_request = BatchTransferCurrencyRequest(
        addresses=[
            "addresses_example",
        ],
        wallet_ids=[
            "wallet_ids_example",
        ],
        amounts=[
            10,
        ],
        references=[
            3.14,
        ],
    ) # BatchTransferCurrencyRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Batch transfer currency
        api_response = api_instance.batch_transfer_currency(currency_id, x_authorization, x_password, batch_transfer_currency_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling CurrenciesApi->batch_transfer_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_id** | **str**| Any currency id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of a specific game or the &#x60;accessToken&#x60; of a specific player. |
 **x_password** | **str**| The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet. |
 **batch_transfer_currency_request** | [**BatchTransferCurrencyRequest**](BatchTransferCurrencyRequest.md)|  |

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
**200** | Successfully transferred the currency amounts to the provided wallet addresses and/or wallet addresses of the provided walletIds. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **burn_currency**
> TransactionModel burn_currency(currency_id, x_authorization, x_password, burn_currency_request)

Burn currency

Removes (burns) the provided amount of currency from the authenticating game or players wallet. The currency amount is permanently removed from the circulating supply of the currency.

### Example


```python
import time
import metafab_python
from metafab_python.api import currencies_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.burn_currency_request import BurnCurrencyRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = currencies_api.CurrenciesApi(api_client)
    currency_id = "currencyId_example" # str | Any currency id within the MetaFab ecosystem.
    x_authorization = "["game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP","player_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP"]" # str | The `secretKey` of a specific game or the `accessToken` of a specific player.
    x_password = "mySecurePassword" # str | The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet.
    burn_currency_request = BurnCurrencyRequest(
        amount=133.7,
    ) # BurnCurrencyRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Burn currency
        api_response = api_instance.burn_currency(currency_id, x_authorization, x_password, burn_currency_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling CurrenciesApi->burn_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_id** | **str**| Any currency id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of a specific game or the &#x60;accessToken&#x60; of a specific player. |
 **x_password** | **str**| The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet. |
 **burn_currency_request** | [**BurnCurrencyRequest**](BurnCurrencyRequest.md)|  |

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
**200** | Successfully removed (burned) the currency amount from the authenticating game or player&#39;s wallet. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_currency**
> CreateCurrency200Response create_currency(x_authorization, x_password, create_currency_request)

Create currency

Creates a new game currency and deploys an ERC20 token contract on behalf of the authenticating game's primary wallet. The deployed ERC20 contract is preconfigured to fully support bridging across blockchains, batched transfers and gasless transactions on any supported blockchain as well as full support for gasless transactions from player managed wallets.

### Example


```python
import time
import metafab_python
from metafab_python.api import currencies_api
from metafab_python.model.create_currency_request import CreateCurrencyRequest
from metafab_python.model.create_currency200_response import CreateCurrency200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = currencies_api.CurrenciesApi(api_client)
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    create_currency_request = CreateCurrencyRequest(
        name="Bright Gems",
        symbol="BGEM",
        supply_cap=15000.5,
        chain="MATIC",
    ) # CreateCurrencyRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create currency
        api_response = api_instance.create_currency(x_authorization, x_password, create_currency_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling CurrenciesApi->create_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_password** | **str**| The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **create_currency_request** | [**CreateCurrencyRequest**](CreateCurrencyRequest.md)|  |

### Return type

[**CreateCurrency200Response**](CreateCurrency200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new currency and deployed its associated ERC20 token contract on the chain specified. Returns a currency object containing a contract property with the deployment transaction. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currencies**
> [GetCurrencies200ResponseInner] get_currencies(x_game_key)

Get currencies

Returns an array of active currencies for the game associated with the provided `X-Game-Key`.

### Example


```python
import time
import metafab_python
from metafab_python.api import currencies_api
from metafab_python.model.get_currencies200_response_inner import GetCurrencies200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = currencies_api.CurrenciesApi(api_client)
    x_game_key = "game_pk_4SOqpDi8pQdnQgfCOBW29qR8YmwOhxVPz5iHoMgUEJLDdPXgwLuHqZf8ewo2GajZ" # str | The `publishedKey` of a specific game. This can be shared or included in game clients, websites, etc.

    # example passing only required values which don't have defaults set
    try:
        # Get currencies
        api_response = api_instance.get_currencies(x_game_key)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling CurrenciesApi->get_currencies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_game_key** | **str**| The &#x60;publishedKey&#x60; of a specific game. This can be shared or included in game clients, websites, etc. |

### Return type

[**[GetCurrencies200ResponseInner]**](GetCurrencies200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved an array of currencies for the game associated with the provided &#x60;X-Game-Key&#x60; |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency_balance**
> float get_currency_balance(currency_id)

Get currency balance

Returns the current currency balance of the provided wallet address or or the wallet address associated with the provided walletId.

### Example


```python
import time
import metafab_python
from metafab_python.api import currencies_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = currencies_api.CurrenciesApi(api_client)
    currency_id = "currencyId_example" # str | Any currency id within the MetaFab ecosystem.
    address = "0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D" # str | A valid EVM based address. For example, `0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D`. (optional)
    wallet_id = "walletId_example" # str | Any wallet id within the MetaFab ecosystem. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get currency balance
        api_response = api_instance.get_currency_balance(currency_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling CurrenciesApi->get_currency_balance: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get currency balance
        api_response = api_instance.get_currency_balance(currency_id, address=address, wallet_id=wallet_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling CurrenciesApi->get_currency_balance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_id** | **str**| Any currency id within the MetaFab ecosystem. |
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
**200** | Successfully retrieved currency balance for the provided address or walletId. Balance is returned as a string to handle uint256 numbers. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency_fees**
> GetCurrencyFees200Response get_currency_fees(currency_id)

Get currency fees

Returns the current fee recipient address and fees of the currency for the provided currencyId. Fees are only applicable for gasless transactions performed by default by players.

### Example


```python
import time
import metafab_python
from metafab_python.api import currencies_api
from metafab_python.model.get_currency_fees200_response import GetCurrencyFees200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = currencies_api.CurrenciesApi(api_client)
    currency_id = "currencyId_example" # str | Any currency id within the MetaFab ecosystem.

    # example passing only required values which don't have defaults set
    try:
        # Get currency fees
        api_response = api_instance.get_currency_fees(currency_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling CurrenciesApi->get_currency_fees: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_id** | **str**| Any currency id within the MetaFab ecosystem. |

### Return type

[**GetCurrencyFees200Response**](GetCurrencyFees200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved currency fees for the currency of the provided currencyId. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency_role**
> bool get_currency_role(currency_id, role)

Get currency role

Returns a boolean (true/false) representing if the provided role for this currency has been granted to the provided address or address associated with the provided walletId.

### Example


```python
import time
import metafab_python
from metafab_python.api import currencies_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = currencies_api.CurrenciesApi(api_client)
    currency_id = "currencyId_example" # str | Any currency id within the MetaFab ecosystem.
    role = "minter" # str | A valid MetaFab role or bytes string representing a role, such as `0xc9eb32e43bf5ecbceacf00b32281dfc5d6d700a0db676ea26ccf938a385ac3b7`
    address = "0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D" # str | A valid EVM based address. For example, `0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D`. (optional)
    wallet_id = "walletId_example" # str | Any wallet id within the MetaFab ecosystem. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get currency role
        api_response = api_instance.get_currency_role(currency_id, role)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling CurrenciesApi->get_currency_role: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get currency role
        api_response = api_instance.get_currency_role(currency_id, role, address=address, wallet_id=wallet_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling CurrenciesApi->get_currency_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_id** | **str**| Any currency id within the MetaFab ecosystem. |
 **role** | **str**| A valid MetaFab role or bytes string representing a role, such as &#x60;0xc9eb32e43bf5ecbceacf00b32281dfc5d6d700a0db676ea26ccf938a385ac3b7&#x60; |
 **address** | **str**| A valid EVM based address. For example, &#x60;0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D&#x60;. | [optional]
 **wallet_id** | **str**| Any wallet id within the MetaFab ecosystem. | [optional]

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the boolean value representing if the provided role has been granted to the provided address or walletId. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_currency_role**
> TransactionModel grant_currency_role(currency_id, x_authorization, x_password, grant_currency_role_request)

Grant currency role

Grants the provided role for the currency to the provided address or address associated with the provided walletId. Granted roles give different types of authority on behalf of the currency for specific players, addresses, or contracts to perform different types of permissioned currency operations.

### Example


```python
import time
import metafab_python
from metafab_python.api import currencies_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.grant_currency_role_request import GrantCurrencyRoleRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = currencies_api.CurrenciesApi(api_client)
    currency_id = "currencyId_example" # str | Any currency id within the MetaFab ecosystem.
    x_authorization = "["game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP","player_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP"]" # str | The `secretKey` of a specific game or the `accessToken` of a specific player.
    x_password = "mySecurePassword" # str | The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet.
    grant_currency_role_request = GrantCurrencyRoleRequest(
        role="role_example",
        address="address_example",
        wallet_id=[
            "wallet_id_example",
        ],
    ) # GrantCurrencyRoleRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Grant currency role
        api_response = api_instance.grant_currency_role(currency_id, x_authorization, x_password, grant_currency_role_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling CurrenciesApi->grant_currency_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_id** | **str**| Any currency id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of a specific game or the &#x60;accessToken&#x60; of a specific player. |
 **x_password** | **str**| The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet. |
 **grant_currency_role_request** | [**GrantCurrencyRoleRequest**](GrantCurrencyRoleRequest.md)|  |

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
**200** | Successfully granted the provided role to the provided address or address associated with the provided walletId. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mint_currency**
> TransactionModel mint_currency(currency_id, x_authorization, x_password, mint_currency_request)

Mint currency

Creates (mints) the provided amount of currency to the provided wallet address or wallet address associated with the provided walletId.

### Example


```python
import time
import metafab_python
from metafab_python.api import currencies_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.mint_currency_request import MintCurrencyRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = currencies_api.CurrenciesApi(api_client)
    currency_id = "currencyId_example" # str | Any currency id within the MetaFab ecosystem.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    mint_currency_request = MintCurrencyRequest(
        amount=133.7,
        address="address_example",
        wallet_id="wallet_id_example",
    ) # MintCurrencyRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Mint currency
        api_response = api_instance.mint_currency(currency_id, x_authorization, x_password, mint_currency_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling CurrenciesApi->mint_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_id** | **str**| Any currency id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_password** | **str**| The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **mint_currency_request** | [**MintCurrencyRequest**](MintCurrencyRequest.md)|  |

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
**200** | Successfully created (minted) the currency amount to the provided wallet address or wallet address of the provided walletId. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_currency_role**
> TransactionModel revoke_currency_role(currency_id, x_authorization, x_password, revoke_collection_role_request)

Revoke currency role

Revokes the provided role for the currency to the provided address or address associated with the provided walletId.

### Example


```python
import time
import metafab_python
from metafab_python.api import currencies_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.revoke_collection_role_request import RevokeCollectionRoleRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = currencies_api.CurrenciesApi(api_client)
    currency_id = "currencyId_example" # str | Any currency id within the MetaFab ecosystem.
    x_authorization = "["game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP","player_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP"]" # str | The `secretKey` of a specific game or the `accessToken` of a specific player.
    x_password = "mySecurePassword" # str | The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet.
    revoke_collection_role_request = RevokeCollectionRoleRequest(
        role="role_example",
        address="address_example",
        wallet_id=[
            "wallet_id_example",
        ],
    ) # RevokeCollectionRoleRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Revoke currency role
        api_response = api_instance.revoke_currency_role(currency_id, x_authorization, x_password, revoke_collection_role_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling CurrenciesApi->revoke_currency_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_id** | **str**| Any currency id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of a specific game or the &#x60;accessToken&#x60; of a specific player. |
 **x_password** | **str**| The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet. |
 **revoke_collection_role_request** | [**RevokeCollectionRoleRequest**](RevokeCollectionRoleRequest.md)|  |

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
**200** | Successfully revoked the provided role from the provided address or address associated with the provided walletId. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_currency_fees**
> TransactionModel set_currency_fees(currency_id, x_authorization, x_password, set_currency_fees_request)

Set currency fees

Sets the recipient address, basis points, fixed amount and cap amount for a currency's fees.

### Example


```python
import time
import metafab_python
from metafab_python.api import currencies_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.set_currency_fees_request import SetCurrencyFeesRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = currencies_api.CurrenciesApi(api_client)
    currency_id = "currencyId_example" # str | Any currency id within the MetaFab ecosystem.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_password = "mySecurePassword" # str | The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    set_currency_fees_request = SetCurrencyFeesRequest(
        recipient_address="recipient_address_example",
        basis_points=3.14,
        fixed_amount=3.14,
        cap_amount=3.14,
    ) # SetCurrencyFeesRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Set currency fees
        api_response = api_instance.set_currency_fees(currency_id, x_authorization, x_password, set_currency_fees_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling CurrenciesApi->set_currency_fees: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_id** | **str**| Any currency id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_password** | **str**| The password of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **set_currency_fees_request** | [**SetCurrencyFeesRequest**](SetCurrencyFeesRequest.md)|  |

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
**200** | Successfuly set the currency&#39;s fees. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_currency**
> TransactionModel transfer_currency(currency_id, x_authorization, x_password, transfer_currency_request)

Transfer currency

Transfers an amount of currency to the provided wallet address or wallet address associated with the provided walletId. If you want to transfer to multiple wallets with different amounts and optional references in one API request, please see the Batch transfer currency documentation.  An optional reference may be included for the transfer. References are useful for identifying transfers intended to pay for items, trades, services and more.

### Example


```python
import time
import metafab_python
from metafab_python.api import currencies_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.transfer_currency_request import TransferCurrencyRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = currencies_api.CurrenciesApi(api_client)
    currency_id = "currencyId_example" # str | Any currency id within the MetaFab ecosystem.
    x_authorization = "["game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP","player_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP"]" # str | The `secretKey` of a specific game or the `accessToken` of a specific player.
    x_password = "mySecurePassword" # str | The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet.
    transfer_currency_request = TransferCurrencyRequest(
        address="address_example",
        wallet_id="wallet_id_example",
        amount=133.7,
        reference=1242,
    ) # TransferCurrencyRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Transfer currency
        api_response = api_instance.transfer_currency(currency_id, x_authorization, x_password, transfer_currency_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling CurrenciesApi->transfer_currency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_id** | **str**| Any currency id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of a specific game or the &#x60;accessToken&#x60; of a specific player. |
 **x_password** | **str**| The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet. |
 **transfer_currency_request** | [**TransferCurrencyRequest**](TransferCurrencyRequest.md)|  |

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
**200** | Successfully transferred the currency amount to the provided wallet address or wallet address of the provided wallet Id. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

