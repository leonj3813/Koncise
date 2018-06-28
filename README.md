# Koncise
> Django Rest Framework server to provide an api for text summation. Uses the Python library Sumy. Hosted at koncise.io.

Project using Django Rest Framework to provide a simple API for text summation. Uses the Python library Sumy (<https://github.com/miso-belica/sumy>) for the summation algorithms. Currently supports the algorithms LSA, Lexrank, and Textrank. Also supports summary sentence length and input language options.

Utilizes Django Rest Framework for POST data parsing, serialization, and daily rate limiting of API.

## Localhost usage
The Django project can be run with
```python
 pip install -r requirements.txt
 python manage.py runserver
 ```
 This serves the application at localhost:8000 and the API endpoint at api.localhost:8000. You may have to change your hosts file to get the api subdomain to work on your localhost.

### Docker
The project also includes a docker-compose file that can be used to set up the application behind a Nginx server. Running
```shell
docker-compose up
```
will serve the application at localhost and the API endpoint at api.localhost.

## Usage
The index page includes all API commands and examples for use.
