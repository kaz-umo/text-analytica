from django.shortcuts import render

def home_view(request):
    text = ""

    if request.method == "POST":
        text = request.POST.get("text", "")

    # Простой анализ текста
    word_count = len(text.split())
    sentence_count = text.count(".") + text.count("!") + text.count("?")
    char_count = len(text)

    context = {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "char_count": char_count,
    }

    return render(request, "analyzer/index.html", context)