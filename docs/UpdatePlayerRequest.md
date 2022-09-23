# UpdatePlayerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** | The player&#39;s current password. Must be provided if setting &#x60;newPassword&#x60;. | [optional] 
**new_password** | **str** | A new password. The player&#39;s old password will no longer be valid. | [optional] 
**reset_access_token** | **bool** | Revokes the player&#39;s previous access token and returns a new one if true. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


