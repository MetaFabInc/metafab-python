# metafab_python.ContractsApi

All URIs are relative to *https://api.trymetafab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contract**](ContractsApi.md#create_contract) | **POST** /v1/contracts | Create custom contract
[**get_contracts**](ContractsApi.md#get_contracts) | **GET** /v1/contracts | Get contracts
[**read_contract**](ContractsApi.md#read_contract) | **GET** /v1/contracts/{contractId}/reads | Read contract data
[**transfer_contract_ownership**](ContractsApi.md#transfer_contract_ownership) | **POST** /v1/contracts/{contractId}/owners | Transfer contract ownership
[**upgrade_contract_trusted_forwarder**](ContractsApi.md#upgrade_contract_trusted_forwarder) | **POST** /v1/contracts/{contractId}/forwarders | Upgrade contract trusted forwarder
[**write_contract**](ContractsApi.md#write_contract) | **POST** /v1/contracts/{contractId}/writes | Write contract data


# **create_contract**
> ContractModel create_contract(x_authorization, create_contract_request)

Create custom contract

Create a MetaFab custom contract entry from an existing contract address and contract abi. This allows the game and players belonging to the authenticated game to interact with the contract's read and write functions through MetaFab's read and write contract endpoints.

### Example


```python
import time
import metafab_python
from metafab_python.api import contracts_api
from metafab_python.model.contract_model import ContractModel
from metafab_python.model.create_contract_request import CreateContractRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = contracts_api.ContractsApi(api_client)
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    create_contract_request = CreateContractRequest(
        address="address_example",
        forwarder_address="forwarder_address_example",
        abi="abi_example",
        chain="SELECT ONE",
    ) # CreateContractRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create custom contract
        api_response = api_instance.create_contract(x_authorization, create_contract_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ContractsApi->create_contract: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **create_contract_request** | [**CreateContractRequest**](CreateContractRequest.md)|  |

### Return type

[**ContractModel**](ContractModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a MetaFab contract entry. Returns a contract object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contracts**
> [ContractModel] get_contracts(x_game_key)

Get contracts

Returns an array of active contracts deployed by the game associated with the provided `X-Game-Key`.

### Example


```python
import time
import metafab_python
from metafab_python.api import contracts_api
from metafab_python.model.contract_model import ContractModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = contracts_api.ContractsApi(api_client)
    x_game_key = "game_pk_4SOqpDi8pQdnQgfCOBW29qR8YmwOhxVPz5iHoMgUEJLDdPXgwLuHqZf8ewo2GajZ" # str | The `publishedKey` of a specific game. This can be shared or included in game clients, websites, etc.

    # example passing only required values which don't have defaults set
    try:
        # Get contracts
        api_response = api_instance.get_contracts(x_game_key)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ContractsApi->get_contracts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_game_key** | **str**| The &#x60;publishedKey&#x60; of a specific game. This can be shared or included in game clients, websites, etc. |

### Return type

[**[ContractModel]**](ContractModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved an array of contracts for the game associated with the provided &#x60;X-Game-Key&#x60;. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_contract**
> bool, date, datetime, dict, float, int, list, str, none_type read_contract(contract_id, func)

Read contract data

Oftentimes you'll want to query and retrieve some data from a contract. This is incredibly easy to do for any contract deployed through MetaFab.  Using this endpoint, you can get the data returned by any readable function listed in a contracts ABI. This could be things like querying the totalSupply of a currency contract, the number of owners of an items contract, and more.

### Example


```python
import time
import metafab_python
from metafab_python.api import contracts_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = contracts_api.ContractsApi(api_client)
    contract_id = "contractId_example" # str | Any contract id within the MetaFab platform.
    func = "func_example" # str | A contract function name. This can be any valid function from the the ABI of the contract you are interacting with. For example, `balanceOf`.
    args = "123,"Hello",false" # str | A comma seperated list of basic data type arguments. This is optional and only necessary if the function being invoked requires arguments per the contract ABI. For example, `123,\"Hello\",false`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Read contract data
        api_response = api_instance.read_contract(contract_id, func)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ContractsApi->read_contract: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read contract data
        api_response = api_instance.read_contract(contract_id, func, args=args)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ContractsApi->read_contract: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Any contract id within the MetaFab platform. |
 **func** | **str**| A contract function name. This can be any valid function from the the ABI of the contract you are interacting with. For example, &#x60;balanceOf&#x60;. |
 **args** | **str**| A comma seperated list of basic data type arguments. This is optional and only necessary if the function being invoked requires arguments per the contract ABI. For example, &#x60;123,\&quot;Hello\&quot;,false&#x60;. | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved value returned by contract function. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_contract_ownership**
> TransactionModel transfer_contract_ownership(contract_id, x_authorization, x_wallet_decrypt_key, transfer_contract_ownership_request)

Transfer contract ownership

Transfer ownership and control of a MetaFab deployed smart contract to another wallet you control. Transferring control does not disrupt your usage of MetaFab APIs and can be done so without causing any service outages for your game. The new owner wallet will have full control over any relevant item collections and marketplace related pages this contract may be associated with, such as for MetaFab item or NFT contracts.  Your game's custodial wallet will retain a `MANAGER_ROLE` on your contracts, allowing you to still use MetaFab APIs without issue while you retain full contract ownership and the contract's administrator role. If ever you want eject from using the MetaFab APIs but still retain your deployed smart contracts, you can revoke the `MANAGER_ROLE` from your game's custodial wallet address for your contract. We do not lock you into our systems.  Please be certain that the wallet address you transfer ownership to is one you control. Once ownership and admin permissions are transferred, your game's custodial wallet no longer has permission to reassign ownership or administrative priveleges for your contract.

### Example


```python
import time
import metafab_python
from metafab_python.api import contracts_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.transfer_contract_ownership_request import TransferContractOwnershipRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = contracts_api.ContractsApi(api_client)
    contract_id = "contractId_example" # str | Any contract id within the MetaFab platform.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_wallet_decrypt_key = "AXNP8MKb+5SbBtHWrZu5KHh5/BomXY/dMRG/BDUn7a4=" # str | The `walletDecryptKey` of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    transfer_contract_ownership_request = TransferContractOwnershipRequest(
        owner_address="owner_address_example",
    ) # TransferContractOwnershipRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Transfer contract ownership
        api_response = api_instance.transfer_contract_ownership(contract_id, x_authorization, x_wallet_decrypt_key, transfer_contract_ownership_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ContractsApi->transfer_contract_ownership: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Any contract id within the MetaFab platform. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_wallet_decrypt_key** | **str**| The &#x60;walletDecryptKey&#x60; of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **transfer_contract_ownership_request** | [**TransferContractOwnershipRequest**](TransferContractOwnershipRequest.md)|  |

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
**200** | Successfully transferred ownership of the target contract. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_contract_trusted_forwarder**
> TransactionModel upgrade_contract_trusted_forwarder(contract_id, x_authorization, x_wallet_decrypt_key, upgrade_contract_trusted_forwarder_request)

Upgrade contract trusted forwarder

In rare circumstances, you may need to upgrade the underlying trusted forwarder contract address attached to your game's contracts. Using this endpoint, you can provide a new trusted forwarder contract address to assign to any of your contracts that implement the `upgradeTrustedForwarder` function.

### Example


```python
import time
import metafab_python
from metafab_python.api import contracts_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.upgrade_contract_trusted_forwarder_request import UpgradeContractTrustedForwarderRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = contracts_api.ContractsApi(api_client)
    contract_id = "contractId_example" # str | Any contract id within the MetaFab platform.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    x_wallet_decrypt_key = "AXNP8MKb+5SbBtHWrZu5KHh5/BomXY/dMRG/BDUn7a4=" # str | The `walletDecryptKey` of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet.
    upgrade_contract_trusted_forwarder_request = UpgradeContractTrustedForwarderRequest(
        forwarder_address="forwarder_address_example",
    ) # UpgradeContractTrustedForwarderRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Upgrade contract trusted forwarder
        api_response = api_instance.upgrade_contract_trusted_forwarder(contract_id, x_authorization, x_wallet_decrypt_key, upgrade_contract_trusted_forwarder_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ContractsApi->upgrade_contract_trusted_forwarder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Any contract id within the MetaFab platform. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **x_wallet_decrypt_key** | **str**| The &#x60;walletDecryptKey&#x60; of the authenticating game. Required to decrypt and perform blockchain transactions with the game primary wallet. |
 **upgrade_contract_trusted_forwarder_request** | [**UpgradeContractTrustedForwarderRequest**](UpgradeContractTrustedForwarderRequest.md)|  |

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
**200** | Successfully upgraded the trusted forwarder for the target contract. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **write_contract**
> TransactionModel write_contract(contract_id, x_authorization, x_wallet_decrypt_key, write_contract_request)

Write contract data

MetaFab's convenience endpoints for contract interactions may not be flexible enough depending on your use case. For these situations, you can interact with contracts and create transactions directly.  Using this endpoint, you can execute a transaction for any writeable contract method as defined in the contract's ABI for the MetaFab contractId provided. Both Games and Player resources have authority to use this endpoint to execute transactions against any valid MetaFab contractId.  Additionally, MetaFab will automatically attempt to perform a gasless transaction for players interacting with a contract through this endpoint. Gasless transactions by players through this endpoint will only work if the target contract was deployed through MetaFab or supports MetaFab's ERC2771 trusted forwarder contract.

### Example


```python
import time
import metafab_python
from metafab_python.api import contracts_api
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.write_contract_request import WriteContractRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = contracts_api.ContractsApi(api_client)
    contract_id = "contractId_example" # str | Any contract id within the MetaFab platform.
    x_authorization = "["game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP","player_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP"]" # str | The `secretKey` of a specific game or the `accessToken` of a specific player.
    x_wallet_decrypt_key = "AXNP8MKb+5SbBtHWrZu5KHh5/BomXY/dMRG/BDUn7a4=" # str | The `walletDecryptKey` of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet.
    write_contract_request = WriteContractRequest(
        func="func_example",
        args=[
            WriteContractRequestArgsInner(None),
        ],
    ) # WriteContractRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Write contract data
        api_response = api_instance.write_contract(contract_id, x_authorization, x_wallet_decrypt_key, write_contract_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ContractsApi->write_contract: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Any contract id within the MetaFab platform. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of a specific game or the &#x60;accessToken&#x60; of a specific player. |
 **x_wallet_decrypt_key** | **str**| The &#x60;walletDecryptKey&#x60; of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet. |
 **write_contract_request** | [**WriteContractRequest**](WriteContractRequest.md)|  |

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
**200** | Successfully executed and confirmed the transaction. Returns a transaction object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

