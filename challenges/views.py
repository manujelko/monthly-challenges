from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None,
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    try:
        redirect_month = months[month - 1]
    except IndexError:
        raise Http404()

    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month_name": month},
        )
    except KeyError:
        raise Http404()


def index(request):
    months = list(monthly_challenges)
    return render(request, "challenges/index.html", {"months": months})
