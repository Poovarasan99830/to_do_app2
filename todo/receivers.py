


# from django.dispatch import receiver
# from django.core.mail import send_mail
# from .signals import user_registered
# from .models import ActivityLog

# @receiver(user_registered)
# def send_welcome_email(sender, instance, **kwargs):
#     subject = "Welcome to Smart AI Civic Portal!"
#     message = f"Hi {instance.name},\n\nWelcome! Your account has been created successfully."
#     from_email = "kingpoovarasan49@gmail.com"
#     recipient_list = [instance.email]
#     print("📨 Inside send_welcome_email receiver...")


#     try:
#         print("📨 Inside send_welcome_email receiver...")

#         send_mail(
#             subject,
#             message,
#             from_email,
#             recipient_list,
#             fail_silently=False  # this shows actual error in console
#         )
#         print(f"📧 Email successfully sent to {instance.email}")
#     except Exception as e:
#         print(f"❌ Email send failed: {e}")

# @receiver(user_registered)
# def log_user_creation(sender, instance, **kwargs):
#     ActivityLog.objects.create(
#         user=instance,
#         action=f"User '{instance.name}' created successfully."
#     )
#     print(f"🪵 Log saved for {instance.name}")

# @receiver(user_registered)
# def update_analytics(sender, instance, **kwargs):
#     print(f"📊 Analytics updated for {instance.name}")
