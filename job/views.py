from django.shortcuts import render, get_object_or_404, redirect
from .models import Job

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