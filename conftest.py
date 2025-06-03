# conftest.py – cấu hình trình duyệt cho toàn bộ test
# Mục tiêu: cung cấp driver cho tất cả test thông qua @pytest.fixture.

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Cài đặt service để khởi tạo ChromeDriver tự động
    service = Service(ChromeDriverManager().install())

    # cấu hình các tùy chọn cho trình duyệt Chrome, ví dụ:Mở ở chế độ full screen, Tắt thông báo,Chạy ở chế độ headless (không giao diện)...Tuỳ chọn trình duyệt (ở đây dùng Chrome)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Mở trình duyệt ở chế độ full màn hình

    # Khởi tạo trình điều khiển (WebDriver)
    driver = webdriver.Chrome(service=service, options=options)

    # Trả về đối tượng driver cho mỗi test sử dụng và Cho phép xử lý cleanup sau test
    yield driver

    # Sau khi test kết thúc, đóng trình duyệt
    driver.quit()
