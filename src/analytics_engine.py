import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

class AnalyticsEngine:
    def __init__(self):
        pass

    def filter_employees(self, df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        """
        Lọc nhân viên theo điều kiện động 
        kwargs: column__operator=value
        (ví dụ: age_gt=30, department='Engineering'). 
        operator có thể là: eq || (bằng), gt (lớn hơn), 
        lt (nhỏ hơn), gte (lớn hơn hoặc bằng), lte (nhỏ hơn hoặc bằng).
        Trả về một DataFrame mới đã được lọc.
        """
        logging.info("Filtering data")
        try:
            feature_df = df.copy()
            for key, value in kwargs.items():
                if "__" in key:
                    column, operator = key.split("__")
                else: 
                    column, operator = key, 'eq'
                match operator:
                    case 'eq': feature_df = feature_df[feature_df[column] == value]
                    case 'gt': feature_df = feature_df[feature_df[column] > value]
                    case 'lt': feature_df = feature_df[feature_df[column] < value]
                    case 'gte': feature_df = feature_df[feature_df[column] >= value]
                    case 'lte': feature_df = feature_df[feature_df[column] <= value]
            return feature_df

        except Exception as e:
            logging.error(f"Error occurred while filtering data: {e}")
            return pd.DataFrame()

    def calculate_department_stats(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Nhiệm vụ: Group by theo department. Sử dụng NumPy để tính toán các metrics 
        (ví dụ: np.mean cho lương trung bình, np.max cho lương cao nhất, đếm số lượng nhân viên).
        """
        logging.info("Calculate department stats")
        try:
            grouped_df = df.copy()
            grouped_df = grouped_df.groupby('PhongBan').agg(
                SoLuongNhanVien = ('MaNV', 'count'),
                LuongTrungBinh = ('MucLuong', np.mean),
                LuongCaoNhat = ('MucLuong', np.max),
                LuongThapNhat = ('MucLuong', np.min)
            )
            return grouped_df
        except Exception as e:
            logging.error(f"Error occurred while calculating department stats: {e}")
            return pd.DataFrame()

    def get_summary_metrics(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Trả về một số thống kê tổng quan (tổng nhân viên, độ tuổi trung bình toàn công ty, v.v.).
        """
        logging.info("Calculate summary statiticals of employees")
        try:
            summary = {
                'TongSoNhanVien': len(df),
                'TongSoLuong': df['MucLuong'].sum(),
                'TongSoThuong': df['MucThuong'].sum()
            }
            summary_df = pd.DataFrame([summary])
            return summary_df
        except Exception as e:
            logging.error(f"Error occurred while calculating summary metrics: {e}")
            return pd.DataFrame()
