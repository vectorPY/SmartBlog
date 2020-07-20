from django.shortcuts import render, redirect
from .forms import (BannedForm,
                    ExemptionRequestForm,
                    WarnUserForm,
                    BanFromPartOfBlogForm)
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

    if banned_group in user.groups.all():
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
                print("Sent!")
                instance.save()
        else:
            form = ExemptionRequestForm()

        context = {
            "form": form,
            "user": user
        }
        return render(response, "exemRequ.html", context)

    else:
        return redirect('../../home')


def warn_user_view(response, user):
    user_obj = User.objects.filter(username=user).first()
    if response.method == 'POST':
        form = WarnUserForm(response.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.banned_by = response.user
            instance.user = user
            instance.save()

            send_mail(
                f"You were warned by {response.user}",
                instance.reason,
                "muellergoldmann@gmail.com",
                [user_obj.email]
            )
            return redirect("../../home")

    else:
        form = WarnUserForm()

    context = {
        "user": user_obj,
        "form": form
    }
    return render(response, "warn_user.html", context)


def ban_part_of_blog_view(response, user):
    user_obj = User.objects.filter(username=user).first()

    if response.method == 'POST':
        form = BanFromPartOfBlogForm(response.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user
            instance.banned_by = response.user
            instance.save()

            part = form.cleaned_data['part']

            if part == "Comments":
                comment_group = Group.objects.get(name="comment_ban")
                comment_group.user_set.add(user_obj.id)

            elif part == "Write":
                write_group = Group.objects.get(name="write_ban")
                write_group.user_set.add(user_obj.id)

            elif part == 'Read':
                read_group = Group.objects.get(name="read_ban")
                read_group.user_set.add(user_obj.id)

            return redirect('../../home')

    else:
        form = BanFromPartOfBlogForm()

    context = {
        "form": form,
        "user": user_obj
    }

    return render(response, "ban_part_of_blog.html", context)
