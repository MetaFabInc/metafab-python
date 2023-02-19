# CreateProfileRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The profile&#39;s username, used to authenticate the profile. Profile usernames are globally unique across MetaFab. There cannot be 2 profiles with the same username created. | 
**password** | **str** | The password to authenticate as the profile. Additionally, this password is used to encrypt/decrypt a profile&#39;s primary wallet and must be provided anytime this profile makes blockchain interactions through various endpoints. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


