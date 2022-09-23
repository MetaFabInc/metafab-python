# BatchTransferCurrencyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amounts** | **[float]** | An array of currency amounts to transfer. Ordering corresponds to the ordering of provided &#x60;addresses&#x60; and/or &#x60;walletIds&#x60;. If both &#x60;addresses&#x60; and &#x60;walletIds&#x60; are provided, &#x60;addresses&#x60; are first in the order. | 
**addresses** | **[str]** | An array of valid EVM based addresses to transfer currency to. | [optional] 
**wallet_ids** | **[str]** | An array of wallet ids within the MetaFab ecosystem to transfer currency to. | [optional] 
**references** | **[float]** | An optional array of uint256 numbers to reference each transfer in the batch. Ordering corresponds to the ordering of provided &#x60;addresses&#x60; or &#x60;walletIds&#x60;. If both &#x60;addresses&#x60; and &#x60;walletIds&#x60; are provided, &#x60;addresses&#x60; are first in the order. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


