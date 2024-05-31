import os
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile

def load_data(file: InMemoryUploadedFile):
    file_extension = file.name.split('.')[-1].lower()
    if file_extension == 'csv':
        data = pd.read_csv(file)
    elif file_extension in ['xlsx', 'xls']:
        data = pd.read_excel(file)
    else:
        raise ValueError("Unsupported file type. Please provide a CSV or Excel file.")
    return data

def generate_summary_report(data: pd.DataFrame):
    summary = {
        'Data Types': data.dtypes.to_dict(),
        'Statistics': data.describe(include='all').to_dict(),
        'Missing Values': data.isnull().sum().to_dict(),
        'Unique Values': data.nunique().to_dict(),
        'First Few Rows': data.head().to_dict(orient='records')
    }
    return summary

def summary_view(request):
    if request.method == 'POST' and request.FILES.get('datafile'):
        datafile = request.FILES['datafile']
        
        try:
            data = load_data(datafile)
            summary = generate_summary_report(data)
        except ValueError as e:
            return HttpResponse(f"Error: {e}")

        return render(request, 'summary/summary.html', {'summary': summary})
    return render(request, 'summary/upload.html')
