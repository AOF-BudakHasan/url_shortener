# Short Url
Get shorted url from a long url string. Choose your favorite adapter [GoogleUrlShorter, BitLinkUrlShorter]

```bash
pip install -i https://test.pypi.org/simple/ url-shortener==0.0.1
```

## Supported Services
GoogleUrlShorter, BitLinkUrlShorter 
## Usage

```python
from src import (UrlShorter, GoogleUrlShorter, BitLinkUrlShorter)
# ===> Usage with `GoogleUrlShorter` adapter
adapter_google = GoogleUrlShorter('YOUR_GOOGLE_API_KEY')
shorted_url = UrlShorter(adapter_google).get_short_url('YOUR_LONG_URL_STRING')

# ===> Usage with `BitLinkUrlShorter` adapter
adapter_bitlink = BitLinkUrlShorter('YOUR_BITLINK_ACCESS_TOKEN')
shorted_url = UrlShorter(adapter_bitlink).get_short_url('YOUR_LONG_URL_STRING')

# Success response for all adapters will return as tuple
#     ({'id': 'SHORTED_URL_STRING'}, 201)
# Error response for all adapters will return as tuple
#     (dict(
#         message='ERROR_MESSAGE_TITLE'
#         description='ERROR_MESSAGE_DESCRIPTION'
#         errors=[{},{}],
#         status_code=400 # response.status_code
#     ), status_code)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
