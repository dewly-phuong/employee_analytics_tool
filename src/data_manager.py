import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)


class DataManager:
    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path

    def load_csv(self, file_name: str) -> pd.DataFrame:
        """
        Đọc file CSV bằng Pandas và trả về DataFrame.
        """
        logging.info(f"Loading data from {self.input_path}/{file_name}")
        try:
            df = pd.read_csv(f"{self.input_path}/{file_name}")
            logging.info("Data loaded successfully.")
            return df
        except Exception as e:
            logging.error(f"Error occurred while loading data: {e}")
            return pd.DataFrame()

    def save_csv(self, df: pd.DataFrame, file_name: str) -> bool:
        """
        Ghi DataFrame thành file CSV. Trả về True nếu thành công.
        """
        logging.info(f"Saving data to {self.output_path}/{file_name}")
        try:
            df.to_csv(f"{self.output_path}/{file_name}", index=False)
            logging.info("Data saved successfully.")
            return True
        except Exception as e:
            logging.error(f"Error occurred while saving data: {e}")
            return False
