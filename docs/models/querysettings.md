# QuerySettings


## Fields

| Field                                                                                                                     | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               | Example                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                   | *OptionalNullable[int]*                                                                                                   | :heavy_minus_sign:                                                                                                        | Optional limit for number of results per vector index, this is overriden by ?page_size=int if a single query is provided. | 10                                                                                                                        |
| `min_score`                                                                                                               | *OptionalNullable[float]*                                                                                                 | :heavy_minus_sign:                                                                                                        | Optional score threshold for filtering results                                                                            | 0.5                                                                                                                       |
| `modality`                                                                                                                | *OptionalNullable[str]*                                                                                                   | :heavy_minus_sign:                                                                                                        | Optional modality override for the query, this is only used for multimodal embeddings                                     | image                                                                                                                     |