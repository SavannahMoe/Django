import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'learning_log.settings') ### this is very important to be in this order, Learning_log is project 

import django
django.setup()

from MainApp.models import Topic, Entry #MainApp is the application

topics = Topic.objects.all() #all gets all filter if specific Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process 

t = Topic.objects.get(id=1)
print(t)
entries=t.entry_set.all() ##because of the foregin key relationship we set in the model 
for entry in entries:       ##if method was Post then it would have been t.post_set.all
    print(entry)
'''
for t in topics:
    print(f"Topic ID: {t.id} Topic: {t}")
#without the str method in models=== allows us to get chess and rock climbing instead of object 1 and 2 

entry = Entry.objects.all()

for e in entry:
    print(f"Topic: {e.topic}")
    print(f"Text: {e.text}")
    print(f"Date: {e.date_added}")

'''