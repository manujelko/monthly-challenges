from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

MONTH_NOT_SUPPORTED = HttpResponseNotFound("<h1>This month is not supported!</h1>")

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Do at least 30 pushups every day!",
    "may": "Bike for at least 30 minutes every day!",
    "june": "Sunbathe for 20 minutes every day!",
    "july": "Swim for at least 20 minutes every day!",
    "august": "Read at least 20 pages each day!",
    "september": "Run for at least 20 minutes each day!",
    "october": "Do handstands for at least 20 minutes each day!",
    "november": "Learn Python for at least 30 minutes each day!",
    "december": "Learn HTML/CSS for at least 30 minutes each day!",
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    try:
        redirect_month = months[month - 1]
    except IndexError:
        return MONTH_NOT_SUPPORTED

    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month_name": month.capitalize()},
        )
    except KeyError:
        return MONTH_NOT_SUPPORTED


def index(request):
    list_items = ""

    for month in monthly_challenges:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f"<ul>{list_items}</li>"
    return HttpResponse(response_data)
