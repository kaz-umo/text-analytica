import nltk
import os

# Локальный путь
local_nltk_data = os.path.join(os.getcwd(), 'nltk_data')
os.makedirs(local_nltk_data, exist_ok=True)

# Указание путей, где NLTK будет искать данные
nltk.data.path.append(local_nltk_data)
nltk.data.path.append('/app/nltk_data')  # для Heroku

# Загрузка необходимых пакетов
nltk.download('punkt', download_dir=local_nltk_data)
nltk.download('stopwords', download_dir=local_nltk_data)

# Проверка загрузки моделей для языков
languages = ['english', 'russian', 'german', 'french', 'spanish', 'italian', 'turkish']

for lang in languages:
    try:
        tokenizer = nltk.data.load(f'tokenizers/punkt/{lang}.pickle')
        print(f"{lang}.pickle успешно загружен.")
    except LookupError as e:
        print(f"Ошибка при загрузке модели для {lang}: {e}")
