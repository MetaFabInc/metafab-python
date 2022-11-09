"""
    MetaFab API

     Complete MetaFab API references and guides can be found at: https://trymetafab.com  # noqa: E501

    The version of the OpenAPI document: 1.2.1
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
from metafab_python.model.contract_model import ContractModel
from metafab_python.model.create_contract_request import CreateContractRequest
from metafab_python.model.transaction_model import TransactionModel
from metafab_python.model.write_contract_request import WriteContractRequest


class ContractsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_contract_endpoint = _Endpoint(
            settings={
                'response_type': (ContractModel,),
                'auth': [],
                'endpoint_path': '/v1/contracts',
                'operation_id': 'create_contract',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_authorization',
                    'create_contract_request',
                ],
                'required': [
                    'x_authorization',
                    'create_contract_request',
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
                    'x_authorization':
                        (str,),
                    'create_contract_request':
                        (CreateContractRequest,),
                },
                'attribute_map': {
                    'x_authorization': 'X-Authorization',
                },
                'location_map': {
                    'x_authorization': 'header',
                    'create_contract_request': 'body',
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
        self.get_contracts_endpoint = _Endpoint(
            settings={
                'response_type': ([ContractModel],),
                'auth': [],
                'endpoint_path': '/v1/contracts',
                'operation_id': 'get_contracts',
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
        self.read_contract_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [],
                'endpoint_path': '/v1/contracts/{contractId}/reads',
                'operation_id': 'read_contract',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'contract_id',
                    'func',
                    'args',
                ],
                'required': [
                    'contract_id',
                    'func',
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
                    'contract_id':
                        (str,),
                    'func':
                        (str,),
                    'args':
                        (str,),
                },
                'attribute_map': {
                    'contract_id': 'contractId',
                    'func': 'func',
                    'args': 'args',
                },
                'location_map': {
                    'contract_id': 'path',
                    'func': 'query',
                    'args': 'query',
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
        self.write_contract_endpoint = _Endpoint(
            settings={
                'response_type': (TransactionModel,),
                'auth': [],
                'endpoint_path': '/v1/contracts/{contractId}/writes',
                'operation_id': 'write_contract',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'contract_id',
                    'x_authorization',
                    'x_password',
                    'write_contract_request',
                ],
                'required': [
                    'contract_id',
                    'x_authorization',
                    'x_password',
                    'write_contract_request',
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
                    'contract_id':
                        (str,),
                    'x_authorization':
                        (str,),
                    'x_password':
                        (str,),
                    'write_contract_request':
                        (WriteContractRequest,),
                },
                'attribute_map': {
                    'contract_id': 'contractId',
                    'x_authorization': 'X-Authorization',
                    'x_password': 'X-Password',
                },
                'location_map': {
                    'contract_id': 'path',
                    'x_authorization': 'header',
                    'x_password': 'header',
                    'write_contract_request': 'body',
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

    def create_contract(
        self,
        x_authorization,
        create_contract_request,
        **kwargs
    ):
        """Create custom contract  # noqa: E501

        Create a MetaFab custom contract entry from an existing contract address and contract abi. This allows the game and players belonging to the authenticated game to interact with the contract's read and write functions through MetaFab's read and write contract endpoints.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_contract(x_authorization, create_contract_request, async_req=True)
        >>> result = thread.get()

        Args:
            x_authorization (str): The `secretKey` of the authenticating game.
            create_contract_request (CreateContractRequest):

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
            ContractModel
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
        kwargs['x_authorization'] = \
            x_authorization
        kwargs['create_contract_request'] = \
            create_contract_request
        return self.create_contract_endpoint.call_with_http_info(**kwargs)

    def get_contracts(
        self,
        x_game_key,
        **kwargs
    ):
        """Get contracts  # noqa: E501

        Returns an array of active contracts deployed by the game associated with the provided `X-Game-Key`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_contracts(x_game_key, async_req=True)
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
            [ContractModel]
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
        return self.get_contracts_endpoint.call_with_http_info(**kwargs)

    def read_contract(
        self,
        contract_id,
        func,
        **kwargs
    ):
        """Read contract data  # noqa: E501

        Oftentimes you'll want to query and retrieve some data from a contract. This is incredibly easy to do for any contract deployed through MetaFab.  Using this endpoint, you can get the data returned by any readable function listed in a contracts ABI. This could be things like querying the totalSupply of a currency contract, the number of owners of an items contract, and more.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.read_contract(contract_id, func, async_req=True)
        >>> result = thread.get()

        Args:
            contract_id (str): Any contract id within the MetaFab ecosystem.
            func (str): A contract function name. This can be any valid function from the the ABI of the contract you are interacting with. For example, `balanceOf`.

        Keyword Args:
            args (str): A comma seperated list of basic data type arguments. This is optional and only necessary if the function being invoked requires arguments per the contract ABI. For example, `123,\"Hello\",false`.. [optional]
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
            bool, date, datetime, dict, float, int, list, str, none_type
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
        kwargs['contract_id'] = \
            contract_id
        kwargs['func'] = \
            func
        return self.read_contract_endpoint.call_with_http_info(**kwargs)

    def write_contract(
        self,
        contract_id,
        x_authorization,
        x_password,
        write_contract_request,
        **kwargs
    ):
        """Write contract data  # noqa: E501

        MetaFab's convenience endpoints for contract interactions may not be flexible enough depending on your use case. For these situations, you can interact with contracts and create transactions directly.  Using this endpoint, you can execute a transaction for any writeable contract method as defined in the contract's ABI for the MetaFab contractId provided. Both Games and Player resources have authority to use this endpoint to execute transactions against any valid MetaFab contractId.  Additionally, MetaFab will automatically attempt to perform a gasless transaction for players interacting with a contract through this endpoint. Gasless transactions by players through this endpoint will only work if the target contract was deployed through MetaFab or supports MetaFab's ERC2771 trusted forwarder contract.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.write_contract(contract_id, x_authorization, x_password, write_contract_request, async_req=True)
        >>> result = thread.get()

        Args:
            contract_id (str): Any contract id within the MetaFab ecosystem.
            x_authorization (str): The `secretKey` of a specific game or the `accessToken` of a specific player.
            x_password (str): The password of the authenticating game or player. Required to decrypt and perform blockchain transactions with the game or player primary wallet.
            write_contract_request (WriteContractRequest):

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
            TransactionModel
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
        kwargs['contract_id'] = \
            contract_id
        kwargs['x_authorization'] = \
            x_authorization
        kwargs['x_password'] = \
            x_password
        kwargs['write_contract_request'] = \
            write_contract_request
        return self.write_contract_endpoint.call_with_http_info(**kwargs)

