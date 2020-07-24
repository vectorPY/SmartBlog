from django.shortcuts import (render,
                              redirect,
                              get_object_or_404)
from .forms import CreateIdeaForm, DeleteIdeaForm
from .models import Idea


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
        "form": form
    }

    return render(response, "create_idea.html", context)


def idea_list(response):
    ideas = Idea.objects.all()

    context = {
        "ideas": ideas
    }

    return render(response, "list_ideas.html", context)


def delete_idea(response, pk):
    idea = get_object_or_404(Idea, pk=pk)

    if response.method == 'POST':
        form = DeleteIdeaForm(response.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.deleted_by = response.user
            instance.idea = pk
            instance.save()

            idea.delete()

            return redirect('../../ideas')
    else:
        form = DeleteIdeaForm()

    context = {
        "form": form,
        "idea": idea
    }

    return render(response, "delete_idea.html", context)
