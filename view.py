from django.shortcuts import render
from .forms import UploadForm
from .models import File_upload, FormData
import csv 

# Create your views here.
def upload(request):
    form = UploadForm(request.POST, request.FILES) 
    if form.is_valid():
        form.save()
        form = UploadForm()
        obj = File_upload.objects.get(id=1)
        
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            print(reader)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    name = row[1]
                    field_1 = row[2]
                    FormData.objects.create(
                        name=name, field_1=field_1
                    )
                    print(row)
                    
    return render(request, 'store/main.html', {'form':form})
