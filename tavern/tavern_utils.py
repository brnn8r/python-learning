import json


def save_response(response):
    filename = 'test_results.json'
    with open(filename, 'w') as f:
        json.dump(response.json(), f)
