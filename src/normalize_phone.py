import re

mock = "+432 10 123 45 67"

def normalize_phone(phone_number: str):
    replace = ""
    pattern = r"[^\d+]"
    result = re.sub(pattern, replace, phone_number)

    country = result.find("+")
    if country == -1:
        result = "+38" + result

    return result


# Test
print(normalize_phone(mock)) # +432101234567