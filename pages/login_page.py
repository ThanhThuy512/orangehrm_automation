# pages/login_page.py – đại diện cho trang đăng nhập OrangeHRM
# Mục tiêu: cung cấp phương thức open() và login() để test file sử dụng.
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    # URL của trang đăng nhập
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    # Định nghĩa các locator cho phần tử (kiểu By, giá trị)
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self):
        # Mở trang web bằng driver
        self.driver.get(self.URL)

    def login(self, username, password):
        # Gọi các hàm dùng chung từ BasePage để thao tác login
        self.enter_text(*self.USERNAME_INPUT, username)   # Nhập username
        self.enter_text(*self.PASSWORD_INPUT, password)   # Nhập password
        self.click(*self.LOGIN_BUTTON)                    # Click nút đăng nhập
        # Chờ đến khi menu xuất hiện sau login
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.oxd-main-menu")))
