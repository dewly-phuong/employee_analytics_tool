import unittest
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from analytics_engine import AnalyticsEngine


class TestAnalyticsEngine(unittest.TestCase):
    def setUp(self):
        self.engine = AnalyticsEngine()
        self.sample_data = pd.DataFrame(
            {
                "MaNV": ["NV001", "NV002", "NV003"],
                "HoTen": ["Nguyen Van A", "Tran Thi B", "Le Van C"],
                "NgaySinh": ["1990-05-15", "1993-08-22", "1988-11-02"],
                "SoDienThoai": ["0901234567", "0912345678", "0923456789"],
                "Email": ["nva@congty.com", "ttb@congty.com", "lvc@congty.com"],
                "PhongBan": ["IT", "HR", "Ke toan"],
                "ChucVu": ["Truong phong", "Chuyen vien", "Ke toan truong"],
                "MucLuong": [35000000, 18000000, 28000000],
                "MucThuong": [5000000, 2000000, 4000000],
            }
        )

    def test_filter_employees_eq(self):
        result = self.engine.filter_employees(self.sample_data, PhongBan="IT")
        self.assertEqual(len(result), 1)
        self.assertEqual(result.iloc[0]["MaNV"], "NV001")

    def test_filter_employees_gt(self):
        result = self.engine.filter_employees(self.sample_data, MucLuong__gt=20000000)
        self.assertEqual(len(result), 2)  # NV001 and NV003

    def test_filter_employees_lt(self):
        result = self.engine.filter_employees(self.sample_data, MucLuong__lt=30000000)
        self.assertEqual(len(result), 2)  # NV002 and NV003

    def test_filter_employees_gte(self):
        result = self.engine.filter_employees(self.sample_data, MucLuong__gte=28000000)
        self.assertEqual(len(result), 2)  # NV001 and NV003

    def test_filter_employees_lte(self):
        result = self.engine.filter_employees(self.sample_data, MucLuong__lte=18000000)
        self.assertEqual(len(result), 1)  # NV002

    def test_calculate_department_stats(self):
        result = self.engine.calculate_department_stats(self.sample_data)
        self.assertIn("IT", result.index)
        self.assertEqual(result.loc["IT", "SoLuongNhanVien"], 1)
        self.assertEqual(result.loc["IT", "LuongTrungBinh"], 35000000)

    def test_get_summary_metrics(self):
        result = self.engine.get_summary_metrics(self.sample_data)
        self.assertEqual(result.iloc[0]["TongSoNhanVien"], 3)
        self.assertEqual(result.iloc[0]["TongSoLuong"], 81000000)
        self.assertEqual(result.iloc[0]["TongSoThuong"], 11000000)


if __name__ == "__main__":
    unittest.main()
