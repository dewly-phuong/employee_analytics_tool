import logging

logging.basicConfig(level=logging.INFO)


class EmployeeAnalyticsTool:
    def __init__(self, data_manager, analytics_engine):
        self.data_manager = data_manager
        self.analytics_engine = analytics_engine

    def runner(self, input_file: str, output_file: str):
        logging.info("Starting Employee Analytics Tool")
        # Load data
        df = self.data_manager.load_csv(input_file)
        if df.empty:
            logging.warning("No data to process.")
            return

        # Tính toán thống kê theo phòng ban
        department_stats_df = self.analytics_engine.calculate_department_stats(df)

        # Lưu kết quả vào file CSV
        success = self.data_manager.save_csv(department_stats_df, output_file)
        if success:
            logging.info("Employee Analytics Tool completed successfully.")
        else:
            logging.error("Employee Analytics Tool failed to save results.")
