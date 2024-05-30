# FastAPI PDF Search

This project implements a FastAPI application for searching through PDF documents using Google's Generative AI.

## Installation

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
    ```bash
    git clone <repository_url>
    ```
2. **Navigate to Project Directory**: Move into the project directory after cloning:
    ```bash
    cd <project_directory>
    ```
3. **Create Virtual Environment (Optional)**: It's recommended to create a virtual environment before installing dependencies to isolate them from other projects. You can create a virtual environment using `venv`:
    ```bash
    python3 -m venv myenv
    ```
    Activate the virtual environment:
    - On Windows:
        ```bash
        myenv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source myenv/bin/activate
        ```
4. **Install Dependencies**: Install the required dependencies listed in `requirements.txt` using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the FastAPI Server**: Start the FastAPI server using the following command:
    ```bash
    uvicorn main:app --reload
    ```
2. **Access API Documentation**: Once the server is running, access the API documentation at `http://127.0.0.1:8000/docs`.
3. **Submit PDF and Query**: Use the `/submit` endpoint to upload a PDF file and submit a query.

## Configuration

Before running the server, set your Google API key in the `main.py` file.

