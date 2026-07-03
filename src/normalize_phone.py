import re

mock = "(050)8889900"

def normalize_phone(phone_number: str):
    replace = ""
    pattern = r"[^\d+]"
    result = re.sub(pattern, replace, phone_number)

    country = result.find("+38")
    if country == -1:
        result = "+38" + result

    return result


normalize_phone(mock) # +380508889900