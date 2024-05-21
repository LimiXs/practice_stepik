"""
https://stepik.org/lesson/988837/step/7?unit=996322
"""
t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case (_, author, name) if len(author) >= 6 and len(name) >= 10:
        print("Yes")
    case (_, author, name, price) if len(author) >= 6 and price > 0:
        print("Yes")
    case (_, author, name, _, year) if year >= 2020:
        print("Yes")
    case (_, author, name, price, year) if price > 0 and year >= 2020:
        print("Yes")
    case _:
        print("No")
