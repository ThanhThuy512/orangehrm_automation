from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EmployeePage(BasePage):
    # Định danh các phần tử
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']") # => Locator ô input tìm tên nhân viên
    SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Search']")            # => Nút để tìm kiếm
    EMPLOYEE_ROWS = (By.CSS_SELECTOR, "div.oxd-table-body div.oxd-table-card")    # => Hàng trong bảng kết quả tìm được

    def search_employee(self, name):      # => Gọi 2 thao tác: nhập tên + bấm search
        """
        Nhập tên nhân viên và thực hiện tìm kiếm
        """
        self.enter_text(*self.EMPLOYEE_NAME_INPUT, name)  # Nhập tên
        self.click(*self.SEARCH_BUTTON)                   # Nhấn nút Search

    def get_search_results_count(self):                   # => Trả về số hàng kết quả tìm được
        """
        Đếm số kết quả (hàng trong bảng kết quả)
        """
        rows = self.find_all_elements(*self.EMPLOYEE_ROWS)
        return len(rows)

