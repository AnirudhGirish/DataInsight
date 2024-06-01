from django.shortcuts import render
from django.contrib import messages
import pandas as pd

def summary_view(request):
    if request.method == 'POST' and request.FILES.get('datafile'):
        datafile = request.FILES['datafile']

        try:
            if datafile.name.endswith('.csv'):
                df = pd.read_csv(datafile)
            elif datafile.name.endswith('.xls') or datafile.name.endswith('.xlsx'):
                df = pd.read_excel(datafile)
            else:
                messages.error(request, 'File format not supported. Please upload a CSV or Excel file.')
                return render(request, 'summary/upload.html')

            summary = generate_summary(df)
            return render(request, 'summary/summary.html', {'summary': summary})

        except Exception as e:
            messages.error(request, f'Error processing file: {e}')
            return render(request, 'summary/upload.html')

    return render(request, 'summary/upload.html')

def generate_summary(df):
    summary = {
        'Data_Types': df.dtypes.apply(lambda x: x.name).to_dict(),
        'Statistics': df.describe(include='all').to_dict(),
        'Missing_Values': df.isnull().sum().to_dict(),
        'Unique_Values': df.nunique().to_dict(),
        'First_Few_Rows': df.head().to_dict(orient='records')
    }
    return summary
