

def success_mock_google_adapter(*args, **kwargs):
    class MockResponse:
        def __init__(self, json, status_code):
            self._json = json
            self.status_code = status_code

        def json(self):
            return self._json
    return MockResponse(dict(id='http://goo.gl/12test123'), 201)


def failed_mock_google_adapter(*args, **kwargs):
    class MockResponse:
        def __init__(self, json, status_code):
            self._json = json
            self.status_code = status_code

        def json(self):
            return self._json
    google_failed_dict = {
     "error": {
      "errors": [
       {
        "domain": "global",
        "reason": "forbidden",
        "message": "Forbidden"
       }
      ],
      "code": 403,
      "message": "MockErrorMessage"
     }
    }
    return MockResponse(google_failed_dict, 403)


def success_mock_bitlink_adapter(*args, **kwargs):
    class MockResponse:
        def __init__(self, json, status_code):
            self._json = json
            self.status_code = status_code

        def json(self):
            return self._json
    return MockResponse(dict(id='http://bit.ly/12test123'), 201)


def failed_mock_bitlink_adapter(*args, **kwargs):
    class MockResponse:
        def __init__(self, json, status_code):
            self._json = json
            self.status_code = status_code

        def json(self):
            return self._json
    google_failed_dict = {
      "message": "MockErrorMessage",
      "errors": [
        {
          "field": "string",
          "message": "string",
          "error_code": "string"
        }
      ],
      "resource": "string",
      "description": "string"
    }
    return MockResponse(google_failed_dict, 403)


