"""
    MetaFab API

     Complete MetaFab API references and guides can be found at: https://trymetafab.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: metafabproject@gmail.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from metafab_python.api_client import ApiClient, Endpoint as _Endpoint
from metafab_python.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from metafab_python.model.auth_player200_response import AuthPlayer200Response
from metafab_python.model.create_player_request import CreatePlayerRequest
from metafab_python.model.player_model import PlayerModel
from metafab_python.model.update_player_request import UpdatePlayerRequest


class PlayersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.auth_player_endpoint = _Endpoint(
            settings={
                'response_type': (AuthPlayer200Response,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/v1/players',
                'operation_id': 'auth_player',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_game_key',
                ],
                'required': [
                    'x_game_key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_game_key':
                        (str,),
                },
                'attribute_map': {
                    'x_game_key': 'X-Game-Key',
                },
                'location_map': {
                    'x_game_key': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.create_player_endpoint = _Endpoint(
            settings={
                'response_type': (AuthPlayer200Response,),
                'auth': [],
                'endpoint_path': '/v1/players',
                'operation_id': 'create_player',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_game_key',
                    'create_player_request',
                ],
                'required': [
                    'x_game_key',
                    'create_player_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_game_key':
                        (str,),
                    'create_player_request':
                        (CreatePlayerRequest,),
                },
                'attribute_map': {
                    'x_game_key': 'X-Game-Key',
                },
                'location_map': {
                    'x_game_key': 'header',
                    'create_player_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.update_player_endpoint = _Endpoint(
            settings={
                'response_type': (PlayerModel,),
                'auth': [],
                'endpoint_path': '/v1/players/{playerId}',
                'operation_id': 'update_player',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'player_id',
                    'x_authorization',
                    'update_player_request',
                ],
                'required': [
                    'player_id',
                    'x_authorization',
                    'update_player_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'player_id':
                        (str,),
                    'x_authorization':
                        (str,),
                    'update_player_request':
                        (UpdatePlayerRequest,),
                },
                'attribute_map': {
                    'player_id': 'playerId',
                    'x_authorization': 'X-Authorization',
                },
                'location_map': {
                    'player_id': 'path',
                    'x_authorization': 'header',
                    'update_player_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def auth_player(
        self,
        x_game_key,
        **kwargs
    ):
        """Authenticate player  # noqa: E501

        Returns an existing player object containing access token, wallet, and other details for a game when provided a valid username and password login using Basic Auth.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auth_player(x_game_key, async_req=True)
        >>> result = thread.get()

        Args:
            x_game_key (str): The `publishedKey` of a specific game. This can be shared or included in game clients, websites, etc.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            AuthPlayer200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['x_game_key'] = \
            x_game_key
        return self.auth_player_endpoint.call_with_http_info(**kwargs)

    def create_player(
        self,
        x_game_key,
        create_player_request,
        **kwargs
    ):
        """Create player  # noqa: E501

        Create a new player for a game. Players are automatically associated with an internally managed wallet.  Player access tokens can be used to directly interact with any MetaFab managed contracts, currencies, items collections, marketplaces and more. Player interactions are also gasless by default, completely removing all crypto friction for players to engage with your MetaFab supported games.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_player(x_game_key, create_player_request, async_req=True)
        >>> result = thread.get()

        Args:
            x_game_key (str): The `publishedKey` of a specific game. This can be shared or included in game clients, websites, etc.
            create_player_request (CreatePlayerRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            AuthPlayer200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['x_game_key'] = \
            x_game_key
        kwargs['create_player_request'] = \
            create_player_request
        return self.create_player_endpoint.call_with_http_info(**kwargs)

    def update_player(
        self,
        player_id,
        x_authorization,
        update_player_request,
        **kwargs
    ):
        """Update player  # noqa: E501

        Update various fields specific to a player. Such as changing its password and resetting its access token.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_player(player_id, x_authorization, update_player_request, async_req=True)
        >>> result = thread.get()

        Args:
            player_id (str): Any player id within the MetaFab ecosystem.
            x_authorization (str): The `accessToken` of the authenticating player.
            update_player_request (UpdatePlayerRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PlayerModel
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['player_id'] = \
            player_id
        kwargs['x_authorization'] = \
            x_authorization
        kwargs['update_player_request'] = \
            update_player_request
        return self.update_player_endpoint.call_with_http_info(**kwargs)
