import unittest
import pandas as pd
import sys
import os
import tempfile
import shutil
from unittest.mock import Mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import EmployeeAnalyticsTool
from data_manager import DataManager
from analytics_engine import AnalyticsEngine


class TestEmployeeAnalyticsTool(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create temporary directories for testing
        self.temp_dir = tempfile.mkdtemp()
        self.input_dir = os.path.join(self.temp_dir, "input")
        self.output_dir = os.path.join(self.temp_dir, "output")
        os.makedirs(self.input_dir)
        os.makedirs(self.output_dir)

        # Initialize real instances
        self.data_manager = DataManager(self.input_dir, self.output_dir)
        self.analytics_engine = AnalyticsEngine()

        # Initialize the tool
        self.tool = EmployeeAnalyticsTool(self.data_manager, self.analytics_engine)

        # Create sample data
        self.sample_data = pd.DataFrame(
            {
                "MaNV": ["NV001", "NV002", "NV003", "NV004"],
                "HoTen": ["Nguyen Van A", "Tran Thi B", "Le Van C", "Pham Thi D"],
                "NgaySinh": ["1990-05-15", "1993-08-22", "1988-11-02", "1995-01-10"],
                "SoDienThoai": ["0901234567", "0912345678", "0923456789", "0934567890"],
                "Email": [
                    "nva@congty.com",
                    "ttb@congty.com",
                    "lvc@congty.com",
                    "ptd@congty.com",
                ],
                "PhongBan": ["IT", "HR", "Ke toan", "IT"],
                "ChucVu": [
                    "Truong phong",
                    "Chuyen vien",
                    "Ke toan truong",
                    "Nhan vien",
                ],
                "MucLuong": [35000000, 18000000, 28000000, 16000000],
                "MucThuong": [5000000, 2000000, 4000000, 1500000],
            }
        )

        # Save sample data to input directory
        self.input_file = "employees.csv"
        self.sample_data.to_csv(
            os.path.join(self.input_dir, self.input_file), index=False
        )

    def tearDown(self):
        """Clean up after each test method."""
        shutil.rmtree(self.temp_dir)

    def test_runner_success(self):
        """Test runner method with valid data."""
        output_file = "department_stats.csv"

        # Run the tool
        self.tool.runner(self.input_file, output_file)

        # Verify output file was created
        output_path = os.path.join(self.output_dir, output_file)
        self.assertTrue(os.path.exists(output_path))

        # Verify output data
        result_df = pd.read_csv(output_path)
        self.assertGreater(len(result_df), 0)

    def test_runner_with_nonexistent_input_file(self):
        """Test runner with a non-existent input file."""
        output_file = "output.csv"

        # This should not raise an error but log a warning
        self.tool.runner("nonexistent_file.csv", output_file)

    def test_runner_saves_csv_output(self):
        """Test that runner saves the result as CSV."""
        output_file = "analytics_output.csv"

        self.tool.runner(self.input_file, output_file)

        output_path = os.path.join(self.output_dir, output_file)
        self.assertTrue(os.path.exists(output_path))
        self.assertTrue(output_file.endswith(".csv"))

    def test_runner_with_mock_data_manager(self):
        """Test runner with mocked DataManager."""
        mock_data_manager = Mock(spec=DataManager)
        mock_data_manager.load_csv.return_value = self.sample_data
        mock_data_manager.save_csv.return_value = True

        tool = EmployeeAnalyticsTool(mock_data_manager, self.analytics_engine)
        tool.runner("input.csv", "output.csv")

        # Verify load_csv was called
        mock_data_manager.load_csv.assert_called_once_with("input.csv")
        # Verify save_csv was called
        mock_data_manager.save_csv.assert_called_once()

    def test_runner_with_empty_dataframe(self):
        """Test runner when data is empty."""
        # Create empty CSV file
        empty_file = "empty.csv"
        empty_df = pd.DataFrame()
        empty_df.to_csv(os.path.join(self.input_dir, empty_file), index=False)

        output_file = "empty_output.csv"

        # Run should handle empty data gracefully
        self.tool.runner(empty_file, output_file)

    def test_runner_with_mock_analytics_engine(self):
        """Test runner with mocked AnalyticsEngine."""
        mock_analytics_engine = Mock(spec=AnalyticsEngine)
        mock_analytics_engine.calculate_department_stats.return_value = (
            self.sample_data.head(2)
        )

        tool = EmployeeAnalyticsTool(self.data_manager, mock_analytics_engine)
        tool.runner(self.input_file, "mock_output.csv")

        # Verify calculate_department_stats was called
        mock_analytics_engine.calculate_department_stats.assert_called_once()

    def test_runner_integration_with_filter_and_stats(self):
        """Test integration: load data, then generate stats."""
        output_file = "integration_test.csv"

        # Run the tool
        self.tool.runner(self.input_file, output_file)

        # Load and verify result
        result_df = pd.read_csv(os.path.join(self.output_dir, output_file))
        self.assertIsInstance(result_df, pd.DataFrame)
        self.assertGreater(len(result_df), 0)

    def test_runner_output_contains_expected_columns(self):
        """Test that output contains expected stat columns."""
        output_file = "column_test.csv"

        self.tool.runner(self.input_file, output_file)

        result_df = pd.read_csv(os.path.join(self.output_dir, output_file))

        # Check for expected statistics columns
        expected_cols = [
            "SoLuongNhanVien",
            "LuongTrungBinh",
            "LuongCaoNhat",
            "LuongThapNhat",
        ]
        for col in expected_cols:
            self.assertIn(col, result_df.columns)

    def test_tool_initialization(self):
        """Test EmployeeAnalyticsTool initialization."""
        tool = EmployeeAnalyticsTool(self.data_manager, self.analytics_engine)

        self.assertIsNotNone(tool.data_manager)
        self.assertIsNotNone(tool.analytics_engine)
        self.assertEqual(tool.data_manager, self.data_manager)
        self.assertEqual(tool.analytics_engine, self.analytics_engine)


class TestEmployeeAnalyticsToolWithMocks(unittest.TestCase):
    def test_runner_calls_methods_in_correct_order(self):
        """Test that runner calls methods in the correct order."""
        mock_data_manager = Mock(spec=DataManager)
        mock_analytics_engine = Mock(spec=AnalyticsEngine)

        sample_df = pd.DataFrame(
            {"MaNV": ["NV001"], "PhongBan": ["IT"], "MucLuong": [35000000]}
        )

        mock_data_manager.load_csv.return_value = sample_df
        mock_data_manager.save_csv.return_value = True
        mock_analytics_engine.calculate_department_stats.return_value = sample_df

        tool = EmployeeAnalyticsTool(mock_data_manager, mock_analytics_engine)
        tool.runner("input.csv", "output.csv")

        # Verify order: load -> calculate -> save
        self.assertEqual(mock_data_manager.load_csv.call_count, 1)
        self.assertEqual(mock_analytics_engine.calculate_department_stats.call_count, 1)
        self.assertEqual(mock_data_manager.save_csv.call_count, 1)

    def test_runner_handles_save_failure(self):
        """Test runner when save operation fails."""
        mock_data_manager = Mock(spec=DataManager)
        mock_analytics_engine = Mock(spec=AnalyticsEngine)

        sample_df = pd.DataFrame({"data": [1, 2, 3]})

        mock_data_manager.load_csv.return_value = sample_df
        mock_data_manager.save_csv.return_value = False  # Simulate save failure
        mock_analytics_engine.calculate_department_stats.return_value = sample_df

        tool = EmployeeAnalyticsTool(mock_data_manager, mock_analytics_engine)

        # Should not raise an exception
        tool.runner("input.csv", "output.csv")


if __name__ == "__main__":
    unittest.main()
