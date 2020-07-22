from django.shortcuts import render, redirect
from .forms import CreateIdeaForm


# Create your views here.
def create_idea(response):
    if response.method == 'POST':
        form: CreateIdeaForm = CreateIdeaForm(response.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = response.user
            instance.save()

            return redirect("../../home")

    else:
        form: CreateIdeaForm = CreateIdeaForm()

    context = {
        "form": form,
    }

    return render(response, "create_list.html", context)




