# FASTag Fraud Detection

This project aims to detect fraudulent FASTag transactions using machine learning. It consists of a machine learning model trained to predict whether a transaction is fraudulent based on various features such as vehicle type, lane type, transaction amount, and more.

## Project Structure

- **FastagFraudDetection.ipynb**: Jupyter notebook containing the data exploration, preprocessing, model training, and evaluation.
- **main.py**: FastAPI application that serves the model and provides an endpoint for predicting fraud.
- **index.html**: HTML file to interact with the FastAPI endpoint for testing fraud detection.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/VatsAmanJha/FASTag-Fraud-Detection.git
    cd fastag-fraud-detection
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the FastAPI application:
    ```sh
    uvicorn main:app --reload
    ```

2. Open `index.html` in your web browser to test the fraud detection.

## Usage

### FastagFraudDetection.ipynb

- **Data Exploration**: The notebook includes detailed steps for exploring the dataset, visualizing different features, and understanding the distribution of data.
- **Data Preprocessing**: Steps for handling missing values, encoding categorical variables, and scaling numerical features.
- **Model Training**: Training an XGBoost model to detect fraudulent transactions.
- **Model Evaluation**: Evaluating the model's performance using metrics such as accuracy, precision, recall, and F1-score.

### main.py

- **FastAPI Setup**: Initializes a FastAPI application with a single endpoint `/predict` for fraud detection.
- **Prediction Endpoint**: Accepts a JSON payload with transaction details and returns whether the transaction is fraudulent or not.
- **CORS Configuration**: Allows requests from specified origins to interact with the FastAPI server.

### index.html

- **Form Submission**: A simple web form to input transaction details and send a request to the FastAPI endpoint.
- **Result Display**: Displays the prediction result received from the server.

## Example

To test the application:

1. Run the FastAPI server using:
    ```sh
    uvicorn main:app --reload
    ```

2. Open `index.html` in a web browser.

3. Fill in the form with transaction details and submit to see the prediction result.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## Acknowledgments

- Thanks to the contributors and the open-source community for their invaluable support.
- Special thanks to the developers of FastAPI and XGBoost for their excellent tools.
