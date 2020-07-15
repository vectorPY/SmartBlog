from django.shortcuts import render, redirect
from .forms import BannedForm, ExemptionRequestForm
from django.contrib.auth.models import Group, User
from django.core.mail import send_mail


# Create your views here.
def ban_view(response, user):
    if response.method == 'POST':
        form = BannedForm(response.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.banned_by = response.user

            instance.user = user
            banned_group = Group.objects.get(name="banned")
            ban_user: User = User.objects.filter(username=user).first()
            banned_group.user_set.add(ban_user.id)

            instance.save()

            return redirect("../../home")

    else:
        form = BannedForm()

    context = {
        "form": form
    }
    return render(response, "ban_view.html", context)


def exemption_request_view(response, user):
    user: User = User.objects.filter(username=user).first()
    banned_group: Group = Group.objects.get(name="banned")

    if user in banned_group:
        if response.method == 'POST':
            form = ExemptionRequestForm(response.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = user.username

                send_mail(
                    f"Exemption Request of {user.username}",
                    instance.reason,
                    'vector.thedev@gmail.com',
                    ['muellergoldmann@gmail.com']
                )

                instance.save()
    else:
        return redirect('../../home')
