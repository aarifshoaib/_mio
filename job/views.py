from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Job
from job import models
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.generic import TemplateView
import base64
import logging



db_logger = logging.getLogger('db_logger')

def url_encode_func(url, encode=True):
    if encode:
        return base64.urlsafe_b64encode(url.encode()).decode()
    return base64.urlsafe_b64decode(url.encode()).decode()

class JobsList(View):
    template_name = 'job/job_list.html';
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
        query = models.Job.objects.all()

        # Handle search filtering
        if keyword:
            try:
                if 'id=' in keyword:
                    id = self.col2num(keyword.split('=')[1])
                    query = query.filter(id=id)
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
        paginator = Paginator(query.order_by('id'), self.PAGINATION_SIZE)
        page_number = request.GET.get('page', 1)
        try:
            jobs_page = paginator.get_page(page_number)
        except PageNotAnInteger:
            jobs_page = paginator.page(1)
        except EmptyPage:
            jobs_page = paginator.page(paginator.num_pages)

        # Prepare context for rendering
        context = {
            'jobs': jobs_page,
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



def job_list(request):
    if request.method == 'POST':
        # Handle form submission
        job_title = request.POST.get('job_title')
        department = request.POST.get('department')
        job_type = request.POST.get('job_type')
        status = request.POST.get('status')
        description = request.POST.get('description')

        # Save the new job to the database
        Job.objects.create(
            title=job_title,
            department=department,
            job_type=job_type,
            status=status,
            description=description
        )
        
        # Redirect to the same job list page
        return redirect('job:job-list')  # Correct redirect

    # Get all jobs to display in the table
    jobs = Job.objects.all()
    return render(request, 'job/job_list.html', {'jobs': jobs})

def job_edit(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":
        job.title = request.POST.get('job_title')
        job.department = request.POST.get('department')
        job.job_type = request.POST.get('job_type')
        job.status = request.POST.get('status')
        job.description = request.POST.get('description')
        job.save()

        # Redirect using the correct namespace 'job'
        return redirect('job:job-list')  # Correct redirect

    return render(request, 'job/job_edit.html', {'job': job})

def job_delete(request, id):
    job = get_object_or_404(Job, id=id)

    if request.method == "POST":
        job.delete()
        return redirect('job:job-list')  # Correct redirect

    return render(request, 'job/job_confirm_delete.html', {'job': job})