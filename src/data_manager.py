import pandas as pd

class DataManager:
    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path

    def load_csv(self, file_name: str) -> pd.DataFrame:
        """
        Đọc file CSV bằng Pandas và trả về DataFrame.
        """
        pass

    def save_csv(self, df: pd.DataFrame, file_name: str) -> bool:
        """
        Ghi DataFrame thành file CSV. Trả về True nếu thành công.
        """
        pass