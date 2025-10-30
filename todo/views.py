from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def home(request):
    tasks = Task.objects.order_by('-created_at')
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('home')
    return render(request, 'todo/home.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('home')



from django.shortcuts import render
from .models import User

def register_user(request):
    message = None
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        # Save user (fires signal)
        try:
            User.objects.create(name=name, email=email)
            message = f"✅ {name} registered successfully!"

        except Exception as e:
            message = f"❌ Error: {e}"
        else:
            return redirect('home')

    return render(request, "todo/register.html", {"message": message})




# from .signals import user_registered
# from .models import User

# def register_user(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         user = User.objects.create(name=name, email=email)

#         # 👇 Fire the signal manually
#         user_registered.send(sender=User, instance=user)
#         print("🚀 Signal sent!")

#     return render(request, "todo/register.html")
