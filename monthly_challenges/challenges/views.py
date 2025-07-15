from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .constants import CHALLENGE_BY_NAME, CHALLENGES_HOME
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django at least 20 minutes every day!",
    "april": "Read for 30 minutes every day!",
    "may": "Exercise for 45 minutes daily!",
    "june": "Drink 8 glasses of water daily!",
    "july": "Practice meditation for 15 minutes!",
    "august": "Write in a journal every evening!",
    "september": "Learn something new for 30 minutes!",
    "october": "Take a photo every day!",
    "november": "Practice gratitude daily!",
    "december": None
    # "december": "Help someone every day!"
}

def index(request):
    months = list(monthly_challenges.keys())
    # html_content = "<h1>Monthly Challenges</h1>"
    #
    # for month in months:
    #     month_url = reverse(CHALLENGE_BY_NAME, args=[month])
    #     html_content += f'<li><a href="{month_url}">{month.capitalize()}</a></li>'
    #
    # html_content += "</ul>"
    return render(request, "challenges/index.html", {
        "months": months,
        "challenge_by_name_url": CHALLENGE_BY_NAME,
        "home_url": CHALLENGES_HOME,
    })

def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys()) #[] of challenges
        redirect_month = months[month - 1 if month > 1 else 0]
        redirect_path = reverse(CHALLENGE_BY_NAME, args=[redirect_month]) # /challenges
        # return HttpResponse(monthly_challenges[forward_month])
        return HttpResponseRedirect(redirect_path)
    except IndexError:
        return HttpResponseNotFound("Invalid month!")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_title": month,
            "home_url": CHALLENGES_HOME,
        })
    except KeyError:
        # raise Http404("This month is not supported!")
        response_data = render_to_string("404.html", {
            "home_url": CHALLENGES_HOME,
        })
        return HttpResponseNotFound(response_data)

