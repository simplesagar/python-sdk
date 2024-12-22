# VideoDescribeSettings


## Fields

| Field                                                                                                                         | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `prompt`                                                                                                                      | *OptionalNullable[str]*                                                                                                       | :heavy_minus_sign:                                                                                                            | Prompt for video description                                                                                                  |
| `enabled`                                                                                                                     | *Optional[bool]*                                                                                                              | :heavy_minus_sign:                                                                                                            | Enable video description                                                                                                      |
| `max_length`                                                                                                                  | *OptionalNullable[int]*                                                                                                       | :heavy_minus_sign:                                                                                                            | Maximum length of the description                                                                                             |
| `json_output`                                                                                                                 | [Optional[models.VideoDescribeSettingsJSONOutput]](../models/videodescribesettingsjsonoutput.md)                              | :heavy_minus_sign:                                                                                                            | JSON format for the response                                                                                                  |
| `vector_index`                                                                                                                | [OptionalNullable[models.VectorModel]](../models/vectormodel.md)                                                              | :heavy_minus_sign:                                                                                                            | Name of the vector model to use for embedding the text output. If vector_index is duplicated, the vector will be overwritten. |