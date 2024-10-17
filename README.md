# PDF Unlocker Web Application

This is a Flask-based web application designed to unlock password-protected PDF files. The application allows users to upload a PDF file, check if it is locked, and if necessary, prompt for a password to unlock it. Once unlocked, users can view the PDF content directly in the browser and download the unlocked version.

## Features

- **PDF Upload**: Users can upload a PDF file via a simple drag-and-drop interface or by clicking to browse their files.
- **Password Protection Check**: The application automatically detects if the uploaded PDF is password-protected.
- **Password Input**: If the PDF is locked, users are prompted to enter the password to unlock it.
- **View and Download**: Once the PDF is unlocked, users can view it in the browser and download the unlocked version, with `-unlocked` appended to the original file name.

## Technologies Used

- **Flask**: A lightweight web framework for Python.
- **HTML/CSS**: For the frontend interface.
- **JavaScript**: To handle drag-and-drop functionality for file uploads.
- **PDF Handling**: Libraries for checking password protection and unlocking PDFs.

## Installation

To set up the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/sikandarsubhani/pdf_unlocker
   ```
   
2. Navigate to the project directory:
   ```bash
   cd pdf_unlocker
   ```
   
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
4. Run the application:
   ```bash
   python app.py
   ```

5. Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

1. Upload a PDF file using the upload interface.
2. If prompted, enter the password for the PDF file.
3. View and download the unlocked PDF as needed.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

---
