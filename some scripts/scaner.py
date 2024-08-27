import cv2
from pyzbar.pyzbar import decode

def preprocess_image(image):
    """Применяет предварительную обработку изображения для улучшения распознавания."""
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Применение фильтра Гаусса для сглаживания
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    # Увеличение контраста
    _, binary_image = cv2.threshold(blurred_image, 128, 255, cv2.THRESH_BINARY)
    return binary_image

def decode_datamatrix(image):
    """Распознает только Data Matrix коды на изображении."""
    codes = decode(image)
    results = []

    for code in codes:
        if code.type == 'DATAMATRIX':
            code_data = {
                'data': code.data.decode('utf-8'),
                'rect': code.rect
            }
            results.append(code_data)

    return results

def main(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Ошибка загрузки изображения.")
        return

    processed_image = preprocess_image(image)
    datamatrix_codes = decode_datamatrix(processed_image)

    if datamatrix_codes:
        print(f"Найдено {len(datamatrix_codes)} Data Matrix кодов:")
        for idx, code in enumerate(datamatrix_codes):
            print(f"Data Matrix код {idx + 1}:")
            print(f"Данные: {code['data']}")
            print(f"Координаты: {code['rect']}")
    else:
        print("Data Matrix коды не найдены.")

# Пример вызова функции
image_path = 'ImportedPhoto_1724409619817.jpg'  # Укажите путь к вашему изображению
main(image_path)
