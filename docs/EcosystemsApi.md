# metafab_python.EcosystemsApi

All URIs are relative to *https://api.trymetafab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_ecosystem_game**](EcosystemsApi.md#approve_ecosystem_game) | **POST** /v1/ecosystems/{ecosystemId}/games | Approve ecosystem game
[**auth_ecosystem**](EcosystemsApi.md#auth_ecosystem) | **GET** /v1/ecosystems/auth | Authenticate ecosystem
[**auth_profile**](EcosystemsApi.md#auth_profile) | **GET** /v1/profiles/auth | Authenticate profile
[**auth_profile_player**](EcosystemsApi.md#auth_profile_player) | **GET** /v1/profiles/{profileId}/games/{gameId}/players/auth | Authenticate profile player
[**create_ecosystem**](EcosystemsApi.md#create_ecosystem) | **POST** /v1/ecosystems | Create ecosystem
[**create_profile**](EcosystemsApi.md#create_profile) | **POST** /v1/profiles | Create profile
[**create_profile_player**](EcosystemsApi.md#create_profile_player) | **POST** /v1/profiles/{profileId}/games/{gameId}/players | Create profile player
[**get_ecosystem**](EcosystemsApi.md#get_ecosystem) | **GET** /v1/ecosystems/{ecosystemId} | Get ecosystem
[**get_ecosystem_game**](EcosystemsApi.md#get_ecosystem_game) | **GET** /v1/ecosystems/{ecosystemId}/games/{gameId} | Get ecosystem game
[**get_ecosystem_games**](EcosystemsApi.md#get_ecosystem_games) | **GET** /v1/ecosystems/{ecosystemId}/games | Get ecosystem games
[**get_profile_game**](EcosystemsApi.md#get_profile_game) | **GET** /v1/profiles/{profileId}/games/{gameId} | Get profile game
[**get_profile_games**](EcosystemsApi.md#get_profile_games) | **GET** /v1/profiles/{profileId}/games | Get profile games
[**unapprove_ecosystem_game**](EcosystemsApi.md#unapprove_ecosystem_game) | **DELETE** /v1/ecosystems/{ecosystemId}/games/{gameId} | Unapprove ecosystem game
[**update_ecosystem**](EcosystemsApi.md#update_ecosystem) | **PATCH** /v1/ecosystems/{ecosystemId} | Update ecosystem
[**update_profile**](EcosystemsApi.md#update_profile) | **PATCH** /v1/profiles/{profileId} | Update profile
[**update_profile_player**](EcosystemsApi.md#update_profile_player) | **PATCH** /v1/profiles/{profileId}/games/{gameId}/players/{playerId} | Update profile player


# **approve_ecosystem_game**
> approve_ecosystem_game(ecosystem_id, x_authorization, approve_ecosystem_game_request)

Approve ecosystem game

Approves a game for an ecosystem. By approving a game, it allows that game to integrate the ability for profile accounts from an ecosystem to login directly to the approved game and play. This also allows games to request access to assets held at the profile level for the game to frictionlessly interact with on behalf of the profile.

### Example


```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from metafab_python.model.approve_ecosystem_game_request import ApproveEcosystemGameRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)
    ecosystem_id = "ecosystemId_example" # str | The ecosystem id of the authenticating ecosystem.
    x_authorization = "ecosystem_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating ecosystem.
    approve_ecosystem_game_request = ApproveEcosystemGameRequest(
        game_id="game_id_example",
    ) # ApproveEcosystemGameRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Approve ecosystem game
        api_instance.approve_ecosystem_game(ecosystem_id, x_authorization, approve_ecosystem_game_request)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->approve_ecosystem_game: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ecosystem_id** | **str**| The ecosystem id of the authenticating ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating ecosystem. |
 **approve_ecosystem_game_request** | [**ApproveEcosystemGameRequest**](ApproveEcosystemGameRequest.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully approved the game for the ecosystem. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_ecosystem**
> EcosystemModel auth_ecosystem()

Authenticate ecosystem

Returns an existing ecosystem object containing authorization keys when provided a valid email (in place of username) and password login using Basic Auth.

### Example

* Basic Authentication (basicAuth):

```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from metafab_python.model.ecosystem_model import EcosystemModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = metafab_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with metafab_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Authenticate ecosystem
        api_response = api_instance.auth_ecosystem()
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->auth_ecosystem: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**EcosystemModel**](EcosystemModel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully authorized the request and retrieved an ecosystem object containing authorization keys and credentials. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_profile**
> AuthProfile200Response auth_profile(x_ecosystem_key)

Authenticate profile

Returns an existing profile object containing access token, wallet, and other details when provided a valid profile username and password login using Basic Auth.

### Example

* Basic Authentication (basicAuth):

```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from metafab_python.model.auth_profile200_response import AuthProfile200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = metafab_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with metafab_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)
    x_ecosystem_key = "ecosystem_pk_a5sFpDi8pQdnQgfCOBW29qR8YmwOhxVPz5iHoMgUEJLDdPXgwLuHqZf8ewo2GajZ" # str | The `publishedKey` of a specific ecosystem. This can be shared or included in clients, websites, etc.

    # example passing only required values which don't have defaults set
    try:
        # Authenticate profile
        api_response = api_instance.auth_profile(x_ecosystem_key)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->auth_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ecosystem_key** | **str**| The &#x60;publishedKey&#x60; of a specific ecosystem. This can be shared or included in clients, websites, etc. |

### Return type

[**AuthProfile200Response**](AuthProfile200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully authorized the request and retrieved a profile object containing access token, wallet, and other details. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_profile_player**
> AuthPlayer200Response auth_profile_player(profile_id, game_id, x_authorization, x_wallet_decrypt_key, x_username)

Authenticate profile player

Returns an existing player object containing access token, wallet, wallet decrypt key, profile authorization and other details for a game when provided profile authentication and the player's username.

### Example


```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from metafab_python.model.auth_player200_response import AuthPlayer200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)
    profile_id = "profileId_example" # str | The profile id of the authenticating profile.
    game_id = "gameId_example" # str | Any game id within the MetaFab platform.
    x_authorization = "profile_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `accessToken` of the authenticating profile.
    x_wallet_decrypt_key = "AXNP8MKb+5SbBtHWrZu5KHh5/BomXY/dMRG/BDUn7a4=" # str | The `walletDecryptKey` of the authenticating profile. Required to decrypt and perform blockchain transactions with the profile wallet.
    x_username = "arkdev" # str | The username of a player.

    # example passing only required values which don't have defaults set
    try:
        # Authenticate profile player
        api_response = api_instance.auth_profile_player(profile_id, game_id, x_authorization, x_wallet_decrypt_key, x_username)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->auth_profile_player: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The profile id of the authenticating profile. |
 **game_id** | **str**| Any game id within the MetaFab platform. |
 **x_authorization** | **str**| The &#x60;accessToken&#x60; of the authenticating profile. |
 **x_wallet_decrypt_key** | **str**| The &#x60;walletDecryptKey&#x60; of the authenticating profile. Required to decrypt and perform blockchain transactions with the profile wallet. |
 **x_username** | **str**| The username of a player. |

### Return type

[**AuthPlayer200Response**](AuthPlayer200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully authorized the request and retrieved a player object containing access token, wallet, profile authorization, and other details. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ecosystem**
> EcosystemModel create_ecosystem(create_ecosystem_request)

Create ecosystem

Create a new ecosystem. An ecosystem is a parent entity that many profiles live under for a given ecosystem of games. Ecosystems allow your players to create one profile within your ecosystem that allows a single account and wallet to be used across all of the approved games in your ecosystem that they play.

### Example


```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from metafab_python.model.create_ecosystem_request import CreateEcosystemRequest
from metafab_python.model.ecosystem_model import EcosystemModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)
    create_ecosystem_request = CreateEcosystemRequest(
        name="NFT Worlds",
        email="dev@nftworlds.com",
        password="aReallyStrongPassword123!",
    ) # CreateEcosystemRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create ecosystem
        api_response = api_instance.create_ecosystem(create_ecosystem_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->create_ecosystem: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_ecosystem_request** | [**CreateEcosystemRequest**](CreateEcosystemRequest.md)|  |

### Return type

[**EcosystemModel**](EcosystemModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new ecosystem. Returns an ecosystem object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_profile**
> AuthProfile200Response create_profile(x_ecosystem_key, create_profile_request)

Create profile

Create a new profile. Profiles are automatically associated with an internally managed wallet. Profiles can be thought of as a umbrella account that can be used to sign into and create player accounts across many games and have a singular asset store wallet at the profile level that can be used across all connected player accounts for games those player accounts are a part of.  Profiles are associated to a parent ecosystem of games. This allows an ecosystem to approve a permissioned set of games that can request authorized wallet permissions from profiles of players for their game.

### Example


```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from metafab_python.model.create_profile_request import CreateProfileRequest
from metafab_python.model.auth_profile200_response import AuthProfile200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)
    x_ecosystem_key = "ecosystem_pk_a5sFpDi8pQdnQgfCOBW29qR8YmwOhxVPz5iHoMgUEJLDdPXgwLuHqZf8ewo2GajZ" # str | The `publishedKey` of a specific ecosystem. This can be shared or included in clients, websites, etc.
    create_profile_request = CreateProfileRequest(
        username="username_example",
        password="aReallyStrongPassword123",
    ) # CreateProfileRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create profile
        api_response = api_instance.create_profile(x_ecosystem_key, create_profile_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->create_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_ecosystem_key** | **str**| The &#x60;publishedKey&#x60; of a specific ecosystem. This can be shared or included in clients, websites, etc. |
 **create_profile_request** | [**CreateProfileRequest**](CreateProfileRequest.md)|  |

### Return type

[**AuthProfile200Response**](AuthProfile200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new profile. Returns a profile object containing a wallet (used to interact with contracts, currencies, etc). |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_profile_player**
> AuthPlayer200Response create_profile_player(profile_id, game_id, x_authorization, x_wallet_decrypt_key, create_profile_player_request)

Create profile player

Creates a new player account for the provided game id linked to the authenticating profile. The created player account will default to using the parent profile's wallet for any transactions, wallet content balance checks and verifications, and more.

### Example


```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from metafab_python.model.create_profile_player_request import CreateProfilePlayerRequest
from metafab_python.model.auth_player200_response import AuthPlayer200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)
    profile_id = "profileId_example" # str | The profile id of the authenticating profile.
    game_id = "gameId_example" # str | Any game id within the MetaFab platform.
    x_authorization = "profile_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `accessToken` of the authenticating profile.
    x_wallet_decrypt_key = "AXNP8MKb+5SbBtHWrZu5KHh5/BomXY/dMRG/BDUn7a4=" # str | The `walletDecryptKey` of the authenticating profile. Required to decrypt and perform blockchain transactions with the profile wallet.
    create_profile_player_request = CreateProfilePlayerRequest(
        username="username_example",
        permissions=ProfilePermissions(
            key=ProfilePermissionsValue(
                chain="chain_example",
                scopes=[
                    "scopes_example",
                ],
                functions=[
                    "functions_example",
                ],
                erc20_limit=1,
                erc1155_limits={
                    "key": 1,
                },
            ),
        ),
    ) # CreateProfilePlayerRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create profile player
        api_response = api_instance.create_profile_player(profile_id, game_id, x_authorization, x_wallet_decrypt_key, create_profile_player_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->create_profile_player: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The profile id of the authenticating profile. |
 **game_id** | **str**| Any game id within the MetaFab platform. |
 **x_authorization** | **str**| The &#x60;accessToken&#x60; of the authenticating profile. |
 **x_wallet_decrypt_key** | **str**| The &#x60;walletDecryptKey&#x60; of the authenticating profile. Required to decrypt and perform blockchain transactions with the profile wallet. |
 **create_profile_player_request** | [**CreateProfilePlayerRequest**](CreateProfilePlayerRequest.md)|  |

### Return type

[**AuthPlayer200Response**](AuthPlayer200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new player linked to the authenticating profile. Returns a player object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ecosystem**
> PublicEcosystem get_ecosystem(ecosystem_id)

Get ecosystem

Returns a ecosystem object for the provided ecosystem id.

### Example


```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from metafab_python.model.public_ecosystem import PublicEcosystem
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)
    ecosystem_id = "ecosystemId_example" # str | Any ecosystem id within the MetaFab platform.

    # example passing only required values which don't have defaults set
    try:
        # Get ecosystem
        api_response = api_instance.get_ecosystem(ecosystem_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->get_ecosystem: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ecosystem_id** | **str**| Any ecosystem id within the MetaFab platform. |

### Return type

[**PublicEcosystem**](PublicEcosystem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved ecosystem. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ecosystem_game**
> PublicGame get_ecosystem_game(ecosystem_id, game_id)

Get ecosystem game

Returns a game object for the provided game id that the ecosystem has approved.

### Example


```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from metafab_python.model.public_game import PublicGame
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)
    ecosystem_id = "ecosystemId_example" # str | Any ecosystem id within the MetaFab platform.
    game_id = "gameId_example" # str | Any game id within the MetaFab platform.

    # example passing only required values which don't have defaults set
    try:
        # Get ecosystem game
        api_response = api_instance.get_ecosystem_game(ecosystem_id, game_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->get_ecosystem_game: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ecosystem_id** | **str**| Any ecosystem id within the MetaFab platform. |
 **game_id** | **str**| Any game id within the MetaFab platform. |

### Return type

[**PublicGame**](PublicGame.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved an approved game. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ecosystem_games**
> [PublicGame] get_ecosystem_games(ecosystem_id)

Get ecosystem games

Returns an array of games the ecosystem has approved.

### Example


```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from metafab_python.model.public_game import PublicGame
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)
    ecosystem_id = "ecosystemId_example" # str | Any ecosystem id within the MetaFab platform.

    # example passing only required values which don't have defaults set
    try:
        # Get ecosystem games
        api_response = api_instance.get_ecosystem_games(ecosystem_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->get_ecosystem_games: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ecosystem_id** | **str**| Any ecosystem id within the MetaFab platform. |

### Return type

[**[PublicGame]**](PublicGame.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved an array of approved games. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_game**
> GetProfileGames200ResponseInner get_profile_game(profile_id, game_id, x_authorization)

Get profile game

Returns a game this profile has connected player accounts for.

### Example


```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from metafab_python.model.get_profile_games200_response_inner import GetProfileGames200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)
    profile_id = "profileId_example" # str | The profile id of the authenticating profile.
    game_id = "gameId_example" # str | Any game id within the MetaFab platform.
    x_authorization = "profile_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `accessToken` of the authenticating profile.

    # example passing only required values which don't have defaults set
    try:
        # Get profile game
        api_response = api_instance.get_profile_game(profile_id, game_id, x_authorization)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->get_profile_game: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The profile id of the authenticating profile. |
 **game_id** | **str**| Any game id within the MetaFab platform. |
 **x_authorization** | **str**| The &#x60;accessToken&#x60; of the authenticating profile. |

### Return type

[**GetProfileGames200ResponseInner**](GetProfileGames200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved array of games this profile has connected player accounts for. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_games**
> [GetProfileGames200ResponseInner] get_profile_games(profile_id, x_authorization)

Get profile games

Returns an array of games the authorized profile has connected player accounts for.

### Example


```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from metafab_python.model.get_profile_games200_response_inner import GetProfileGames200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)
    profile_id = "profileId_example" # str | The profile id of the authenticating profile.
    x_authorization = "profile_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `accessToken` of the authenticating profile.

    # example passing only required values which don't have defaults set
    try:
        # Get profile games
        api_response = api_instance.get_profile_games(profile_id, x_authorization)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->get_profile_games: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The profile id of the authenticating profile. |
 **x_authorization** | **str**| The &#x60;accessToken&#x60; of the authenticating profile. |

### Return type

[**[GetProfileGames200ResponseInner]**](GetProfileGames200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved array of games this profile has connected player accounts for. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unapprove_ecosystem_game**
> unapprove_ecosystem_game(ecosystem_id, game_id, x_authorization)

Unapprove ecosystem game

Unapproves a game for an ecosystem. The game will no longer be able to allow profiles from the ecosystem to login. All profile permissions approved for the game will also be revoked.

### Example


```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)
    ecosystem_id = "ecosystemId_example" # str | The ecosystem id of the authenticating ecosystem.
    game_id = "gameId_example" # str | Any game id within the MetaFab platform.
    x_authorization = "ecosystem_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating ecosystem.

    # example passing only required values which don't have defaults set
    try:
        # Unapprove ecosystem game
        api_instance.unapprove_ecosystem_game(ecosystem_id, game_id, x_authorization)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->unapprove_ecosystem_game: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ecosystem_id** | **str**| The ecosystem id of the authenticating ecosystem. |
 **game_id** | **str**| Any game id within the MetaFab platform. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating ecosystem. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully approved the game for the ecosystem. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ecosystem**
> EcosystemModel update_ecosystem(ecosystem_id, x_authorization, update_ecosystem_request)

Update ecosystem

Update various fields specific to an ecosystem. Such as changing its password, resetting its published or secret key, or updating its approved games.

### Example


```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from metafab_python.model.update_ecosystem_request import UpdateEcosystemRequest
from metafab_python.model.ecosystem_model import EcosystemModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)
    ecosystem_id = "ecosystemId_example" # str | The ecosystem id of the authenticating ecosystem.
    x_authorization = "ecosystem_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating ecosystem.
    update_ecosystem_request = UpdateEcosystemRequest(
        name="name_example",
        email="email_example",
        current_password="current_password_example",
        new_password="new_password_example",
        icon_image_base64="icon_image_base64_example",
        cover_image_base64="cover_image_base64_example",
        primary_color_hex="primary_color_hex_example",
        reset_published_key=True,
        reset_secret_key=True,
    ) # UpdateEcosystemRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update ecosystem
        api_response = api_instance.update_ecosystem(ecosystem_id, x_authorization, update_ecosystem_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->update_ecosystem: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ecosystem_id** | **str**| The ecosystem id of the authenticating ecosystem. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating ecosystem. |
 **update_ecosystem_request** | [**UpdateEcosystemRequest**](UpdateEcosystemRequest.md)|  |

### Return type

[**EcosystemModel**](EcosystemModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated ecosystem object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> ProfileModel update_profile(profile_id, x_authorization, update_profile_request)

Update profile

Update various fields specific to a profile. Such as changing its password and resetting its access token.

### Example


```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from metafab_python.model.update_profile_request import UpdateProfileRequest
from metafab_python.model.profile_model import ProfileModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)
    profile_id = "profileId_example" # str | The profile id of the authenticating profile.
    x_authorization = "profile_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `accessToken` of the authenticating profile.
    update_profile_request = UpdateProfileRequest(
        current_password="current_password_example",
        new_password="new_password_example",
        reset_access_token=True,
    ) # UpdateProfileRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update profile
        api_response = api_instance.update_profile(profile_id, x_authorization, update_profile_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->update_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The profile id of the authenticating profile. |
 **x_authorization** | **str**| The &#x60;accessToken&#x60; of the authenticating profile. |
 **update_profile_request** | [**UpdateProfileRequest**](UpdateProfileRequest.md)|  |

### Return type

[**ProfileModel**](ProfileModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated profile object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile_player**
> UpdateProfilePlayer200Response update_profile_player(profile_id, game_id, player_id, x_authorization, x_wallet_decrypt_key, update_profile_player_request)

Update profile player

Update various fields specific to a player. Such as changing its permissions.

### Example


```python
import time
import metafab_python
from metafab_python.api import ecosystems_api
from metafab_python.model.update_profile_player200_response import UpdateProfilePlayer200Response
from metafab_python.model.update_profile_player_request import UpdateProfilePlayerRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ecosystems_api.EcosystemsApi(api_client)
    profile_id = "profileId_example" # str | The profile id of the authenticating profile.
    game_id = "gameId_example" # str | Any game id within the MetaFab platform.
    player_id = "playerId_example" # str | Any player id within the MetaFab platform.
    x_authorization = "profile_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `accessToken` of the authenticating profile.
    x_wallet_decrypt_key = "AXNP8MKb+5SbBtHWrZu5KHh5/BomXY/dMRG/BDUn7a4=" # str | The `walletDecryptKey` of the authenticating profile. Required to decrypt and perform blockchain transactions with the profile wallet.
    update_profile_player_request = UpdateProfilePlayerRequest(
        permissions=ProfilePermissions(
            key=ProfilePermissionsValue(
                chain="chain_example",
                scopes=[
                    "scopes_example",
                ],
                functions=[
                    "functions_example",
                ],
                erc20_limit=1,
                erc1155_limits={
                    "key": 1,
                },
            ),
        ),
    ) # UpdateProfilePlayerRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update profile player
        api_response = api_instance.update_profile_player(profile_id, game_id, player_id, x_authorization, x_wallet_decrypt_key, update_profile_player_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling EcosystemsApi->update_profile_player: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The profile id of the authenticating profile. |
 **game_id** | **str**| Any game id within the MetaFab platform. |
 **player_id** | **str**| Any player id within the MetaFab platform. |
 **x_authorization** | **str**| The &#x60;accessToken&#x60; of the authenticating profile. |
 **x_wallet_decrypt_key** | **str**| The &#x60;walletDecryptKey&#x60; of the authenticating profile. Required to decrypt and perform blockchain transactions with the profile wallet. |
 **update_profile_player_request** | [**UpdateProfilePlayerRequest**](UpdateProfilePlayerRequest.md)|  |

### Return type

[**UpdateProfilePlayer200Response**](UpdateProfilePlayer200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the player. Returns a player object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

