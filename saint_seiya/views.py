import requests
from django.shortcuts import render

def saints_api(request):
    url = "https://www.saintseiyaapi.com/api/"
    characters = []

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        characters = data.get("data", {}).get("characters", [])
    except requests.exceptions.RequestException as e:
        print("Request error:", e)
    except ValueError as e:
        print("JSON decode error:", e)

    return render(request, "saint_seiya/saints.html", {"characters": characters})