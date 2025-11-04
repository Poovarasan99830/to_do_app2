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



# from django.shortcuts import render
# from .models import User

# def register_user(request):
#     message = None
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")

#         # Save user (fires signal)
#         try:
#             User.objects.create(name=name, email=email)
#             message = f"✅ {name} registered successfully!"

#         except Exception as e:
#             message = f"❌ Error: {e}"
#         else:
#             return redirect('home')

    # return render(request, "todo/register.html", {"message": message})




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
# views.py
# import random
# from django.core.mail import send_mail
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
# from .models import UserOTP

# def register_user(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         if User.objects.filter(username=username).exists():
#             return render(request, "todo/register.html", {"message": "⚠️ Username already exists!"})

#         user = User.objects.create_user(username=username, email=email, password=password)
#         otp = str(random.randint(100000, 999999))
#         UserOTP.objects.create(user=user, otp=otp)

#         # ✅ Send OTP to email
#         send_mail(
#             "Your Smart AI Civic Portal OTP",
#             f"Hi {username},\n\nYour OTP is {otp}. It will expire in 5 minutes.\n\nThank you!",
#             "kingpoovarasan49@gmail.com",
#             [email],
#             fail_silently=False,
#         )

#         return redirect("verify_otp")

#     return render(request, "todo/register.html")


# # from django.contrib.auth import login
# # from django.contrib.auth.models import User

# # def verify_otp(request):
# #     if request.method == "POST":
# #         email = request.POST.get("email")
# #         otp_entered = request.POST.get("otp")

# #         user = User.objects.get(email=email)
# #         user_otp = UserOTP.objects.get(user=user)

# #         if user_otp.is_expired():
# #             user_otp.delete()
# #             return render(request, "todo/verify_otp.html", {"message": "❌ OTP expired! Please register again.", "email": email})

# #         if user_otp.otp == otp_entered:
# #             login(request, user)
# #             user_otp.delete()
# #             return redirect("home")
# #         else:
# #             return render(request, "todo/verify_otp.html", {"message": "❌ Invalid OTP!", "email": email})

# #     return render(request, "todo/verify_otp.html")



# from django.contrib.auth import login
# from django.contrib.auth.models import User
# from .models import UserOTP

# def verify_otp(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         otp_entered = request.POST.get("otp")

#         # ✅ Fetch multiple users safely
#         users = User.objects.filter(email=email).order_by("-id")
#         if not users.exists():
#             return render(request, "todo/verify_otp.html", {
#                 "message": "❌ No user found with this email.",
#                 "email": email
#             })

#         user = users.first()  # pick the most recent user

#         try:
#             user_otp = UserOTP.objects.get(user=user)
#         except UserOTP.DoesNotExist:
#             return render(request, "todo/verify_otp.html", {
#                 "message": "❌ OTP not found for this user.",
#                 "email": email
#             })

#         # ✅ Expiry check
#         if user_otp.is_expired():
#             user_otp.delete()
#             return render(request, "todo/verify_otp.html", {
#                 "message": "⏰ OTP expired! Please register again.",
#                 "email": email
#             })

#         # ✅ OTP match check
#         if user_otp.otp == otp_entered:
#             login(request, user)
#             user_otp.delete()
#             return redirect("home")
#         else:
#             return render(request, "todo/verify_otp.html", {
#                 "message": "❌ Invalid OTP! Please try again.",
#                 "email": email
#             })

#     return render(request, "todo/verify_otp.html")




import random
import threading
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.mail import send_mail
from .models import UserOTP
from django.conf import settings

def send_async_email(subject, message, recipient_list):
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False
        )
    except Exception as e:
        print("Email sending failed:", e)

def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"message": "⚠️ Username already exists!"})

        user = User.objects.create_user(username=username, email=email, password=password)
        otp = str(random.randint(100000, 999999))
        UserOTP.objects.create(user=user, otp=otp)

        threading.Thread(
            target=send_async_email,
            args=("Your Smart AI Civic Portal OTP",
                  f"Hi {username},\n\nYour OTP is {otp}. It will expire in 5 minutes.\n\nThank you!",
                  [email])
        ).start()

        return redirect("verify_otp")

    return render(request, "register.html")


def verify_otp(request):
    if request.method == "POST":
        email = request.POST.get("email")
        otp_entered = request.POST.get("otp")

        users = User.objects.filter(email=email).order_by("-id")
        if not users.exists():
            return render(request, "verify_otp.html", {"message": "❌ No user found with this email.", "email": email})

        user = users.first()

        try:
            user_otp = UserOTP.objects.get(user=user)
        except UserOTP.DoesNotExist:
            return render(request, "verify_otp.html", {"message": "❌ OTP not found.", "email": email})

        if user_otp.is_expired():
            user_otp.delete()
            return render(request, "verify_otp.html", {"message": "⏰ OTP expired!", "email": email})

        if user_otp.otp == otp_entered:
            login(request, user)
            user_otp.delete()
            return redirect("home")
        else:
            return render(request, "verify_otp.html", {"message": "❌ Invalid OTP!", "email": email})

    return render(request, "verify_otp.html")
