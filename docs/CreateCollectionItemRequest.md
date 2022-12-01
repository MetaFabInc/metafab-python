# CreateCollectionItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique itemId to use for this item within the collection. If an existing itemId is used, the current metadata will be overriden. Any number may be used.  The terms &#x60;itemId&#x60; and &#x60;collectionItemId&#x60; are used interchangeably and equivalent to one another throughout MetaFab documentation. | 
**name** | **str** | The name of this item. | 
**description** | **str** | A text description of this item. This is a great spot to include lore, game mechanics and more related to this item. | 
**image_base64** | **str** | A base64 string of the image for this item. Either &#x60;imageBase64&#x60; or &#x60;imageUrl&#x60; must be provided. Supported image formats are &#x60;jpg&#x60;, &#x60;jpeg&#x60;, &#x60;png&#x60;, &#x60;gif&#x60;. Recommended size of 1:1 aspect ratio and no more than 1500x1500 pixels. | [optional] 
**image_url** | **str** | An external url that resolves to an image to use for this item. This can also be set to an ipfs:// uri. Recommended size of 1:1 aspect ratio and no more than 1500x1500 pixels. | [optional] 
**external_url** | **str** | An optional URL where players can go to learn more about this item specifically, or your game, or any other link. | [optional] 
**attributes** | [**[CreateCollectionItemRequestAttributesInner]**](CreateCollectionItemRequestAttributesInner.md) | An array of objects that conform with the [metadata attributes standard that can be found here](https://docs.opensea.io/docs/metadata-standards#attributes) | [optional] 
**data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | An arbitrary object of data attached to the top level metadata object. This is useful for including data or resource URLs specific to your game. Such as URLs that point to 3D models, music files, bitmaps, or anything else you need to reference. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


