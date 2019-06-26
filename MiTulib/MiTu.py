import json
from .ElementList import ElementList


def make(element_list):
    elements = []
    ElementList(element_list).add_into_list(elements)
    result = {
        "ver": "1.0.0",
        "pos": {
            "x": 528,
            "y": 322
        },
        "scale": {
            "x": 1.5,
            "y": 1.5
        },
        "elementGroup": [{
            "pos": {
                "x": 0,
                "y": 0
            },
            "element": elements
        }]
    }
    return json.dumps(result)
