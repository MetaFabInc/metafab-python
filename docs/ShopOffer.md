# ShopOffer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of this offer. | [optional] 
**input_collection** | **str** | The address of the ERC1155 or MetaFab game items contract for input items required by this offer. | [optional] 
**input_collection_item_ids** | **[int]** | An array of item ids from the input collection that are required for this offer. | [optional] 
**input_collection_item_amounts** | **[int]** | An array of amounts for each item id for the input collection that are required to use this offer. | [optional] 
**input_currency** | **str** | The address of the ERC20 or MetaFab game currency for the currency required by this offer. | [optional] 
**input_currency_amount** | **float** | The amount of currency required by this offer. | [optional] 
**output_collection** | **str** | The address of the ERC1155 or MetaFab game items contract for output items given by this offer. | [optional] 
**output_collection_item_ids** | **[int]** | An array of item ids from the output collection that are given for this offer. | [optional] 
**output_collection_item_amounts** | **[int]** | An array of amounts for each item id for the output collection that are given by this offer. | [optional] 
**output_currency** | **str** | The address of the ERC20 or MetaFab game currency for the output currency given by this offer. | [optional] 
**output_currency_amount** | **float** | The amount of currency given by this offer. | [optional] 
**uses** | **int** | The number of times this offer has been used. | [optional] 
**max_uses** | **int** | The maximum number of times this offer can be used. A value of &#x60;0&#x60; means there is no limit on how many times this offer can be used. | [optional] 
**last_updated_at** | **int** | A unix timestamp in seconds that represents the last time this offer was set or updated. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


