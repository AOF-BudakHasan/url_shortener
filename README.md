# Short Url
Get shorted url from a long url string. Choose your favorite adapter [GoogleUrlShorter, BitLinkUrlShorter]

```bash
pip install -i https://test.pypi.org/simple/ url-shortener==0.0.6
```

## Supported Services
GoogleUrlShorter, BitLinkUrlShorter 
## Usage

```python
from url_shortener import (
    UrlShorter, 
    GoogleUrlShorter, 
    BitLinkUrlShorter)

# ===> Working with `GoogleUrlShorter` adapter
selected_adapter = GoogleUrlShorter('YOUR_GOOGLE_API_KEY')

# ===> Working with `BitLinkUrlShorter` adapter
selected_adapter = BitLinkUrlShorter('YOUR_BITLINK_ACCESS_TOKEN')

# Now you can send our long url with `selected_adapter` 
# returns -> tuple -> (dict, int)
response, status_code = UrlShorter(selected_adapter).get_short_url('YOUR_LONG_URL_STRING')  

if status_code == 201:
    # Success response for all adapters will return as tuple
    #     ({'id': 'SHORTED_URL_STRING'}, 201)
    print("Here your shorted url: {shorted_url}".format(shorted_url=response['id']))
else:
    # Error response for all adapters will return as tuple
    #     (dict(
    #         message='ERROR_MESSAGE_TITLE'
    #         description='ERROR_MESSAGE_DESCRIPTION'
    #         errors=[{},{}],
    #         status_code=403 # response.status_code
    #     ), status_code)
    print("Oops! An error occurred. Details: {message}".format(message=response['description']))


```

## License
[MIT](https://choosealicense.com/licenses/mit/)
