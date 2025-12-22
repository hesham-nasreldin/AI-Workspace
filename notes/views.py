from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Notes


# Create your views here.
@login_required(login_url="my-login")
def notes_index(request):
    if request.method == "POST":
        if "add" in request.POST:
            note_title = request.POST.get("title")
            note_content = request.POST.get("content")

            Notes.objects.create(title=note_title, content=note_content)

            for note in Notes.objects.all():
                print(note.title, note.content)

            redirect("notes_index")
        if "delete" in request.POST:
            note_id = request.POST.get("delete")
            note = get_object_or_404(Notes, id=note_id)
            note.delete()

            redirect("notes_index")

    context = {"notes": Notes.objects.all()}
    return render(request, template_name="notes/index.html", context=context)


@login_required(login_url="my-login")
async def edit_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id)

    context = {
        "note_title": note.title,
        "note_content": note.content,
    }
    if request.method == "POST":

        if "save" in request.POST:
            new_title = request.POST.get("title")
            new_content = request.POST.get("content")

            notes = get_object_or_404(Notes, id=note_id)
            notes.title = new_title
            notes.content = new_content

            notes.save()

            return redirect("notes_index")

    return render(request, "notes/edit.html", context=context)
