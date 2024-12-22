# ImageSettings


## Fields

| Field                                                                                                                                                                           | Type                                                                                                                                                                            | Required                                                                                                                                                                        | Description                                                                                                                                                                     | Example                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `read`                                                                                                                                                                          | [OptionalNullable[models.ImageReadSettings]](../models/imagereadsettings.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                                              | Settings for reading and analyzing image content.                                                                                                                               | {<br/>"enabled": true<br/>}                                                                                                                                                     |
| `embed`                                                                                                                                                                         | List[[models.EmbeddingRequest](../models/embeddingrequest.md)]                                                                                                                  | :heavy_minus_sign:                                                                                                                                                              | List of embedding settings for generating multiple embeddings. If url is provided, value must be None. <br/> Default: [{type: 'url', vector_index: 'multimodal'}] if none provided. | [<br/>{<br/>"type": "url",<br/>"vector_index": "multimodal"<br/>},<br/>{<br/>"type": "url",<br/>"vector_index": "image"<br/>}<br/>]                                             |
| `describe`                                                                                                                                                                      | [OptionalNullable[models.ImageDescribeSettings]](../models/imagedescribesettings.md)                                                                                            | :heavy_minus_sign:                                                                                                                                                              | Settings for generating image descriptions.                                                                                                                                     | {<br/>"enabled": true,<br/>"max_length": 1000<br/>}                                                                                                                             |
| `detect`                                                                                                                                                                        | [OptionalNullable[models.ImageDetectSettings]](../models/imagedetectsettings.md)                                                                                                | :heavy_minus_sign:                                                                                                                                                              | Settings for object detection in images.                                                                                                                                        | {<br/>"faces": {<br/>"confidence_threshold": 0.8,<br/>"enabled": true<br/>}<br/>}                                                                                               |
| `json_output`                                                                                                                                                                   | [OptionalNullable[models.JSONImageOutputSettings]](../models/jsonimageoutputsettings.md)                                                                                        | :heavy_minus_sign:                                                                                                                                                              | Settings for structured JSON output of image analysis.                                                                                                                          | {<br/>"response_shape": {<br/>"colors": [<br/>"str"<br/>],<br/>"objects": [<br/>"str"<br/>]<br/>}<br/>}                                                                         |