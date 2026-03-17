import os
import nltk
from django.shortcuts import render
from django.core.files.storage import default_storage
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# ➤ Указываем пути к nltk_data:
nltk.data.path.append(os.path.join(os.getcwd(), 'nltk_data'))
nltk.data.path.append('/app/nltk_data')  # для Heroku

# ➤ Проверяем и при необходимости скачиваем нужные ресурсы
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', download_dir=nltk.data.path[0])

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', download_dir=nltk.data.path[0])

# ➤ Список языков для обработки
supported_languages = [
    'english', 'russian', 'german', 'french', 'spanish', 'italian', 'kazakh', 'turkish',
]

def upload_text(request):
    context = {}

    if request.method == 'POST' and request.FILES.get('text_file'):
        uploaded_file = request.FILES['text_file']
        selected_language = request.POST.get('language', 'english')  # язык из формы, по умолчанию english

        if selected_language not in supported_languages:
            context['error'] = f"Выбран неподдерживаемый язык: {selected_language}"
            return render(request, 'upload.html', context)

        file_path = default_storage.save(uploaded_file.name, uploaded_file)
        full_path = os.path.join(default_storage.location, file_path)

        # Чтение текста
        with open(full_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Токенизация
        tokens = word_tokenize(text, language=selected_language if selected_language != 'kazakh' else 'english')

        # Удаление стоп-слов (для казахского нет стандартного списка в nltk, поэтому для него пропускаем)
        if selected_language in stopwords.fileids():
            stop_words = set(stopwords.words(selected_language))
            filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
        else:
            filtered_tokens = tokens  # без удаления стоп-слов для языков без списка

        context.update({
            'text': text,
            'tokens': tokens,
            'filtered_tokens': filtered_tokens,
            'token_count': len(tokens),
            'filtered_count': len(filtered_tokens),
            'language': selected_language
        })

    context['supported_languages'] = supported_languages
    return render(request, 'upload.html', context)
