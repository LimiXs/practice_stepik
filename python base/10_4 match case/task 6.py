"""
https://stepik.org/lesson/988843/step/7?unit=996328
"""


def parse_json(data):
    match data:
        case {'access': access, 'data': [_, {'login': str(login), 'email': str(email)}, *_]} if access:
            return login, email
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None


json_data = {
    'id': 2,
    'access': True,
    'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]
}
