# metafab_python
 Complete MetaFab API references and guides can be found at: https://trymetafab.com

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.2.0
- Package version: 1.2.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://trymetafab.com](https://trymetafab.com)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import metafab_python
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import metafab_python
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import metafab_python
from pprint import pprint
from metafab_python.api import contracts_api
from metafab_python.model.contract_model import ContractModel
from metafab_python.model.create_contract_request import CreateContractRequest
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.write_contract_request import WriteContractRequest
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)



# Enter a context with an instance of the API client
with metafab_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contracts_api.ContractsApi(api_client)
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    create_contract_request = CreateContractRequest(
        address="address_example",
        abi="abi_example",
        chain="MATIC",
    ) # CreateContractRequest | 

    try:
        # Create custom contract
        api_response = api_instance.create_contract(x_authorization, create_contract_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling ContractsApi->create_contract: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.trymetafab.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContractsApi* | [**create_contract**](docs/ContractsApi.md#create_contract) | **POST** /v1/contracts | Create custom contract
*ContractsApi* | [**get_contracts**](docs/ContractsApi.md#get_contracts) | **GET** /v1/contracts | Get contracts
*ContractsApi* | [**read_contract**](docs/ContractsApi.md#read_contract) | **GET** /v1/contracts/{contractId}/reads | Read contract data
*ContractsApi* | [**write_contract**](docs/ContractsApi.md#write_contract) | **POST** /v1/contracts/{contractId}/writes | Write contract data
*CurrenciesApi* | [**batch_transfer_currency**](docs/CurrenciesApi.md#batch_transfer_currency) | **POST** /v1/currencies/{currencyId}/batchTransfers | Batch transfer currency
*CurrenciesApi* | [**burn_currency**](docs/CurrenciesApi.md#burn_currency) | **POST** /v1/currencies/{currencyId}/burns | Burn currency
*CurrenciesApi* | [**create_currency**](docs/CurrenciesApi.md#create_currency) | **POST** /v1/currencies | Create currency
*CurrenciesApi* | [**get_currencies**](docs/CurrenciesApi.md#get_currencies) | **GET** /v1/currencies | Get currencies
*CurrenciesApi* | [**get_currency_balance**](docs/CurrenciesApi.md#get_currency_balance) | **GET** /v1/currencies/{currencyId}/balances | Get currency balance
*CurrenciesApi* | [**get_currency_fees**](docs/CurrenciesApi.md#get_currency_fees) | **GET** /v1/currencies/{currencyId}/fees | Get currency fees
*CurrenciesApi* | [**get_currency_role**](docs/CurrenciesApi.md#get_currency_role) | **GET** /v1/currencies/{currencyId}/roles | Get currency role
*CurrenciesApi* | [**grant_currency_role**](docs/CurrenciesApi.md#grant_currency_role) | **POST** /v1/currencies/{currencyId}/roles | Grant currency role
*CurrenciesApi* | [**mint_currency**](docs/CurrenciesApi.md#mint_currency) | **POST** /v1/currencies/{currencyId}/mints | Mint currency
*CurrenciesApi* | [**revoke_currency_role**](docs/CurrenciesApi.md#revoke_currency_role) | **DELETE** /v1/currencies/{currencyId}/roles | Revoke currency role
*CurrenciesApi* | [**set_currency_fees**](docs/CurrenciesApi.md#set_currency_fees) | **POST** /v1/currencies/{currencyId}/fees | Set currency fees
*CurrenciesApi* | [**transfer_currency**](docs/CurrenciesApi.md#transfer_currency) | **POST** /v1/currencies/{currencyId}/transfers | Transfer currency
*ExchangesApi* | [**create_exchange**](docs/ExchangesApi.md#create_exchange) | **POST** /v1/exchanges | Create exchange
*ExchangesApi* | [**get_exchange_offer**](docs/ExchangesApi.md#get_exchange_offer) | **GET** /v1/exchanges/{exchangeId}/items/{exchangeOfferId} | Get exchange offer
*ExchangesApi* | [**get_exchange_offers**](docs/ExchangesApi.md#get_exchange_offers) | **GET** /v1/exchanges/{exchangeId}/offers | Get exchange offers
*ExchangesApi* | [**get_exchanges**](docs/ExchangesApi.md#get_exchanges) | **GET** /v1/exchanges | Get exchanges
*ExchangesApi* | [**remove_exchange_offer**](docs/ExchangesApi.md#remove_exchange_offer) | **DELETE** /v1/exchanges/{exchangeId}/offers/{exchangeOfferId} | Remove exchange offer
*ExchangesApi* | [**set_exchange_offer**](docs/ExchangesApi.md#set_exchange_offer) | **POST** /v1/exchanges/{exchangeId}/offers | Set exchange offer
*ExchangesApi* | [**use_exchange_offer**](docs/ExchangesApi.md#use_exchange_offer) | **POST** /v1/exchanges/{exchangeId}/offers/{exchangeOfferId}/uses | Use exchange offer
*ExchangesApi* | [**withdraw_from_exchange**](docs/ExchangesApi.md#withdraw_from_exchange) | **POST** /v1/exchanges/{exchangeId}/withdrawals | Withdraw from exchange
*GamesApi* | [**auth_game**](docs/GamesApi.md#auth_game) | **GET** /v1/games/auth | Authenticate game
*GamesApi* | [**create_game**](docs/GamesApi.md#create_game) | **POST** /v1/games | Create game
*GamesApi* | [**get_game**](docs/GamesApi.md#get_game) | **GET** /v1/games/{gameId} | Get game
*GamesApi* | [**update_game**](docs/GamesApi.md#update_game) | **PATCH** /v1/games/{gameId} | Update game
*ItemsApi* | [**batch_mint_collection_items**](docs/ItemsApi.md#batch_mint_collection_items) | **POST** /v1/collections/{collectionId}/batchMints | Batch mint collection items
*ItemsApi* | [**batch_transfer_collection_items**](docs/ItemsApi.md#batch_transfer_collection_items) | **POST** /v1/collections/{collectionId}/batchTransfers | Batch transfer collection items
*ItemsApi* | [**burn_collection_item**](docs/ItemsApi.md#burn_collection_item) | **POST** /v1/collections/{collectionId}/items/{collectionItemId}/burns | Burn collection item
*ItemsApi* | [**create_collection**](docs/ItemsApi.md#create_collection) | **POST** /v1/collections | Create collection
*ItemsApi* | [**create_collection_item**](docs/ItemsApi.md#create_collection_item) | **POST** /v1/collections/{collectionId}/items | Create collection item
*ItemsApi* | [**get_collection_approval**](docs/ItemsApi.md#get_collection_approval) | **GET** /v1/collections/{collectionId}/approvals | Get collection approval
*ItemsApi* | [**get_collection_item**](docs/ItemsApi.md#get_collection_item) | **GET** /v1/collections/{collectionId}/items/{collectionItemId} | Get collection item
*ItemsApi* | [**get_collection_item_balance**](docs/ItemsApi.md#get_collection_item_balance) | **GET** /v1/collections/{collectionId}/items/{collectionItemId}/balances | Get collection item balance
*ItemsApi* | [**get_collection_item_balances**](docs/ItemsApi.md#get_collection_item_balances) | **GET** /v1/collections/{collectionId}/balances | Get collection item balances
*ItemsApi* | [**get_collection_item_supplies**](docs/ItemsApi.md#get_collection_item_supplies) | **GET** /v1/collections/{collectionId}/supplies | Get collection item supplies
*ItemsApi* | [**get_collection_item_supply**](docs/ItemsApi.md#get_collection_item_supply) | **GET** /v1/collections/{collectionId}/items/{collectionItemId}/supplies | Get collection item supply
*ItemsApi* | [**get_collection_item_timelock**](docs/ItemsApi.md#get_collection_item_timelock) | **GET** /v1/collections/{collectionId}/items/{collectionItemId}/timelocks | Get collection item timelock
*ItemsApi* | [**get_collection_items**](docs/ItemsApi.md#get_collection_items) | **GET** /v1/collections/{collectionId}/items | Get collection items
*ItemsApi* | [**get_collection_role**](docs/ItemsApi.md#get_collection_role) | **GET** /v1/collections/{collectionId}/roles | Get collection role
*ItemsApi* | [**get_collections**](docs/ItemsApi.md#get_collections) | **GET** /v1/collections | Get collections
*ItemsApi* | [**grant_collection_role**](docs/ItemsApi.md#grant_collection_role) | **POST** /v1/collections/{collectionId}/roles | Grant collection role
*ItemsApi* | [**mint_collection_item**](docs/ItemsApi.md#mint_collection_item) | **POST** /v1/collections/{collectionId}/items/{collectionItemId}/mints | Mint collection item
*ItemsApi* | [**revoke_collection_role**](docs/ItemsApi.md#revoke_collection_role) | **DELETE** /v1/collections/{collectionId}/roles | Revoke collection role
*ItemsApi* | [**set_collection_approval**](docs/ItemsApi.md#set_collection_approval) | **POST** /v1/collections/{collectionId}/approvals | Set collection approval
*ItemsApi* | [**set_collection_item_timelock**](docs/ItemsApi.md#set_collection_item_timelock) | **POST** /v1/collections/{collectionId}/items/{collectionItemId}/timelocks | Set collection item timelock
*ItemsApi* | [**transfer_collection_item**](docs/ItemsApi.md#transfer_collection_item) | **POST** /v1/collections/{collectionId}/items/{collectionItemId}/transfers | Transfer collection item
*PlayersApi* | [**auth_player**](docs/PlayersApi.md#auth_player) | **GET** /v1/players/auth | Authenticate player
*PlayersApi* | [**create_player**](docs/PlayersApi.md#create_player) | **POST** /v1/players | Create player
*PlayersApi* | [**get_player**](docs/PlayersApi.md#get_player) | **GET** /v1/players/{playerId} | Get player
*PlayersApi* | [**get_players**](docs/PlayersApi.md#get_players) | **GET** /v1/players | Get players
*PlayersApi* | [**update_player**](docs/PlayersApi.md#update_player) | **PATCH** /v1/players/{playerId} | Update player
*TransactionsApi* | [**get_transaction**](docs/TransactionsApi.md#get_transaction) | **GET** /v1/transactions/{transactionId} | Get transaction
*WalletsApi* | [**get_wallet_balances**](docs/WalletsApi.md#get_wallet_balances) | **GET** /v1/wallets/{walletId}/balances | Get wallet balances
*WalletsApi* | [**get_wallet_transactions**](docs/WalletsApi.md#get_wallet_transactions) | **GET** /v1/wallets/{walletId}/transactions | Get wallet transactions


## Documentation For Models

 - [AuthGame200Response](docs/AuthGame200Response.md)
 - [AuthGame200ResponseAllOf](docs/AuthGame200ResponseAllOf.md)
 - [AuthGame200ResponseAllOf1](docs/AuthGame200ResponseAllOf1.md)
 - [AuthPlayer200Response](docs/AuthPlayer200Response.md)
 - [BatchMintCollectionItemsRequest](docs/BatchMintCollectionItemsRequest.md)
 - [BatchTransferCollectionItemsRequest](docs/BatchTransferCollectionItemsRequest.md)
 - [BatchTransferCurrencyRequest](docs/BatchTransferCurrencyRequest.md)
 - [BurnCollectionItemRequest](docs/BurnCollectionItemRequest.md)
 - [BurnCurrencyRequest](docs/BurnCurrencyRequest.md)
 - [CollectionModel](docs/CollectionModel.md)
 - [ContractModel](docs/ContractModel.md)
 - [CreateCollection200Response](docs/CreateCollection200Response.md)
 - [CreateCollection200ResponseAllOf](docs/CreateCollection200ResponseAllOf.md)
 - [CreateCollection200ResponseAllOfContract](docs/CreateCollection200ResponseAllOfContract.md)
 - [CreateCollection200ResponseAllOfContractAllOf](docs/CreateCollection200ResponseAllOfContractAllOf.md)
 - [CreateCollectionItemRequest](docs/CreateCollectionItemRequest.md)
 - [CreateCollectionItemRequestAttributesInner](docs/CreateCollectionItemRequestAttributesInner.md)
 - [CreateCollectionRequest](docs/CreateCollectionRequest.md)
 - [CreateContractRequest](docs/CreateContractRequest.md)
 - [CreateCurrency200Response](docs/CreateCurrency200Response.md)
 - [CreateCurrencyRequest](docs/CreateCurrencyRequest.md)
 - [CreateExchange200Response](docs/CreateExchange200Response.md)
 - [CreateExchangeRequest](docs/CreateExchangeRequest.md)
 - [CreateGameRequest](docs/CreateGameRequest.md)
 - [CreatePlayerRequest](docs/CreatePlayerRequest.md)
 - [CurrencyModel](docs/CurrencyModel.md)
 - [ExchangeModel](docs/ExchangeModel.md)
 - [ExchangeOffer](docs/ExchangeOffer.md)
 - [GameModel](docs/GameModel.md)
 - [GetCollections200ResponseInner](docs/GetCollections200ResponseInner.md)
 - [GetCollections200ResponseInnerAllOf](docs/GetCollections200ResponseInnerAllOf.md)
 - [GetCurrencies200ResponseInner](docs/GetCurrencies200ResponseInner.md)
 - [GetCurrencies200ResponseInnerAllOf](docs/GetCurrencies200ResponseInnerAllOf.md)
 - [GetCurrencyFees200Response](docs/GetCurrencyFees200Response.md)
 - [GetExchanges200ResponseInner](docs/GetExchanges200ResponseInner.md)
 - [GrantCollectionRoleRequest](docs/GrantCollectionRoleRequest.md)
 - [GrantCurrencyRoleRequest](docs/GrantCurrencyRoleRequest.md)
 - [MintCollectionItemRequest](docs/MintCollectionItemRequest.md)
 - [MintCurrencyRequest](docs/MintCurrencyRequest.md)
 - [PlayerModel](docs/PlayerModel.md)
 - [PublicGame](docs/PublicGame.md)
 - [PublicPlayer](docs/PublicPlayer.md)
 - [PublicPlayerWallet](docs/PublicPlayerWallet.md)
 - [RevokeCollectionRoleRequest](docs/RevokeCollectionRoleRequest.md)
 - [SetCollectionApprovalRequest](docs/SetCollectionApprovalRequest.md)
 - [SetCollectionItemTimelockRequest](docs/SetCollectionItemTimelockRequest.md)
 - [SetCurrencyFeesRequest](docs/SetCurrencyFeesRequest.md)
 - [SetExchangeOfferRequest](docs/SetExchangeOfferRequest.md)
 - [TransactionModel](docs/TransactionModel.md)
 - [TransferCollectionItemRequest](docs/TransferCollectionItemRequest.md)
 - [TransferCurrencyRequest](docs/TransferCurrencyRequest.md)
 - [UpdateGameRequest](docs/UpdateGameRequest.md)
 - [UpdatePlayerRequest](docs/UpdatePlayerRequest.md)
 - [WalletModel](docs/WalletModel.md)
 - [WithdrawFromExchangeRequest](docs/WithdrawFromExchangeRequest.md)
 - [WriteContractRequest](docs/WriteContractRequest.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author

metafabproject@gmail.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in metafab_python.apis and metafab_python.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from metafab_python.api.default_api import DefaultApi`
- `from metafab_python.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import metafab_python
from metafab_python.apis import *
from metafab_python.models import *
```

