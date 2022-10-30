# WithdrawFromExchangeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | A valid EVM based address to withdraw to. For example, &#x60;0x39cb70F972E0EE920088AeF97Dbe5c6251a9c25D&#x60;. | [optional] 
**wallet_id** | **str** | Any wallet id within the MetaFab ecosystem to withdraw to. | [optional] 
**currency_address** | **str** | The address of the currency (ERC20) token to withdraw from the exchange. If no currencyAddress or currencyId, and no collectionAddress or collectionId are provided, the native token held by the exchange will be withdrawn. | [optional] 
**currency_id** | **str** | A valid MetaFab currency id that represents the currency token to withdraw from the exchange. &#x60;currencyAddress&#x60; or &#x60;currencyId&#x60; can be provided when withdrawing currency. | [optional] 
**collection_address** | **str** | The address of the collection (ERC1155) for the items to withdraw from the exchange. If no currencyAddress and no collectionAddress is provided, the native token held by the exchange will be withdrawn. | [optional] 
**collection_id** | **str** | A valid MetaFab collection id that represents the collection for the items to withdraw from the exchange. &#x60;collectionAddress&#x60; or &#x60;collectionId&#x60; can be provided when withdrawing items. | [optional] 
**item_ids** | **[float]** | The specific itemIds of the provided collection to withdraw from the exchange. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


