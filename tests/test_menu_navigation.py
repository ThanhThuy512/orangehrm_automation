# tests/test_menu_navigation.py/ Kiểm tra danh sách menu sau khi đăng nhập có chứa đầy đủ mục cần thiết không
import allure
#from pages.login_page import LoginPage  # => Gọi lại page object để tái sử dụng hàm login & thao tác dashboard
from utils.login_helpers import login_success
from pages.dashboard_page import DashboardPage

@allure.title("Kiểm tra các mục menu trên Dashboard")
@allure.description("Sau khi đăng nhập, menu bên trái phải hiển thị đúng các mục chính")
def test_menu_items(driver):
    #login = LoginPage(driver)
    login_success(driver)  # 👈 Chỉ 1 dòng gọi login
    dashboard = DashboardPage(driver)

    #with allure.step("Đăng nhập vào hệ thống"):
    #    login.open()
    #    login.login("Admin", "admin123")

    with allure.step("Lấy danh sách tên các mục trong menu"):
        menu_labels = dashboard.get_menu_items_text()  # => Trích danh sách tên các mục trong menu

    with allure.step("Kiểm tra một số mục menu chính phải xuất hiện"):
        assert "Admin" in menu_labels  # => Kiểm tra các mục như "Admin", "PIM" có tồn tại trong menu không.
        assert "PIM" in menu_labels
        assert "Leave" in menu_labels
