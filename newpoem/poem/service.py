from .models import  Poem

def getAllPoems():
    return Poem.objects.all()