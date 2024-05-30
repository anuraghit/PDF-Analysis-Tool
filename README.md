# FastAPI PDF Search

This project implements a FastAPI application for searching through PDF documents using Google's Generative AI.
![Capture](https://github.com/anuraghit/PDF-Analysis-Tool/assets/57986981/98e72e8f-f6c4-428a-960b-0aad87e3d1eb)

## Installation

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
    ```bash
    git clone https://github.com/anuraghit/pdf-query-form
    ```
2. **Navigate to Project Directory**: Move into the project directory after cloning:
    ```bash
    cd <pdf-query-form>
    ```
3. **Install Dependencies**: Install the required dependencies listed in `requirements.txt` using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the FastAPI Server**: Start the FastAPI server using the following command:
    ```bash
    uvicorn main:app --reload
    ```
2. **Access API Documentation**: Once the server is running, access the API documentation at `http://127.0.0.1:8000/docs`.
3. **Navigate to the frontend directory and install dependencies:
4. ```bash
   cd pdf-query-form/frontend
   npm install
   ```
5. **Submit PDF and Query**: Use the `/submit` endpoint to upload a PDF file and submit a query.

## Configuration

Before running the server, set your Google API key in the `main.py` file.

