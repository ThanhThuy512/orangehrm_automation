# tests/test_search_employee.py / Kiểm tra khả năng tìm nhanh trên Dashboard bằng ô search

import allure
#from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.login_helpers import login_success

@allure.title("Tìm kiếm nhanh trên dashboard")
@allure.description("Nhập từ khóa 'Leave' vào ô tìm kiếm và xác minh kết quả")
def test_quick_search(driver):
   # login = LoginPage(driver)
    login_success(driver)  # 👈 Chỉ 1 dòng gọi login
    dashboard = DashboardPage(driver)

#    with allure.step("Đăng nhập vào trang OrangeHRM"):
#       login.open()
#        login.login("Admin", "admin123")

    with allure.step("Tìm kiếm từ khóa 'Leave'"):
        dashboard.search_in_dashboard("Leave")  # => Gõ từ "Leave" vào ô tìm kiếm trên dashboard

    with allure.step("Kiểm tra kết quả có liên quan"):
        assert "Leave" in driver.page_source  # => Kiểm tra có kết quả liên quan đến "Leave" được hiển thị trên trang
