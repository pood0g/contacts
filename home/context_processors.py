from main.constants import constants
from django.urls import reverse_lazy

def page_data(request):
    
    page_variables = {
        "SITE_TITLE": constants['SITE_TITLE'],
        "nav_items": [{
            "title": app[0].capitalize(),
            "url": (url := reverse_lazy(app[0])),
            "icon": app[1],
            "active": "active" if request.path == url else ""
            }
        for app in constants['NAVBAR_ITEMS']]
    }
    
    return page_variables