# UpdateGameRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** | The game&#39;s current password. Must be provided if setting &#x60;newPassword&#x60;. | [optional] 
**new_password** | **str** | A new password. The game&#39;s old password will no longer be valid. | [optional] 
**rpcs** | **{str: (str,)}** | Sets a custom RPC for your game to use instead of MetaFab&#39;s default RPCs for the chain(s) you specify.  Expects a JSON object containing key value pairs of supported &#x60;chain&#x60; -&gt; &#x60;rpc url&#x60;. Only the chain names provided as keys in the object will be explicitly overriden. To delete a custom RPC for your game, provide the chain name to delete as a key in the provided object and &#x60;null&#x60; as the value.  Set RPC example, &#x60;{ MATIC: &#39;https://polygon-rpc.com&#39; }&#x60; Delete RPC example, &#x60;{ MATIC: null }&#x60; | [optional] 
**reset_published_key** | **bool** | Revokes the game&#39;s previous published key and returns a new one if true. | [optional] 
**reset_secret_key** | **bool** | Revokes the game&#39;s previous secret key and returns a new on if true. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

