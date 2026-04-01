from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DICTIONARY_PATH = ROOT_DIR / "docs"
DATA_PATH_RAW = ROOT_DIR / "data/raw/loan.csv"
DATA_PATH_CLEAN = ROOT_DIR / "data/clean/loan_clean.parquet"
DATA_PATH_PROCESSED = ROOT_DIR / "data/processed/loan_processed.parquet"
DATA_PATH_X_train_BALANCED = ROOT_DIR / "data/processed/loan_X_train.parquet"
DATA_PATH_y_train_BALANCED = ROOT_DIR / "data/processed/loan_y_train.parquet"
DATA_PATH_X_test = ROOT_DIR / "data/processed/loan_X_test.parquet"
DATA_PATH_y_test = ROOT_DIR / "data/processed/loan_y_test.parquet"
ENCODER_PATH = ROOT_DIR / "models/encoder.pkl"
SCALER_PATH = ROOT_DIR / "models/scaler.pkl"
KAGGLE_DATASET = 'ranadeep/credit-risk-dataset'