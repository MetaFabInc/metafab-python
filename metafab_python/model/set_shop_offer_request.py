"""
    MetaFab API

    Complete MetaFab API references and guides can be found at: https://trymetafab.com  # noqa: E501

    The version of the OpenAPI document: 1.5.1
    Contact: metafabproject@gmail.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from metafab_python.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from metafab_python.exceptions import ApiAttributeError



class SetShopOfferRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'id': (int,),  # noqa: E501
            'input_collection_address': (str,),  # noqa: E501
            'input_collection_id': (str,),  # noqa: E501
            'input_collection_item_ids': ([int],),  # noqa: E501
            'input_collection_item_amounts': ([int],),  # noqa: E501
            'input_currency_address': (str,),  # noqa: E501
            'input_currency_id': (str,),  # noqa: E501
            'input_currency_amount': (float,),  # noqa: E501
            'output_collection_address': (str,),  # noqa: E501
            'output_collection_id': (str,),  # noqa: E501
            'output_collection_item_ids': ([int],),  # noqa: E501
            'output_collection_item_amounts': ([int],),  # noqa: E501
            'output_currency_address': (str,),  # noqa: E501
            'output_currency_id': (str,),  # noqa: E501
            'output_currency_amount': (float,),  # noqa: E501
            'max_uses': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'input_collection_address': 'inputCollectionAddress',  # noqa: E501
        'input_collection_id': 'inputCollectionId',  # noqa: E501
        'input_collection_item_ids': 'inputCollectionItemIds',  # noqa: E501
        'input_collection_item_amounts': 'inputCollectionItemAmounts',  # noqa: E501
        'input_currency_address': 'inputCurrencyAddress',  # noqa: E501
        'input_currency_id': 'inputCurrencyId',  # noqa: E501
        'input_currency_amount': 'inputCurrencyAmount',  # noqa: E501
        'output_collection_address': 'outputCollectionAddress',  # noqa: E501
        'output_collection_id': 'outputCollectionId',  # noqa: E501
        'output_collection_item_ids': 'outputCollectionItemIds',  # noqa: E501
        'output_collection_item_amounts': 'outputCollectionItemAmounts',  # noqa: E501
        'output_currency_address': 'outputCurrencyAddress',  # noqa: E501
        'output_currency_id': 'outputCurrencyId',  # noqa: E501
        'output_currency_amount': 'outputCurrencyAmount',  # noqa: E501
        'max_uses': 'maxUses',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, *args, **kwargs):  # noqa: E501
        """SetShopOfferRequest - a model defined in OpenAPI

        Args:
            id (int): A unique offer id to use for this offer for the shop. If an existing offer id is used, the current offer will be updated but the existing number of uses will be kept. If you want to reset the number of uses for an existing offer, first remove it using the remove offer endpoint, then set it.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            input_collection_address (str): A valid EVM based ERC1155 or MetaFab game items contract address that represents the collection for input items required by this offer. `inputCollectionAddress` or `inputCollectionId` can optionally be provided.. [optional]  # noqa: E501
            input_collection_id (str): A valid MetaFab collection id that represents the collection for input items required by this offer. `inputCollectionAddress` or `inputCollectionId` can optionally be provided.. [optional]  # noqa: E501
            input_collection_item_ids ([int]): An array of item ids from the provided input collection that are required to use this offer. Input items are transferred from the wallet to the shop contract upon using an offer.. [optional]  # noqa: E501
            input_collection_item_amounts ([int]): An array of amounts for each item id from the provided input collection that are required to use this offer. Item amounts array indices are reflective of the amount required for a given item id at the same index.. [optional]  # noqa: E501
            input_currency_address (str): A valid EVM based ERC20 or MetaFab game currency contract address that for the currency required by this offer.. [optional]  # noqa: E501
            input_currency_id (str): A valid MetaFab currency id that represents the currency required by this offer.. [optional]  # noqa: E501
            input_currency_amount (float): The amount of currency required by this offer. If an inputCurrencyAmount is provided without in input currency address or id, the native chain currency is used as the required currency.. [optional]  # noqa: E501
            output_collection_address (str): A valid EVM based ERC1155 or MetaFab game items contract address that represents the collection for output items given by this offer. `outputCollectionAddress` or `outputCollectionId` can optionally be provided.. [optional]  # noqa: E501
            output_collection_id (str): A valid MetaFab collection id that represents the collection for output items given by this offer. `outputCollectionAddress` or `outputCollectionId` can optionally be provided.. [optional]  # noqa: E501
            output_collection_item_ids ([int]): An array of item ids from the provided output collection that are given by this offer. Output items are automatically minted if the shop contract has the `minter` role for the output collection contract. Otherwise, they are transferred from the item balance held by the shop contract.. [optional]  # noqa: E501
            output_collection_item_amounts ([int]): An array of amounts for each item id from the provided output collection that are given by this offer. Item amounts array indices are reflective of the amount required for a given item id at the same index.. [optional]  # noqa: E501
            output_currency_address (str): A valid EVM based ERC20 or MetaFab game currency contract address that for the currency given by this offer. The output currency amount is automatically minted if the shop contract has the `minter` role for the output currency contract. Otherwise, they are transferred from the currency balance held by the shop contract.. [optional]  # noqa: E501
            output_currency_id (str): A valid MetaFab currency id for the currency given by this offer.. [optional]  # noqa: E501
            output_currency_amount (float): The amount of currency given by this offer. If an outputCurrencyAmount is provided without an output currency address or id, the native chain currency is used as the given currency.. [optional]  # noqa: E501
            max_uses (int): The maximum number of times this offer can be used in total. maxUses is collective across all uses of the offer. If 5 unique players use an offer, that counts as 5 offer uses. Exclude this or use 0 to allow unlimited uses.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, id, *args, **kwargs):  # noqa: E501
        """SetShopOfferRequest - a model defined in OpenAPI

        Args:
            id (int): A unique offer id to use for this offer for the shop. If an existing offer id is used, the current offer will be updated but the existing number of uses will be kept. If you want to reset the number of uses for an existing offer, first remove it using the remove offer endpoint, then set it.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            input_collection_address (str): A valid EVM based ERC1155 or MetaFab game items contract address that represents the collection for input items required by this offer. `inputCollectionAddress` or `inputCollectionId` can optionally be provided.. [optional]  # noqa: E501
            input_collection_id (str): A valid MetaFab collection id that represents the collection for input items required by this offer. `inputCollectionAddress` or `inputCollectionId` can optionally be provided.. [optional]  # noqa: E501
            input_collection_item_ids ([int]): An array of item ids from the provided input collection that are required to use this offer. Input items are transferred from the wallet to the shop contract upon using an offer.. [optional]  # noqa: E501
            input_collection_item_amounts ([int]): An array of amounts for each item id from the provided input collection that are required to use this offer. Item amounts array indices are reflective of the amount required for a given item id at the same index.. [optional]  # noqa: E501
            input_currency_address (str): A valid EVM based ERC20 or MetaFab game currency contract address that for the currency required by this offer.. [optional]  # noqa: E501
            input_currency_id (str): A valid MetaFab currency id that represents the currency required by this offer.. [optional]  # noqa: E501
            input_currency_amount (float): The amount of currency required by this offer. If an inputCurrencyAmount is provided without in input currency address or id, the native chain currency is used as the required currency.. [optional]  # noqa: E501
            output_collection_address (str): A valid EVM based ERC1155 or MetaFab game items contract address that represents the collection for output items given by this offer. `outputCollectionAddress` or `outputCollectionId` can optionally be provided.. [optional]  # noqa: E501
            output_collection_id (str): A valid MetaFab collection id that represents the collection for output items given by this offer. `outputCollectionAddress` or `outputCollectionId` can optionally be provided.. [optional]  # noqa: E501
            output_collection_item_ids ([int]): An array of item ids from the provided output collection that are given by this offer. Output items are automatically minted if the shop contract has the `minter` role for the output collection contract. Otherwise, they are transferred from the item balance held by the shop contract.. [optional]  # noqa: E501
            output_collection_item_amounts ([int]): An array of amounts for each item id from the provided output collection that are given by this offer. Item amounts array indices are reflective of the amount required for a given item id at the same index.. [optional]  # noqa: E501
            output_currency_address (str): A valid EVM based ERC20 or MetaFab game currency contract address that for the currency given by this offer. The output currency amount is automatically minted if the shop contract has the `minter` role for the output currency contract. Otherwise, they are transferred from the currency balance held by the shop contract.. [optional]  # noqa: E501
            output_currency_id (str): A valid MetaFab currency id for the currency given by this offer.. [optional]  # noqa: E501
            output_currency_amount (float): The amount of currency given by this offer. If an outputCurrencyAmount is provided without an output currency address or id, the native chain currency is used as the given currency.. [optional]  # noqa: E501
            max_uses (int): The maximum number of times this offer can be used in total. maxUses is collective across all uses of the offer. If 5 unique players use an offer, that counts as 5 offer uses. Exclude this or use 0 to allow unlimited uses.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
