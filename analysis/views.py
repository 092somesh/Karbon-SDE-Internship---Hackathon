import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
from .model import probe_model_5l_profit

def home(request):
    """
    Render the home page.
    """
    return render(request, 'home.html')

def upload_file(request):
    """
    Handle file upload and process the JSON data for financial analysis.
    """
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                # Save uploaded file to a specific location
                with open('data.json', 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)

                # Load data from the saved file
                with open("data.json", "r", encoding='utf-8') as file:
                    content = file.read()
                    data = json.loads(content)

                # Call model function to get evaluated financial flags
                flags = probe_model_5l_profit(data["data"])
                print(flags)  # Debugging output

                # Save the financial flags data as a new JSON file
                with open("result_data.json", "w", encoding='utf-8') as result_file:
                    json.dump(flags, result_file, indent=4)

                # Render the results page with flags data
                return render(request, 'result.html', {'flags': flags})
            except json.JSONDecodeError as e:
                print(f"JSON decoding error: {e}")
                return render(request, 'error.html', {'error_message': "Invalid JSON file format."})
            except Exception as e:
                print(f"An error occurred while rendering: {e}")
                return render(request, 'error.html', {'error_message': str(e)})
        else:
            return redirect(request.path_info)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})