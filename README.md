# Scooter demand forecasting in Voiholm

## Set up
Why use poetry for package and dependency management:
- simple to use
- easy to configuring

Poetry set up: 
Make sure you have poetry installed (add link)

To create virtual environment:
```
poetry install
```

How to activate virtual environment using poetry:
```
poetry shell
```

How to add packages:
```
poetry add package-name
```

How to update dependencies: 
```
poetry update 
```

## Code structure overview

project_root/
│
├── demand_forecasting/
│   ├── features.py       # Script for creating features for the model
│   ├── train.py          # Script for training the ML model
│   ├── predict.py        # Script for making predictions
│   ├── preprocess.py     # Script for data preprocessing
│   ├── read.py           # Script for reading the data
|   ├── verify.py         # Script for verifying the dataframes
│
├── input/                # Raw input data
|
├── output/               # Model prediction output data
│
├── notebooks/            # Jupyter notebooks for exploration and analysis
│
├── tests/                 # Unit tests
│
├── poetry.lock            # ? Dependencies file
├── pypoetry.toml          # ? 
├── README.md              # Project documentation
├── .gitignore             # Gitignore file