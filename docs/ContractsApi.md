# metafab_python.ContractsApi

All URIs are relative to *https://api.trymetafab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contract**](ContractsApi.md#create_contract) | **POST** /v1/contracts | Create custom contract
[**get_contracts**](ContractsApi.md#get_contracts) | **GET** /v1/contracts | Get contracts
[**read_contract**](ContractsApi.md#read_contract) | **GET** /v1/contracts/{contractId}/reads | Read contract data
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
    contract_id = "contractId_example" # str | Any contract id within the MetaFab ecosystem.
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
 **contract_id** | **str**| Any contract id within the MetaFab ecosystem. |
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

# **write_contract**
> TransactionModel write_contract(contract_id, x_authorization, x_password, write_contract_request)

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
    contract_id = "contractId_example" # str | Any contract id within the MetaFab ecosystem.
    x_authorization = "["game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP","player_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP"]" # str | The `secretKey` of a specific game or the `accessToken` of a specific player.
    x_password = "mySecurePassword" # str | The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet.
    write_contract_request = WriteContractRequest(
        func="func_example",
        args="args_example",
    ) # WriteContractRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Write contract data
        api_response = api_instance.write_contract(contract_id, x_authorization, x_password, write_contract_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ContractsApi->write_contract: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| Any contract id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of a specific game or the &#x60;accessToken&#x60; of a specific player. |
 **x_password** | **str**| The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet. |
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

