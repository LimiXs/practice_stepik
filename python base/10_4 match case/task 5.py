"""
https://stepik.org/lesson/988843/step/6?unit=996328
"""


def parse_json(data):
    match data:
        case {'id': ids, 'access': bool() as access, 'data': list(data)}:
            return access, data[0]
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None


json_data = {
    'id': 2,
    'access': False,
    'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]
}
