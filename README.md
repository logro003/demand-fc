# Scooter demand next day forecasting in Voiholm

## Poetry set up: 
Why use poetry for package and dependency management:
- Simple to use
- Easy to configuring

Make sure you have poetry installed (https://pypi.org/project/poetry/)

To create virtual environment:
```
poetry install
```

To activate virtual environment using poetry:
```
poetry shell
```

To add packages:
```
poetry add package-name
```

To update dependencies: 
```
poetry update
```

## Code structure overview for case presentation

- project_root/

    - app/
        - config.py         # Configurations for model features and hyperparameters  
        - main.py           # Runs training and prediction

    - demand_forecasting/
        - features.py       # Script for creating features for the model
        - predict.py        # Script for making predictions for next day
        - preprocess.py     # Script for data preprocessing
        - read.py           # Script for reading the input data
        - train.py          # Script for training the ML model
        - verify.py         # Script for verifying the dataframes

    - input/                # Raw input data

    - output/               # Model prediction output data

    - notebooks/            # Jupyter notebooks for exploration and analysis

    - tests/                # Unit tests

    - poetry.lock            # ? Dependencies file
    - pypoetry.toml          # ? 
    - README.md              # Project documentation
    -.gitignore             # Gitignore file
    -.env                   # Environment variables for what data to include in traning and for which date to make predictions

## Running tests
Run all tests by
```
 poetry run pytest
```

## Running application locally
```
poetry run python app/main.py
```

## Docker 
The image contains the folders app and demand forecasting and necessary files for poetry. See Dockerfile.

To build image: 
```
docker build -t demand_forecast_image .

```
To run image with input files from input folder and saving predictions to output folder:
```
docker run -v $(pwd)/output:/demand_forecast/output -v $(pwd)/input:/demand_forecast/input --env-file .env demand_forecast_image 
```
