from django.shortcuts import render

# 🔹 Главная страница с анализом текста
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


# 🔹 Заглушки для всех модулей
def m1_basic(request):
    return render(request, "analyzer/m1_basic.html")

def m2_lexical(request):
    return render(request, "analyzer/m2_lexical.html")

def m3_semantic(request):
    return render(request, "analyzer/m3_semantic.html")

def m4_topic(request):
    return render(request, "analyzer/m4_topic.html")

def m5_evaluation(request):
    return render(request, "analyzer/m5_evaluation.html")

def m6_context(request):
    return render(request, "analyzer/m6_context.html")