# metafab_python.WalletsApi

All URIs are relative to *https://api.trymetafab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_wallet_signature**](WalletsApi.md#create_wallet_signature) | **POST** /v1/wallets/{walletId}/signatures | Create wallet signature
[**get_wallet**](WalletsApi.md#get_wallet) | **GET** /v1/wallets/{walletId} | Get wallet
[**get_wallet_balances**](WalletsApi.md#get_wallet_balances) | **GET** /v1/wallets/{walletId}/balances | Get wallet balances
[**get_wallet_transactions**](WalletsApi.md#get_wallet_transactions) | **GET** /v1/wallets/{walletId}/transactions | Get wallet transactions


# **create_wallet_signature**
> str create_wallet_signature(wallet_id, x_wallet_decrypt_key, create_wallet_signature_request)

Create wallet signature

Creates a wallet signature from a plaintext message using the wallet for the provided walletId and walletDecryptKey. Wallet signatures cannot be generated for EOA wallets.

### Example


```python
import time
import metafab_python
from metafab_python.api import wallets_api
from metafab_python.model.create_wallet_signature_request import CreateWalletSignatureRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = wallets_api.WalletsApi(api_client)
    wallet_id = "walletId_example" # str | Any wallet id within the MetaFab platform.
    x_wallet_decrypt_key = "AXNP8MKb+5SbBtHWrZu5KHh5/BomXY/dMRG/BDUn7a4=" # str | The `walletDecryptKey` for the provided `walletId`.
    create_wallet_signature_request = CreateWalletSignatureRequest(
        message="message_example",
    ) # CreateWalletSignatureRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create wallet signature
        api_response = api_instance.create_wallet_signature(wallet_id, x_wallet_decrypt_key, create_wallet_signature_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling WalletsApi->create_wallet_signature: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Any wallet id within the MetaFab platform. |
 **x_wallet_decrypt_key** | **str**| The &#x60;walletDecryptKey&#x60; for the provided &#x60;walletId&#x60;. |
 **create_wallet_signature_request** | [**CreateWalletSignatureRequest**](CreateWalletSignatureRequest.md)|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a wallet signature from the provided message using the provided wallet. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet**
> WalletModel get_wallet(wallet_id)

Get wallet

Returns a wallet object for the provided walletId.

### Example


```python
import time
import metafab_python
from metafab_python.api import wallets_api
from metafab_python.model.wallet_model import WalletModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = wallets_api.WalletsApi(api_client)
    wallet_id = "walletId_example" # str | Any wallet id within the MetaFab platform.

    # example passing only required values which don't have defaults set
    try:
        # Get wallet
        api_response = api_instance.get_wallet(wallet_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling WalletsApi->get_wallet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Any wallet id within the MetaFab platform. |

### Return type

[**WalletModel**](WalletModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved a wallet object for the provided walletId. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet_balances**
> {str: (float,)} get_wallet_balances(wallet_id)

Get wallet balances

Returns the current native token balance for all chains supported by MetaFab for the provided walletId. This includes balances like Eth, Matic and other native tokens from chains MetaFab supports.

### Example


```python
import time
import metafab_python
from metafab_python.api import wallets_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = wallets_api.WalletsApi(api_client)
    wallet_id = "walletId_example" # str | Any wallet id within the MetaFab platform.

    # example passing only required values which don't have defaults set
    try:
        # Get wallet balances
        api_response = api_instance.get_wallet_balances(wallet_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling WalletsApi->get_wallet_balances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Any wallet id within the MetaFab platform. |

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
**200** | Successfully retrieved native token balances of the provided walletId&#39;s address for each chain supported by MetaFab. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet_transactions**
> [TransactionModel] get_wallet_transactions(wallet_id)

Get wallet transactions

Returns an array of MetaFab initiated transactions performed by the provided walletId. Transactions returned are ordered chronologically from newest to oldest.

### Example


```python
import time
import metafab_python
from metafab_python.api import wallets_api
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
    api_instance = wallets_api.WalletsApi(api_client)
    wallet_id = "walletId_example" # str | Any wallet id within the MetaFab platform.

    # example passing only required values which don't have defaults set
    try:
        # Get wallet transactions
        api_response = api_instance.get_wallet_transactions(wallet_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling WalletsApi->get_wallet_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Any wallet id within the MetaFab platform. |

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
**200** | Successfully retrieved an array of transactions performed by the provided walletId. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

