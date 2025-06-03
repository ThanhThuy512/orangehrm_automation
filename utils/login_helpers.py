# utils/login_helpers.py

import allure
from pages.login_page import LoginPage

@allure.step("Đăng nhập vào hệ thống thành công")
def login_success(driver, username="Admin", password="admin123"):
    """
    Đăng nhập vào OrangeHRM với tài khoản mặc định.
    Hàm này dùng chung trong nhiều test để tránh lặp code login.
    """
    login = LoginPage(driver)
    login.open()
    login.login(username, password)
