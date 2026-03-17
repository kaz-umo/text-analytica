from django.shortcuts import render


# 🔹 Главная страница с анализом
def home(request):
    text = ""

    if request.method == "POST":
        text = request.POST.get("text", "")

    word_count = len(text.split())
    sentence_count = text.count(".") + text.count("!") + text.count("?")
    char_count = len(text)

    context = {
        "text": text,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "char_count": char_count,
    }

    return render(request, "analyzer/index.html", context)


# 🔹 Остальные страницы (пока заглушки)
def basic_module(request):
    return render(request, "analyzer/basic.html")

def extraction_module(request):
    return render(request, "analyzer/extraction.html")

def statistics_module(request):
    return render(request, "analyzer/statistics.html")

def lexical_module(request):
    return render(request, "analyzer/lexical.html")

def topic_module(request):
    return render(request, "analyzer/topic.html")

def evaluation_module(request):
    return render(request, "analyzer/evaluation.html")

def context_module(request):
    return render(request, "analyzer/context.html")