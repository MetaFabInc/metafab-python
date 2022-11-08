# metafab_python.PlayersApi

All URIs are relative to *https://api.trymetafab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_player**](PlayersApi.md#auth_player) | **GET** /v1/players/auth | Authenticate player
[**create_player**](PlayersApi.md#create_player) | **POST** /v1/players | Create player
[**get_player**](PlayersApi.md#get_player) | **GET** /v1/players/{playerId} | Get player
[**get_players**](PlayersApi.md#get_players) | **GET** /v1/players | Get players
[**update_player**](PlayersApi.md#update_player) | **PATCH** /v1/players/{playerId} | Update player


# **auth_player**
> AuthPlayer200Response auth_player(x_game_key)

Authenticate player

Returns an existing player object containing access token, wallet, and other details for a game when provided a valid username and password login using Basic Auth.

### Example

* Basic Authentication (basicAuth):

```python
import time
import metafab_python
from metafab_python.api import players_api
from metafab_python.model.auth_player200_response import AuthPlayer200Response
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
    api_instance = players_api.PlayersApi(api_client)
    x_game_key = "game_pk_4SOqpDi8pQdnQgfCOBW29qR8YmwOhxVPz5iHoMgUEJLDdPXgwLuHqZf8ewo2GajZ" # str | The `publishedKey` of a specific game. This can be shared or included in game clients, websites, etc.

    # example passing only required values which don't have defaults set
    try:
        # Authenticate player
        api_response = api_instance.auth_player(x_game_key)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling PlayersApi->auth_player: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_game_key** | **str**| The &#x60;publishedKey&#x60; of a specific game. This can be shared or included in game clients, websites, etc. |

### Return type

[**AuthPlayer200Response**](AuthPlayer200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully authorized the request and retrieved a player object containing access token, wallet, and other details. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_player**
> AuthPlayer200Response create_player(x_game_key, create_player_request)

Create player

Create a new player for a game. Players are automatically associated with an internally managed wallet.  Player access tokens can be used to directly interact with any MetaFab managed contracts, currencies, items collections, marketplaces and more. Player interactions are also gasless by default, completely removing all crypto friction for players to engage with your MetaFab supported games.

### Example


```python
import time
import metafab_python
from metafab_python.api import players_api
from metafab_python.model.create_player_request import CreatePlayerRequest
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
    api_instance = players_api.PlayersApi(api_client)
    x_game_key = "game_pk_4SOqpDi8pQdnQgfCOBW29qR8YmwOhxVPz5iHoMgUEJLDdPXgwLuHqZf8ewo2GajZ" # str | The `publishedKey` of a specific game. This can be shared or included in game clients, websites, etc.
    create_player_request = CreatePlayerRequest(
        username="username_example",
        password="aReallyStrongPassword123",
    ) # CreatePlayerRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create player
        api_response = api_instance.create_player(x_game_key, create_player_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling PlayersApi->create_player: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_game_key** | **str**| The &#x60;publishedKey&#x60; of a specific game. This can be shared or included in game clients, websites, etc. |
 **create_player_request** | [**CreatePlayerRequest**](CreatePlayerRequest.md)|  |

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
**200** | Successfully created a new player. Returns a player object containing a wallet (used to interact with contracts, currencies, etc). |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player**
> PublicPlayer get_player(player_id)

Get player

Returns a player object for the provided player id.

### Example


```python
import time
import metafab_python
from metafab_python.api import players_api
from metafab_python.model.public_player import PublicPlayer
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    player_id = "playerId_example" # str | Any player id within the MetaFab ecosystem.

    # example passing only required values which don't have defaults set
    try:
        # Get player
        api_response = api_instance.get_player(player_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling PlayersApi->get_player: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| Any player id within the MetaFab ecosystem. |

### Return type

[**PublicPlayer**](PublicPlayer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved player. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_players**
> [PublicPlayer] get_players(x_authorization)

Get players

Returns all players for the authenticated game as an array of player objects.

### Example


```python
import time
import metafab_python
from metafab_python.api import players_api
from metafab_python.model.public_player import PublicPlayer
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.

    # example passing only required values which don't have defaults set
    try:
        # Get players
        api_response = api_instance.get_players(x_authorization)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling PlayersApi->get_players: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |

### Return type

[**[PublicPlayer]**](PublicPlayer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved players. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_player**
> PlayerModel update_player(player_id, x_authorization, update_player_request)

Update player

Update various fields specific to a player. Such as changing its password and resetting its access token.

### Example


```python
import time
import metafab_python
from metafab_python.api import players_api
from metafab_python.model.update_player_request import UpdatePlayerRequest
from metafab_python.model.player_model import PlayerModel
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = players_api.PlayersApi(api_client)
    player_id = "playerId_example" # str | Any player id within the MetaFab ecosystem.
    x_authorization = "player_at_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `accessToken` of the authenticating player.
    update_player_request = UpdatePlayerRequest(
        current_password="current_password_example",
        new_password="new_password_example",
        reset_access_token=True,
    ) # UpdatePlayerRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update player
        api_response = api_instance.update_player(player_id, x_authorization, update_player_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling PlayersApi->update_player: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| Any player id within the MetaFab ecosystem. |
 **x_authorization** | **str**| The &#x60;accessToken&#x60; of the authenticating player. |
 **update_player_request** | [**UpdatePlayerRequest**](UpdatePlayerRequest.md)|  |

### Return type

[**PlayerModel**](PlayerModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated player object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

