---
title: API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - shell
  - python

includes:
  - errors

search: false
---

# Introduction

The Koncise API uses the latest in machine learning and data mining technologies to create a summary containing the major points from a given article.

By default the API will return a five sentence summary of any given English text. Shorter or longer summaries can be requested, as can summaries of articles in different languages.

The Koncise API is free to use for up to 100 summaries a day.

<!-- We have language bindings in Shell, Ruby, and Python! You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right.

This example API documentation page was created with [Slate](https://github.com/lord/slate). Feel free to edit it and use it as a base for your own API's documentation. -->

# Summation

```python
import kittn

api = kittn.authorize('meowmeowmeow')
api.kittens.get()
```

```shell
curl "http://example.com/api/kittens"
  -H "Authorization: meowmeowmeow"
```

> The above command returns JSON structured like this:

```json
[
  {
    "id": 1,
    "name": "Fluffums",
    "breed": "calico",
    "fluffiness": 6,
    "cuteness": 7
  },
  {
    "id": 2,
    "name": "Max",
    "breed": "unknown",
    "fluffiness": 5,
    "cuteness": 10
  }
]
```

This endpoint returns the summary of the text parameter.

If the number of sentences in text is less than the sentences_count, the original text will be returned.

### URL Endpoint

`POST https://api.koncise.io`

### POST Parameters

Parameter | Description | Required
--------- | ----------- | -----------  
text | Text to summarize | True
sentences_count | Length of summary, defaults to 5 | False
language | Language of given article, defaults to 'english' | False
