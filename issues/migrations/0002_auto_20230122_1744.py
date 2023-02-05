

from django.db import migrations


def populate_status(apps, schemedotor):
    statuses = {
        "to do": "An isue that has not yet been started",
        "in progress": "An isue in active development",
        "done": "An issuethat has been marked as complete"
    }
    Status = apps.get_model("issues", "Status")
    for name, desc in statuses.items():
        status_obj = Status(name=name, description=desc)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        {"issues", "0001_initial"},
    ]


    operations =[migrations.RunPython(populate_status)]