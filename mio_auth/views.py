import base64
from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.generic import TemplateView
import logging

from mio_agents import models

# Create your views here.


db_logger = logging.getLogger('db_logger')

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
    
def url_encode_func(url, encode=True):
    if encode:
        return base64.urlsafe_b64encode(url.encode()).decode()
    return base64.urlsafe_b64decode(url.encode()).decode()

class NewAgent(TemplateView):
    template_name = 'pages/modal/new-agent.html'
    def get(self, request, *args, **kwargs):
        context = {
            'open_modal': True
        }   
        return render(request, self.template_name, context=context)
    
class AgentsList(View):
    template_name = 'pages/agents/agents-list.html';
    PAGINATION_SIZE = 25

    def col2num(self, col: str) -> int:
        import string
        if not all(c.isalpha() for c in col):
            raise ValueError(f"Invalid column name: {col}")
        num = 0
        for c in col.upper():
            num = num * 26 + (ord(c) - ord('A')) + 1
        return num - 1

    def get(self, request):
        keyword = request.GET.get('keyword', '').strip()
        get_url = request.get_full_path()
        
        if '?keyword' in get_url:
            get_url = get_url.split('&page=')[0]
            current_url = f"{get_url}&"
        else:
            get_url = get_url.split('?')[0]
            current_url = f"{get_url}?"

        # Initialize the base query
        query = models.AgentManagementNewAgentModel.objects.all()

        # Handle search filtering
        if keyword:
            try:
                if 'id=' in keyword:
                    agent_id = self.col2num(keyword.split('=')[1])
                    query = query.filter(agent_id=agent_id)
                else:
                    query = query.filter(
                        Q(name__icontains=keyword) |
                        Q(phone__icontains=keyword) |
                        Q(district__icontains=keyword) |
                        Q(place__icontains=keyword)
                    )
            except Exception as e:
                db_logger.error(f"Error in keyword search: {e}")
                return JsonResponse({'status': 'error', 'message': 'Invalid search keyword'}, status=400)

        # Apply pagination
        paginator = Paginator(query.order_by('agent_id'), self.PAGINATION_SIZE)
        page_number = request.GET.get('page', 1)
        try:
            agents_page = paginator.get_page(page_number)
        except PageNotAnInteger:
            agents_page = paginator.page(1)
        except EmptyPage:
            agents_page = paginator.page(paginator.num_pages)

        # Prepare context for rendering
        context = {
            'agents': agents_page,
            'current_url': current_url,
            'keyword': keyword,
            'result_cnt': query.count(),
            'return_url': url_encode_func(request.get_full_path()),  # Ensure `url_encode_func` is defined elsewhere
        }
        print (context)
        # Log user activity
        db_logger.info(f'<b style="color:red">{request.user}</b>: Accessed Agent List Page')

        # Render the response
        return render(request, self.template_name, context=context)
