from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
# Create your views here.


class Login(View):
    template_name = 'auth/login.html'
    def get(self, request):
        return render(request, self.template_name)

class CheckAuthenticateSecretKeyAPI(View):
    def post(self, request):
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            print (username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                response_data = {'status': 'success', 'msg': 'LoggedIn', 'login': True, 'otp_input': True}
            else:
                response_data = {'status': 'error', 'msg': 'Invalid username or password', 'login': False, 'otp_input': False}
        except Exception as e:
            response_data = {'status': 'error', 'msg': f'Error: {e}', 'login': False, 'otp_input': False}
        return JsonResponse(response_data)
    
class AgentsList(View):
    template_name = 'pages/crm/leads.html';
    leads = [
        {
            "lead_name": "Collins",
            "company_name": "NovaWave LLC",
            "company_image": "assets/img/icons/company-icon-01.svg",
            "company_address": "Newyork, USA",
            "phone": "+1 875455453",
            "email": "robertson@example.com",
            "created_date": "25 Sep 2023, 01:22 pm",
            "owner": "Hendry",
            "status": "Closed"
        },
        {
            "lead_name": "Konopelski",
            "company_name": "BlueSky Industries",
            "company_image": "assets/img/icons/company-icon-02.svg",
            "company_address": "Winchester, KY",
            "phone": "+1 989757485",
            "email": "sharon@example.com",
            "created_date": "29 Sep 2023, 04:15 pm",
            "owner": "Guillory",
            "status": "Not Contacted"
        },
        {
            "lead_name": "Adams",
            "company_name": "SilverHawk",
            "company_image": "assets/img/icons/company-icon-03.svg",
            "company_address": "Jametown, NY",
            "phone": "+1 546555455",
            "email": "vaughan12@example.com",
            "created_date": "04 Oct 2023, 10:18 am",
            "owner": "Jami",
            "status": "Closed"
        },
        {
            "lead_name": "Schumm",
            "company_name": "SummitPeak",
            "company_image": "assets/img/icons/company-icon-04.svg",
            "company_address": "Compton, RI",
            "phone": "+1 454478787",
            "email": "jessica13@example.com",
            "created_date": "17 Oct 2023, 03:31 pm",
            "owner": "Theresa",
            "status": "Contacted"
        },
        {
            "lead_name": "Wisozk",
            "company_name": "RiverStone Ventur",
            "company_image": "assets/img/icons/company-icon-05.svg",
            "company_address": "Dayton, OH",
            "phone": "+1 124547845",
            "email": "caroltho3@example.com",
            "created_date": "24 Oct 2023, 09:14 pm",
            "owner": "Espinosa",
            "status": "Closed"
        },
        {
            "lead_name": "Heller",
            "company_name": "Bright Bridge Grp",
            "company_image": "assets/img/icons/company-icon-06.svg",
            "company_address": "Lafayette, LA",
            "phone": "+1 478845447",
            "email": "dawnmercha@example.com",
            "created_date": "08 Nov 2023, 09:56 am",
            "owner": "Martin",
            "status": "Closed"
        },
        {
            "lead_name": "Gutkowski",
            "company_name": "CoastalStar Co.",
            "company_image": "assets/img/icons/company-icon-07.svg",
            "company_address": "Centerville, VA",
            "phone": "+1 215544845",
            "email": "rachel@example.com",
            "created_date": "14 Nov 2023, 04:19 pm",
            "owner": "Newell",
            "status": "Closed"
        },
        {
            "lead_name": "Walter",
            "company_name": "HarborView",
            "company_image": "assets/img/icons/company-icon-08.svg",
            "company_address": "Providence, RI",
            "phone": "+1 121145471",
            "email": "jonelle@example.com",
            "created_date": "23 Nov 2023, 11:14 pm",
            "owner": "Janet",
            "status": "Closed"
        },
        {
            "lead_name": "Hansen",
            "company_name": "Golden Gate Ltd",
            "company_image": "assets/img/icons/company-icon-09.svg",
            "company_address": "Swayzee, IN",
            "phone": "+1 321454789",
            "email": "jonathan@example.com",
            "created_date": "10 Dec 2023, 06:43 am",
            "owner": "Craig",
            "status": "Closed"
        },
        {
            "lead_name": "Leuschke",
            "company_name": "Redwood Inc",
            "company_image": "assets/img/icons/company-icon-10.svg",
            "company_address": "Florida City, FL",
            "phone": "+1 278907145",
            "email": "brook@example.com",
            "created_date": "25 Dec 2023, 08:17 pm",
            "owner": "Daniel",
            "status": "Lost"
        },
    ]
    def get(self, request):
        return render(request, self.template_name, {'leads': self.leads})