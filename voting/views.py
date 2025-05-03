from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Entry, Vote
import random

# Create your views here.
def index(request):
    # Get the session ID or create one if it doesn't exist
    if not request.session.session_key:
        request.session.save()
    session_id = request.session.session_key

    # Get all entries
    all_entries = list(Entry.objects.all())

    # If there are fewer than two entries, display a message
    if len(all_entries) < 2:
        return render(request, 'voting/not_enough_entries.html')
    
    # Select 2 random entries
    entries = random.sample(all_entries, 2)

    context = {
        'entry1': entries[0],
        'entry2': entries[1],
    }

    return render(request, 'voting/index.html', context)

def vote(request, entry_id):
    if request.method == 'POST':
        if not request.session.session_key:
            request.session.save()
        session_id = request.session.session_key

        # Record the vote
        entry = Entry.objects.get(pk=entry_id)
        Vote.objects.create(entry=entry, session_id=session_id)
        
        return redirect('index')
    
    return redirect('index')