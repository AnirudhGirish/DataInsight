# Data Insight

Data Insight is a Django-based web application designed to provide comprehensive data analysis and summary reports from `CSV` or `Excel` files. This tool enables users to upload their data files and quickly receive detailed insights, including data types, statistics, missing values, unique values, and a preview of the data. 

## Features

- **File Upload**: Supports uploading of `CSV` and `Excel` files directly from the browser.
- **Data Analysis**: Automatically analyzes the uploaded data to provide a detailed summary.
- **User-Friendly Interface**: Simple and intuitive interface for uploading files and viewing results.
- **No File Storage**: Processes files in-memory without saving them to the server for improved security and performance.

## Installation

To get started with Data Insight, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/AnirudhGirish/DataInsight.git
    cd datainsight
    ```

2. **Set up a virtual environment**:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip3 install -r requirements.txt
    ```

4. **Apply the migrations**:
    ```sh
    python3 manage.py migrate
    ```

5. **Run the development server**:
    ```sh
    python3 manage.py runserver
    ```

6. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

1. **Upload Data File**:
    - Navigate to the home page.
    - Click on the "Upload Data File" button.
    - Select a CSV or Excel file from your computer.
    - Click the "Upload" button to submit the file.

2. **View Data Summary**:
    - After uploading the file, you will be redirected to a summary page.
    - The summary includes:
        - Data types of each column.
        - Descriptive statistics (mean, standard deviation, min, max, etc.).
        - Count of missing values per column.
        - Count of unique values per column.
        - Preview of the first few rows of the dataset.



## Tech Stack

**Frontend:** `HTML, CSS, JavaScript`

**Backend:** `Django`

**Database:** `SQLite3`

## Acknowledgements

- [Pandas](https://pandas.pydata.org/) for data analysis.
- [Django](https://www.djangoproject.com/) for the web framework.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## Support

For support, email anirudhgirish08@gmail.com.