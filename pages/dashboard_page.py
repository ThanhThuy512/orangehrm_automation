# pages/dashboard_page.py – thao tác với trang Dashboard

from selenium.webdriver.common.by import By # => Import công cụ định vị phần tử (By.ID, By.CSS_SELECTOR, ...)
from pages.base_page import BasePage # => Kế thừa class BasePage để dùng lại hàm find_element, enter_text
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage(BasePage):
    # Định danh thanh menu chính sau khi đăng nhập
    MAIN_MENU_ITEMS = (By.CSS_SELECTOR, "ul.oxd-main-menu li")  # => Định vị tất cả mục menu (bên trái) trên dashboard

    # Thanh tìm kiếm nhanh ở góc trên trái (nếu có)
    QUICK_SEARCH_INPUT = (By.CSS_SELECTOR, "input.oxd-input") # => Định vị ô input để tìm chức năng hoặc nhân viên (nếu có)

    SUGGESTION_ITEM = (By.XPATH, "//span[text()='Leave']")  # 👈 Gợi ý trong kết quả
    
    def get_menu_items_text(self):   # => Trả về danh sách tên của các mục trong menu
        """
        Lấy danh sách các nhãn menu hiển thị bên trái dashboard
        Trả về: list chứa text của từng mục
        """
        elements = self.find_all_elements(*self.MAIN_MENU_ITEMS)  # Tìm tất cả các item menu
        return [el.text for el in elements if el.text.strip()]    # Trích text và lọc phần tử rỗng

    def search_in_dashboard(self, keyword):  # => Tự động nhập từ khóa vào ô tìm kiếm
        """
         Gõ từ khóa vào ô tìm kiếm trên Dashboard (xử lý stale element)
        """
        #self.enter_text(*self.QUICK_SEARCH_INPUT, keyword)
        # Chờ ô tìm kiếm sẵn sàng và nhập từ khóa
        input_box = self.wait.until(EC.element_to_be_clickable(self.QUICK_SEARCH_INPUT))
        input_box.clear()
        input_box.send_keys(keyword)

        # Chờ gợi ý xuất hiện và click vào
        suggestion = self.wait.until(EC.element_to_be_clickable(self.SUGGESTION_ITEM))
        suggestion.click()
