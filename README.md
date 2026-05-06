# Employee Analytics Tool

## 📖 Introduction
**Employee Analytics Tool** là một công cụ xử lý và phân tích dữ liệu nhân sự được viết bằng Python. Dự án áp dụng triệt để các nguyên lý Lập trình Hướng đối tượng (OOP) để tách biệt logic I/O và logic tính toán, mang lại một kiến trúc phần mềm sạch sẽ, dễ bảo trì và mở rộng. 

**Employee Analytics Tool** is a Python-based tool for processing and analyzing HR data. The project strictly applies Object-Oriented Programming (OOP) principles to separate I/O logic from computation logic, resulting in a clean, maintainable, and extensible software architecture.

Công cụ sử dụng sức mạnh tính toán vector hóa của **Pandas** và **NumPy** để xử lý tập dữ liệu lớn một cách tối ưu.
*   **Quản lý Dữ liệu (I/O):** Đọc dữ liệu nhân viên từ file CSV và xuất báo cáo kết quả một cách tự động, xử lý các ngoại lệ (exceptions) an toàn.  
    **Data Management (I/O):** Read employee data from CSV files and automatically export result reports, handling exceptions safely.
*   **Lọc Dữ liệu Động (Dynamic Filtering):** Cung cấp cơ chế lọc đa điều kiện linh hoạt lấy cảm hứng từ ORM (như `>=, <=, IN, LIKE`) thông qua *Dynamic Suffixing*.  
    **Dynamic Data Filtering:** Provides a flexible multi-condition filtering mechanism inspired by ORM (such as `>=, <=, IN, LIKE`) via *Dynamic Suffixing*.
*   **Phân tích Thống kê:** Nhóm và tính toán các chỉ số thống kê cơ bản theo phòng ban (lương trung bình, max/min, tổng số nhân viên).  
    **Statistical Analysis:** Group and calculate basic statistical metrics by department (average salary, max/min, total employees).
*   **Kiến trúc Clean Code:** Đảm bảo Single Responsibility Principle (SRP) giữa module điều khiển, xử lý logic và quản lý file.  
    **Clean Code Architecture:** Ensures the Single Responsibility Principle (SRP) between controller, logic processing, and file management modules.
*   **Phân tích Thống kê:** Nhóm và tính toán các chỉ số thống kê cơ bản theo phòng ban (lương trung bình, max/min, tổng số nhân viên).
*   **Thư viện:** 
  * `pandas` (Xử lý DataFrame và Filtering)
  * `numpy` (Tính toán các metric thống kê)
*   **Ngôn ngữ:** Python 3.8+
*   **Thư viện:** 
    *   `pandas` (Xử lý DataFrame và Filtering)
    *   `numpy` (Tính toán các metric thống kê)

## 📂 Project Structure

```
employee_analytics_tool/
├── data/                       
│   ├── input/employees.csv     # Dữ liệu đầu vào
│   └── output/report.csv       # Báo cáo được tạo ra
├── src/                        
│   ├── __init__.py
│   ├── data_manager.py         # Module Load/Export file
│   ├── analytics_engine.py     # Module xử lý logic lọc và thống kê
│   └── main.py                 # File thực thi chính (Controller)
├── .gitignore                  
├── requirements.txt            
└── README.md