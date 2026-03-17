import re

def clean_text(text):
    """
    Базовая функция очистки текста для ИСаТ.
    """
    if not text:
        return ""
    
    # 1. Приводим к нижнему регистру
    text = text.lower()
    
    # 2. Удаляем все символы, кроме букв и пробелов (убираем спецсимволы и цифры)
    text = re.sub(r'[^а-яёa-z\s]', '', text)
    
    # 3. Убираем лишние пробелы
    text = " ".join(text.split())
    
    return text