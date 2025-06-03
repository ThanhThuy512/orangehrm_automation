# utils/helpers.py : Thêm tính năng chụp ảnh màn hình khi test pass/fail và gắn ảnh vào báo cáo Allure
import allure
def capture_screenshot(driver, name="screenshot"):
    """
    Hàm chụp màn hình và đính kèm vào báo cáo Allure.
    Sử dụng khi test bị fail hoặc cần lưu lại bước quan trọng.
    """
    try:
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        print(f"Không thể chụp ảnh: {e}")
