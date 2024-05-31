import os
import chardet
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile

def detect_encoding(file):
    raw_data = file.read(10000)
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    print(f"Detected encoding: {encoding}")  # Debug print
    file.seek(0)  # Reset file pointer after reading
    return encoding

def log_file_info(file):
    file.seek(0)
    raw_data = file.read(100)
    print(f"File first 100 bytes: {raw_data}")
    file.seek(0)

def load_data(file: InMemoryUploadedFile):
    file_extension = file.name.split('.')[-1].lower()
    encoding = detect_encoding(file)
    print(f"Trying to read with encoding: {encoding}")  # Debug print
    encodings_to_try = [encoding, 'utf-8', 'ISO-8859-1', 'latin1']
    
    for enc in encodings_to_try:
        try:
            print(f"Attempting to read with encoding: {enc}")  # Debug print
            if file_extension == 'csv':
                data = pd.read_csv(file, encoding=enc)
            elif file_extension in ['xlsx', 'xls']:
                data = pd.read_excel(file)
            else:
                raise ValueError("Unsupported file type. Please provide a CSV or Excel file.")
            
            if data.empty:
                raise ValueError("The file is empty or not properly formatted.")
            
            return data  # Return data if read successfully
        except (UnicodeDecodeError, ValueError) as e:
            print(f"Failed with encoding {enc}: {e}")  # Debug print
            file.seek(0)  # Reset file pointer and try next encoding
            continue
        except Exception as e:
            raise ValueError(f"Could not read the file: {e}")

    # Log file info if all encoding attempts fail
    log_file_info(file)
    raise ValueError("Failed to read the file with available encodings.")

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
