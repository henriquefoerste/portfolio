# Data Processing Pipeline

## Overview
This project implements a modular and flexible data processing pipeline designed for scalable data preprocessing, transformation, and feature engineering. By applying design patterns such as **Strategy** and **Decorator**, the pipeline allows dynamic selection of preprocessing techniques and efficient performance monitoring. The architecture follows **Domain-Driven Design (DDD)** principles to ensure clear separation of concerns and maintainability.

## Features
- **Data Ingestion:** Load data from CSV files, databases, or APIs.
- **Modular Preprocessing:** Apply customizable data cleaning, transformation, and feature engineering strategies.
- **Performance Monitoring:** Track execution time and log activities using decorators.
- **Configuration Management:** Configure pipeline behavior through YAML files.
- **(Optional) Model Integration:** Train machine learning models using processed data.

## Project Structure
```
data_pipeline_project/
│
├── data/                  
│   ├── raw/               # Raw data files
│   ├── processed/         # Processed data outputs
│   └── external/          # Data from external sources (APIs, databases)
│
├── config/                
│   └── config.yaml        # Configuration file to manage pipeline settings
│
├── pipeline/              
│   ├── __init__.py
│   ├── data_loader.py     # Module to handle data ingestion (CSV, API, DB)
│   ├── pipeline.py        # Main class to manage the pipeline flow
│   └── utils.py           # Helper functions (logging, performance monitoring)
│
├── preprocessing/         
│   ├── __init__.py
│   ├── base_strategy.py   # Abstract base class for preprocessing strategies
│   ├── cleaning.py        # Data cleaning strategies (handle missing values, etc.)
│   ├── transformation.py  # Data transformation strategies (normalize, encode)
│   └── feature_engineering.py  # Feature engineering strategies
│
├── models/                # (Optional) For future integration of ML models
│   ├── __init__.py
│   └── model_trainer.py   # Module to train models on processed data
│
├── tests/                 
│   ├── __init__.py
│   ├── test_data_loader.py
│   ├── test_pipeline.py
│   └── test_preprocessing.py
│
├── logs/                  # Stores log files generated during processing
│
├── notebooks/             # Jupyter notebooks for exploration and testing
│
├── requirements.txt       # List of required Python packages
├── README.md              # Project documentation and usage instructions
└── main.py                # Entry point to run the pipeline
```


## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/henriquefoerste/portfolio.git
   cd portfolio/data_processing_pipeline
   ```

2. **Set up a virtual environment:**
   ```bash
   conda create --name data_pipeline_env python=3.9
   conda activate data_pipeline_env
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Configure the pipeline behavior by modifying the `config/config.yaml` file. This file allows you to select preprocessing strategies and define data sources.

**Example `config.yaml`:**
```yaml
input_data: "data/raw/dataset.csv"
output_data: "data/processed/processed_dataset.csv"

preprocessing:
  cleaning_strategy: "RemoveNulls"
  transformation_strategy: "StandardScaler"
  feature_engineering_strategy: "PolynomialFeatures"
```

## Usage
Run the pipeline using the following command:
```bash
python main.py --config config/config.yaml
```

### Command-Line Arguments:
- `--config`: Path to the configuration file (default: `config/config.yaml`).

## Preprocessing Strategies
The pipeline supports multiple preprocessing strategies that can be easily extended.

1. **Cleaning Strategies:**
   - `RemoveNulls`: Removes rows with null values.
   - `FillMissingValues`: Fills missing values with mean or median.

2. **Transformation Strategies:**
   - `StandardScaler`: Standardizes features by removing the mean and scaling to unit variance.
   - `MinMaxScaler`: Scales features to a given range.

3. **Feature Engineering Strategies:**
   - `PolynomialFeatures`: Generates polynomial and interaction features.
   - `PCA`: Reduces dimensionality using Principal Component Analysis.

## Logging and Monitoring
Execution logs and performance metrics are stored in the `logs/` directory. Decorators are used to track the execution time of each preprocessing step.

## Testing
Run unit tests to ensure each module works correctly:
```bash
pytest tests/
```

## Contributing
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For questions or suggestions, please contact [henriquefoerste@gmail.com](mailto:henriquefoerste@gmail.com).

