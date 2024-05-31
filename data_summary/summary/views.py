import os
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from django.core.files.storage import FileSystemStorage

def load_data(file_path):
    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        data = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type. Please provide a CSV or Excel file.")
    return data

def generate_summary_report(data):
    summary = {}
    summary['Data Types'] = data.dtypes.to_dict()
    summary['Statistics'] = data.describe(include='all').to_dict()
    summary['Missing Values'] = data.isnull().sum().to_dict()
    summary['Unique Values'] = data.nunique().to_dict()
    summary['First Few Rows'] = data.head().to_dict(orient='records')
    return summary

def summary_view(request):
    if request.method == 'POST' and request.FILES['datafile']:
        datafile = request.FILES['datafile']
        fs = FileSystemStorage()
        filename = fs.save(datafile.name, datafile)
        file_path = fs.path(filename)
        
        try:
            data = load_data(file_path)
            summary = generate_summary_report(data)
        except ValueError as e:
            return HttpResponse(f"Error: {e}")
        finally:
            os.remove(file_path)  # Clean up uploaded file
        
        return render(request, 'summary/summary.html', {'summary': summary})
    return render(request, 'summary/upload.html')
