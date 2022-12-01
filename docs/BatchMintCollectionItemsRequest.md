# BatchMintCollectionItemsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ids** | **[int]** | An array of unique itemIds to create (mint). | 
**quantities** | **[int]** | An array of the quantities of each of the unique itemIds provided to create (mint). The quantity of each itemId in itemIds should be at the same index as the specific itemId in the itemIds array. For example, quantities[2] defines the quantity to mint for itemIds[2], etc. | 
**address** | **str** | A valid EVM based address to create (mint) the items for. For example, &#x60;0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D&#x60;. | [optional] 
**wallet_id** | **str** | Any wallet id within the MetaFab ecosystem to create (mint) the items for. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


