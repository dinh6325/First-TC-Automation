from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Cấu hình trình duyệt
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/checkbox")
driver.maximize_window()

time.sleep(2)

# Mở rộng tất cả cây thư mục
toggle_btn = driver.find_element(By.CSS_SELECTOR, ".rct-collapse > svg")
toggle_btn.click()
time.sleep(1)

# Chọn checkbox 'Documents'
documents_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-documents']")
documents_checkbox.click()
time.sleep(1)

# Chọn checkbox 'Downloads'
downloads_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-downloads']")
downloads_checkbox.click()
time.sleep(1)

# Kiểm tra phần kết quả hiển thị phía dưới
result = driver.find_element(By.ID, "result").text
print(" Kết quả hiển thị sau khi chọn checkbox:")
print(result)

assert "documents" in result.lower()
assert "downloads" in result.lower()

print(" Đã chọn checkbox thành công và kết quả đúng!")

driver.quit()
