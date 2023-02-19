# metafab_python.GamesApi

All URIs are relative to *https://api.trymetafab.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_game**](GamesApi.md#auth_game) | **GET** /v1/games/auth | Authenticate game
[**create_game**](GamesApi.md#create_game) | **POST** /v1/games | Create game
[**get_game**](GamesApi.md#get_game) | **GET** /v1/games/{gameId} | Get game
[**update_game**](GamesApi.md#update_game) | **PATCH** /v1/games/{gameId} | Update game


# **auth_game**
> AuthGame200Response auth_game()

Authenticate game

Returns an existing game object containing authorization keys and credentials when provided a valid email (in place of username) and password login using Basic Auth.

### Example

* Basic Authentication (basicAuth):

```python
import time
import metafab_python
from metafab_python.api import games_api
from metafab_python.model.auth_game200_response import AuthGame200Response
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
    api_instance = games_api.GamesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Authenticate game
        api_response = api_instance.auth_game()
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling GamesApi->auth_game: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthGame200Response**](AuthGame200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully authorized the request and retrieved a game object containing authorization keys and credentials. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_game**
> AuthGame200Response create_game(create_game_request)

Create game

Create a new game. A game is the root entity required for all API interactions. Contracts, currencies, items and more are deployed by games, player accounts are created and registered to games, etc.  To use any of MetaFab's services, you must first create a game through this endpoint.  After creating your game through this endpoint, a verification email will be sent to the email address used. Before you can access any of MetaFab's features, you'll need to click the link contained in the verification email to verify your account.

### Example


```python
import time
import metafab_python
from metafab_python.api import games_api
from metafab_python.model.auth_game200_response import AuthGame200Response
from metafab_python.model.create_game_request import CreateGameRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = games_api.GamesApi(api_client)
    create_game_request = CreateGameRequest(
        name="NFT Worlds",
        email="dev@nftworlds.com",
        password="aReallyStrongPassword123!",
    ) # CreateGameRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create game
        api_response = api_instance.create_game(create_game_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling GamesApi->create_game: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_game_request** | [**CreateGameRequest**](CreateGameRequest.md)|  |

### Return type

[**AuthGame200Response**](AuthGame200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new game. Returns a game object containing a wallet and fundingWallet property, respectively representing the games primary wallet address (used to deploy &amp; interact with contract) and funding wallet address (used to cover gasless transaction fees). |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_game**
> PublicGame get_game(game_id)

Get game

Returns a game object for the provided game id.

### Example


```python
import time
import metafab_python
from metafab_python.api import games_api
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
    api_instance = games_api.GamesApi(api_client)
    game_id = "gameId_example" # str | Any game id within the MetaFab platform.

    # example passing only required values which don't have defaults set
    try:
        # Get game
        api_response = api_instance.get_game(game_id)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling GamesApi->get_game: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | Successfully retrieved game. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_game**
> UpdateGame200Response update_game(game_id, x_authorization, update_game_request)

Update game

Update various fields specific to a game. Such as changing its password, resetting its published or secret key, or updating its RPCs.

### Example


```python
import time
import metafab_python
from metafab_python.api import games_api
from metafab_python.model.update_game200_response import UpdateGame200Response
from metafab_python.model.update_game_request import UpdateGameRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.trymetafab.com
# See configuration.py for a list of all supported configuration parameters.
configuration = metafab_python.Configuration(
    host = "https://api.trymetafab.com"
)


# Enter a context with an instance of the API client
with metafab_python.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = games_api.GamesApi(api_client)
    game_id = "gameId_example" # str | The game id of the authenticating game.
    x_authorization = "game_sk_02z4Mv3c85Ig0gNowY9Dq0N2kjb1xwzr27ArLE0669RrRI6dLf822iPO26K1p1FP" # str | The `secretKey` of the authenticating game.
    update_game_request = UpdateGameRequest(
        name="name_example",
        email="email_example",
        current_password="current_password_example",
        new_password="new_password_example",
        rpcs={
            "key": "key_example",
        },
        redirect_uris=[
            "http://localhost",
        ],
        icon_image_base64="icon_image_base64_example",
        cover_image_base64="cover_image_base64_example",
        primary_color_hex="primary_color_hex_example",
        reset_published_key=True,
        reset_secret_key=True,
    ) # UpdateGameRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update game
        api_response = api_instance.update_game(game_id, x_authorization, update_game_request)
        pprint(api_response)
    except metafab_python.ApiException as e:
        print("Exception when calling GamesApi->update_game: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| The game id of the authenticating game. |
 **x_authorization** | **str**| The &#x60;secretKey&#x60; of the authenticating game. |
 **update_game_request** | [**UpdateGameRequest**](UpdateGameRequest.md)|  |

### Return type

[**UpdateGame200Response**](UpdateGame200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated game object. |  -  |
**400** | An API level error occurred. This is often due to problematic data being provided by you. |  -  |
**401** | An authorization error occured. This is often due to incorrect tokens or keys being provided, or accessing a resource that the provided tokens or keys do not have access to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

