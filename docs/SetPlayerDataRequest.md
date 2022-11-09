# SetPlayerDataRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protected_data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | protectedData can only be set if &#x60;X-Authorization&#x60; includes credentials for the game the target player is a part of. Expects an arbitrary object allowed to contain any set of properties and nested data within those properties, including arrays. | [optional] 
**public_data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | publicData can be set if &#x60;X-Authorization&#x60; includes credentials for the target player or game the player is a part of. Expects an arbitrary object allowed to contain any set of properties and nested data within those properties, including arrays. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


