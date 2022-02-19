import json

def pretty_print(json_data):
    """
    prints your json in pretty format so it's readable.
    """
    print(json.dumps(json_data, indent=4, sort_keys=True))


