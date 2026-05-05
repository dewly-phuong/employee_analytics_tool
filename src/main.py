import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

class EmployeeAnalyticsTool:

    def __init__(self, data_manager, analytics_engine):
        self.data_manager = data_manager
        self.analytics_engine = analytics_engine
    
    