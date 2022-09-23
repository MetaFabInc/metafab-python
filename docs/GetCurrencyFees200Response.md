# GetCurrencyFees200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_address** | **str** | The wallet address that fees from all applicable transactions are automatically sent to. | [optional] 
**basis_points** | **float** | The number of fee basis points. 100 basisPoints &#x3D; 1% fee of the total transaction amount deducted from the total received by the recipient. | [optional] 
**fixed_amount** | **float** | The fixed number of currency as a fee regardless of the total transaction amount. 10 &#x3D; 10 of the currency as a fee for any transaction, deducted from the total received by the recipient. | [optional] 
**cap_amount** | **float** | The maximum combined fee between basisPoints and fixedAmount. If the total transaction fee is over this amount, the capAmount will be used as the transaction fee deducted from the total received by the recipient. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


