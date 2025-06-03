from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MenuPage(BasePage):
    # Định danh các mục menu chính
    ADMIN_MENU = (By.XPATH, "//span[text()='Admin']")
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    LEAVE_MENU = (By.XPATH, "//span[text()='Leave']")

    # Gọi hàm click() kế thừa từ BasePage để click vào Admin
    # Dùng * để unpack tuple (By.XPATH, "xpath_here") khi truyền vào hàm click()
    def click_admin_menu(self):   
        self.click(*self.ADMIN_MENU)

    def click_pim_menu(self):
        self.click(*self.PIM_MENU)

    def click_leave_menu(self):
        self.click(*self.LEAVE_MENU)
