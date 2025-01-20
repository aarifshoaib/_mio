from django.shortcuts import render,redirect
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from mio_customer import models  # Assuming the models are in this module
import logging
from django.views.generic import TemplateView
from django.views import View
from mio_customer.models import tbl_customer

import base64

# Create your views here.
db_logger = logging.getLogger('db_logger')
def url_encode_func(url, encode=True):
    if encode:
        return base64.urlsafe_b64encode(url.encode()).decode()
    return base64.urlsafe_b64decode(url.encode()).decode()

class CustomerList(TemplateView):
    template_name = 'pages/customer/customer_list.html'  # This can be omitted if you're directly passing the template to render
    PAGINATION_SIZE = 25

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
        query = models.tbl_customer.objects.all()

        # Apply pagination
        paginator = Paginator(query.order_by('id'), self.PAGINATION_SIZE)
        page_number = request.GET.get('page', 1)
        try:
            customers_page = paginator.get_page(page_number)
        except PageNotAnInteger:
            customers_page = paginator.page(1)
        except EmptyPage:
            customers_page = paginator.page(paginator.num_pages)

        # Prepare context for rendering
        context = {
            'customers': customers_page,
            'current_url': current_url,
            'keyword': keyword,
            'result_cnt': query.count(),
            'return_url': url_encode_func(request.get_full_path()),  # Ensure `url_encode_func` is defined elsewhere
        }

        # Log user activity
        db_logger.info(f'<b style="color:red">{request.user}</b>: Accessed Customer List Page')

        # Render the response with the correct template
        return render(request, 'pages/customer/customer_list.html', context=context)


class CreateCustomer(View):
    def post(self, request, *args, **kwargs):
        # Get data from the form
        name = request.POST.get('customer_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        customer_type = request.POST.get('customer_type')
        industry = request.POST.get('industry')
        tags = request.POST.get('tags')
        notes = request.POST.get('notes')
        visibility = request.POST.get('visibility')
        status = request.POST.get('status')

        # Save new customer to the database
        new_customer = tbl_customer(
            name=name,
            email=email,
            phone=phone,
            address=address,
            customer_type=customer_type,
            industry=industry,
            tags=tags,
            notes=notes,
            visibility=visibility,
            status=status
        )
        new_customer.save()

        # Redirect to the customer list page
        return redirect('customer-list')  # Replace with the actual URL name for customer list page
