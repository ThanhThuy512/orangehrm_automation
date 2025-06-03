# Kiểm tra tìm nhân viên thực cho hệ thống
import allure
#from pages.login_page import LoginPage
from utils.login_helpers import login_success
from pages.menu_page import MenuPage
from pages.employee_page import EmployeePage
from utils.helpers import capture_screenshot
@allure.title("Tìm kiếm nhân viên với từ khóa hợp lệ")
@allure.description("Vào menu PIM, nhập tên nhân viên và xác minh có kết quả trả về")
def test_search_employee(driver):
    #login = LoginPage(driver)
    login_success(driver)  # 👈 Chỉ 1 dòng gọi login
    menu = MenuPage(driver)
    employee = EmployeePage(driver)

#    with allure.step("Đăng nhập"):
#       login.open()
#       login.login("Admin", "admin123")

    with allure.step("Đi đến menu PIM"):
        menu.click_pim_menu()

    with allure.step("Tìm kiếm nhân viên có tên 'Joy'"):
        employee.search_employee("Joy")

    with allure.step("Chụp ảnh kết quả và kiểm tra số kết quả"):
        try:
            capture_screenshot(driver, "Kết quả tìm kiếm nhân viên")
            
            # => Đếm số dòng kết quả hiện ra
            assert employee.get_search_results_count() > 0              # => Kiểm tra có ít nhất 1 kết quả tìm thấy
        except Exception as e:
            capture_screenshot(driver, "Không tìm thấy nhân viên")
            raise e
