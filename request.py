import functions_framework

@functions_framework.http
def make_request(request):
    # """
    # HTTP Cloud Function that makes another HTTP request.
    # Args:
    #     request (flask.Request): The request object.
    #     <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    # Returns:
    #     The response text, or any set of values that can be turned into a
    #     Response object using `make_response`
    #     <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    # """
    import requests

    # The URL to send the request to
    url = "http://example.com"

    # Process the request
    response = requests.get(url)
    response.raise_for_status()
    return "Success!"
