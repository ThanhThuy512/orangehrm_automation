# tests/test_login.py – viết test case đăng nhập
# ✅ Mục tiêu:
# Mỗi test chia thành bước rõ ràng
# Có ghi chú cho Allure report
# Kiểm tra kết quả bằng assert

import allure
from pages.login_page import LoginPage
from utils.helpers import capture_screenshot

@allure.title("Đăng nhập OrangeHRM thành công")
@allure.description("Test đăng nhập với tài khoản mặc định: Admin/admin123")
def test_login_success(driver):
    # Tạo đối tượng trang Login để thao tác
    login_page = LoginPage(driver)

    with allure.step("Mở trang đăng nhập"):
        login_page.open()                        # Truy cập vào trang login
        assert "OrangeHRM" in driver.title       # Kiểm tra tiêu đề trang đúng

    with allure.step("Nhập username & password"):
        login_page.login("Admin", "admin123")    # Gọi hàm login

    with allure.step("Kiểm tra đăng nhập thành công"):
        # assert "dashboard" in driver.current_url.lower() or "Dashboard" in driver.page_source
        # Kiểm tra chuyển trang hoặc nội dung xác nhận login thành công

        try:  # try...except => Đảm bảo ảnh vẫn được chụp khi test fail
            assert "dashboard" in driver.current_url.lower()
            capture_screenshot(driver, "Dashboard sau khi login")  # => Gọi hàm chụp ảnh, hàm chụp ảnh này chỉ cần gọi bên dưới assert là được. 

        except Exception as e:
            capture_screenshot(driver, "Lỗi khi login") 
            raise e
