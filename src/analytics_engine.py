import pandas as pd
import numpy as np

class AnalyticsEngine:
    def __init__(self):
        pass

    def filter_employees(self, df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        """
        Group by theo department. Sử dụng NumPy để tính toán các metrics 
        (ví dụ: np.mean cho lương trung bình, np.max cho lương cao nhất, đếm số lượng nhân viên).
        """
        pass

    def calculate_department_stats(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Nhiệm vụ: Group by theo department. Sử dụng NumPy để tính toán các metrics 
        (ví dụ: np.mean cho lương trung bình, np.max cho lương cao nhất, đếm số lượng nhân viên).
        """
        pass

    def get_summary_metrics(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Trả về một số thống kê tổng quan (tổng nhân viên, độ tuổi trung bình toàn công ty, v.v.).
        """
        pass