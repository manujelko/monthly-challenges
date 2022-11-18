from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
        forward_month = months[month - 1]
    except IndexError:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponseRedirect(f"/challenges/{forward_month}")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except KeyError:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge_text)
