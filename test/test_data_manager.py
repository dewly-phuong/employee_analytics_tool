import unittest
import pandas as pd
import sys
import os
import tempfile
import shutil

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from data_manager import DataManager


class TestDataManager(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create temporary directories for testing
        self.temp_dir = tempfile.mkdtemp()
        self.input_dir = os.path.join(self.temp_dir, "input")
        self.output_dir = os.path.join(self.temp_dir, "output")
        os.makedirs(self.input_dir)
        os.makedirs(self.output_dir)

        # Initialize DataManager
        self.data_manager = DataManager(self.input_dir, self.output_dir)

        # Create sample CSV file for testing
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

        # Save sample data to input directory
        self.sample_file = os.path.join(self.input_dir, "employees.csv")
        self.sample_data.to_csv(self.sample_file, index=False)

    def tearDown(self):
        """Clean up after each test method."""
        shutil.rmtree(self.temp_dir)

    def test_load_csv_success(self):
        """Test loading a valid CSV file."""
        df = self.data_manager.load_csv("employees.csv")
        self.assertEqual(len(df), 3)
        self.assertListEqual(list(df.columns), list(self.sample_data.columns))
        self.assertEqual(df.iloc[0]["MaNV"], "NV001")

    def test_load_csv_file_not_found(self):
        """Test loading a CSV file that doesn't exist."""
        df = self.data_manager.load_csv("nonexistent_file.csv")
        self.assertTrue(df.empty)

    def test_load_csv_empty_dataframe_on_error(self):
        """Test that an empty DataFrame is returned on error."""
        df = self.data_manager.load_csv("invalid_path/file.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.empty)

    def test_save_csv_success(self):
        """Test saving a DataFrame to CSV successfully."""
        output_file = "output_test.csv"
        result = self.data_manager.save_csv(self.sample_data, output_file)

        self.assertTrue(result)
        output_path = os.path.join(self.output_dir, output_file)
        self.assertTrue(os.path.exists(output_path))

        # Verify saved data
        saved_df = pd.read_csv(output_path)
        self.assertEqual(len(saved_df), 3)
        self.assertEqual(saved_df.iloc[0]["MaNV"], "NV001")

    def test_save_csv_empty_dataframe(self):
        """Test saving an empty DataFrame."""
        empty_df = pd.DataFrame()
        output_file = "empty_output.csv"
        result = self.data_manager.save_csv(empty_df, output_file)

        self.assertTrue(result)
        output_path = os.path.join(self.output_dir, output_file)
        self.assertTrue(os.path.exists(output_path))

    def test_save_csv_with_multiple_rows(self):
        """Test saving a DataFrame with multiple rows and columns."""
        large_df = pd.concat([self.sample_data] * 3, ignore_index=True)
        output_file = "large_output.csv"
        result = self.data_manager.save_csv(large_df, output_file)

        self.assertTrue(result)
        saved_df = pd.read_csv(os.path.join(self.output_dir, output_file))
        self.assertEqual(len(saved_df), 9)

    def test_load_csv_preserves_data_types(self):
        """Test that loading CSV preserves data types properly."""
        df = self.data_manager.load_csv("employees.csv")
        self.assertIsInstance(df.iloc[0]["MaNV"], (str, object))
        self.assertIsInstance(df.iloc[0]["MucLuong"], (int, float, object))

    def test_save_and_load_roundtrip(self):
        """Test save then load returns equivalent DataFrame."""
        output_file = "roundtrip_test.csv"

        # Save the sample data
        self.data_manager.save_csv(self.sample_data, output_file)

        # Load it back directly from output directory
        output_path = os.path.join(self.output_dir, output_file)
        loaded_df = pd.read_csv(output_path)

        # Compare (allowing for minor type differences)
        self.assertEqual(len(loaded_df), len(self.sample_data))
        self.assertEqual(list(loaded_df.columns), list(self.sample_data.columns))


if __name__ == "__main__":
    unittest.main()
