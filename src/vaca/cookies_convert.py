import json

def cookie_str_to_dict(cookie_str):
    cookie_dict = {}
    for cookie in cookie_str.split(";"):
        key, value = cookie.split("=")
        cookie_dict[key] = value
    return cookie_dict


def cookie_dict_to_str(cookie_dict_x):
    cookie_dict_x=cookie_dict_x.replace("'", "\"")
    cookie_dict=json.loads(cookie_dict_x)
    cookie_header = ";".join([f"{key}={value}" for key, value in cookie_dict.items()])
    return cookie_header
