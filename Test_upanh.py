from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

# Đường dẫn đến ảnh (nhớ đổi lại đường dẫn đúng với máy bạn)
file_path = r"C:\Users\Le Duy\Pictures\Screenshots\gggg.png"

# Cấu hình
options = Options()
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
time.sleep(2)

# Upload file
upload = driver.find_element(By.ID, "uploadPicture")
upload.send_keys(file_path)

# Kiểm tra upload thành công bằng cách kiểm tra value
uploaded_value = driver.execute_script("return arguments[0].value;", upload)
assert os.path.basename(file_path) in uploaded_value

print("✅ Upload file thành công:", uploaded_value)

driver.quit()
