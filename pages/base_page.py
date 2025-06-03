# pages/base_page.py – các hàm dùng chung cho mọi trang web
# Mục tiêu: tái sử dụng các thao tác phổ biến như tìm phần tử, nhập liệu, click.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Đợi tối đa 10 giây khi tìm phần tử

    def find_element(self, by, value):
        # Tìm một phần tử duy nhất, đảm bảo nó xuất hiện trên trang
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def enter_text(self, by, value, text):
        # Nhập dữ liệu vào ô input
        element = self.find_element(by, value)
        element.clear()        # Xoá nội dung cũ
        element.send_keys(text)  # Gõ nội dung mới vào

    def click(self, by, value):
        # Tìm và click vào một phần tử
        self.find_element(by, value).click()

    def find_all_elements(self, by, value): 
        # Hỗ trợ find_all_elements():
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))