# **Insurance Account value prediction**

This repository contains code and resources for building predictive models to estimate account values within the framework of company insurance. The primary goal of this project is to develop accurate machine learning algorithms that can forecast the future account values for insurance policies held by the company.

**Key Features**:

    Data Processing: Includes scripts and notebooks for cleaning, preprocessing, and transforming raw insurance data into a suitable format for modeling.
    Model Development: Provides implementations of various machine learning algorithms, such as regression models, ensemble methods, and neural networks, tailored for predicting account values.
    Evaluation Metrics: Includes functions for evaluating model performance using appropriate metrics such as RMSE (Root Mean Squared Error), MAE (Mean Absolute Error), and R-squared.
    Documentation: Contains detailed documentation and tutorials explaining the data sources, preprocessing steps, model selection criteria, and interpretation of results.
    Deployment: Offers guidance on deploying trained models into production environments, including considerations for scalability, performance, and maintainability.

**How to Run This Code**:

## 1. Cloning the Repository

To clone this repository, use the following command:

```bash
git clone https://github.com/SMoralesS/insurance-account-value-prediction
cd insurance-account-value-prediction
```
## 2. Running the App
### Docker

To run the FastAPI app in a Docker container, follow these steps:

- 2.1 Build the Docker image:

    ```bash
        docker build -t acount_value_api .
    ```

- 2.2 Run the Docker container:

    ```bash
      docker run -d --name my_fastapi_container -p 80:80 my_fastapi_app
    ```

This will start the FastAPI app inside a Docker container, and it will be accessible at http://localhost:80 in your browser.
    
### Locally

To run the FastAPI app locally, follow these steps:

- 2.1 Install dependencies:

    ```bash
      pip install -r requirements.txt
    ```

- 2.2 Run the app:

    ```bash
      uvicorn main:app --reload
    ```
    
The app will start locally and will be accessible at http://localhost:8000 in your browser.

**Contributing**:

Contributions to this repository are welcome! Whether you're interested in improving data preprocessing pipelines, experimenting with new modeling techniques, or enhancing documentation, your contributions can help advance the accuracy and usability of the predictive models developed in this project.

**License**:

This project is licensed under the MIT License, which means you are free to use, modify, and distribute the code for both commercial and non-commercial purposes. See the LICENSE file for more details.

**Disclaimer**:

Please note that while the models developed in this repository strive to provide accurate predictions, they should be used for informational and research purposes only. Actual account values may vary due to various factors not accounted for in the modeling process, and users should exercise caution when making decisions based on model predictions.
