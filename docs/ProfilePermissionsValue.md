# ProfilePermissionsValue

Key should be the contract address, value is the permissions object request for the contract.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | **str** | The target chain for the contract and related permissions. | [optional] 
**scopes** | **[str]** | An optional array of valid permissioning scopes. | [optional] 
**functions** | **[str]** | An optional array of contract functions to request permission for. | [optional] 
**erc20_limit** | **int** | A maximum lifetime limit of erc20 that can be tranferred for this contract address. | [optional] 
**erc1155_limits** | **{str: (int,)}** | An object mapping erc1155 ids to maximum lifetime transfer limits of each permitted item id supplied for this contract address. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


