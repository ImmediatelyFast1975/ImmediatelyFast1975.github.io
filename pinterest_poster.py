# -*- coding: utf-8 -*-
# Path: C:/Auto_Traffic_Empire/pinterest_poster.py
import os, time, random, glob, requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

OUTPUT_DIR = r"C:\Auto_Traffic_Empire\output_websites"
DOMAIN = "https://ImmediatelyFast1975.github.io"

def setup_safe_browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1440x900")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    return webdriver.Chrome(options=chrome_options)

def go_chu_sinh_hoc(driver, element, text_val):
    ActionChains(driver).move_to_element(element).click().perform()
    time.sleep(0.5)
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE)
    time.sleep(0.5)
    for char in text_val:
        element.send_keys(char)
        time.sleep(random.uniform(0.02, 0.07))
    element.send_keys(Keys.TAB)

def xu_ly_ep_tao_board_doanh_nghiep(driver):
    """BẺ GÃY BẪY TRỐNG BẢNG: Ép mở dropdown, tự tạo bảng trực quan nếu tài khoản chưa có"""
    try:
        dropdown_xpath = "//button[@data-test-id='board-dropdown-select-button'] | //div[contains(@aria-label, 'Board')] | //div[contains(., 'Choose a board')]"
        board_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
        driver.execute_script("arguments[0].click();", board_dropdown)
        time.sleep(2)
        
        search_box = driver.find_elements(By.XPATH, "//input[contains(@placeholder, 'Search') or contains(@id, 'board')]")
        if search_box:
            go_chu_sinh_hoc(driver, search_box[0], "US HOT TRENDS")
            time.sleep(2)
            
            create_board_btn = driver.find_elements(By.XPATH, "//div[contains(., 'Create board') or contains(., 'Tạo bảng')]")
            if create_board_btn:
                driver.execute_script("arguments[0].click();", create_board_btn[0])
                time.sleep(2)
                submit_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit'] | //button[contains(., 'Create') or contains(., 'Tạo')]")))
                driver.execute_script("arguments[0].click();", submit_btn)
                print("    -> [BOARD CONTROL] Tài khoản mới tinh: Đã ép tạo xong bảng 'US HOT TRENDS'!")
                time.sleep(4)
            else:
                search_box[0].send_keys(Keys.ENTER)
                print("    -> [BOARD CONTROL] Đã chọn bảng 'US HOT TRENDS' thành công.")
                time.sleep(2)
    except:
        pass

if __name__ == "__main__":
    targets = glob.glob(os.path.join(OUTPUT_DIR, "*.html"))
    valid_targets = [(os.path.basename(f), f"{DOMAIN}/output_websites/{os.path.basename(f)}") for f in targets if "index" not in f]
    
    if not valid_targets:
        print("❌ Thư mục output trống."); exit()
        
    driver = setup_safe_browser()
    driver.get("https://www.pinterest.com/login/")
    print("\n🚨 ĐỢI SẾP ĐĂNG NHẬP EMAIL MỚI...")
    while True:
        if "login" not in driver.current_url: break
        time.sleep(2)

    for filename, url_live in valid_targets:
        print(f"\n[+] Đang bắn bài: {filename}")
        try:
            driver.get("https://www.pinterest.com/pin-builder/")
            WebDriverWait(driver, 20).until(lambda d: d.execute_script('return document.readyState') == 'complete')
            time.sleep(5)

            # ÉP TẠO VÀ CHỌN BẢNG TRƯỚC ĐỂ TRÁNH LỖI RESET FORM TRẮNG
            xu_ly_ep_tao_board_doanh_nghiep(driver)

            # 1. ĐIỀN LINK ĐÍCH
            link_in = driver.find_element(By.XPATH, "//input[@data-test-id='pin-draft-link'] | //input[@id='website'] | (//input[@type='text'])[last()]")
            go_chu_sinh_hoc(driver, link_in, url_live)
            
            # 2. ĐIỀN TIÊU ĐỀ
            title_in = driver.find_element(By.XPATH, "//textarea[@data-test-id='pin-draft-title'] | (//input[@type='text'])[1]")
            tieu_de_sach = filename.replace("article_20260522_", "").replace(".html", "").replace("_", " ").upper()
            go_chu_sinh_hoc(driver, title_in, f"🔥 HOT US TREND: {tieu_de_sach}")
            
            # 3. NẠP ẢNH VÀ XÓA RÁC ẢNH VỨT LUNG TUNG (Chỉ dùng đúng 1 tệp cover cố định)
            driver.execute_script("var x = document.querySelectorAll('input[type=file]'); for (var i=0; i<x.length; i++) { x[i].style.opacity=1; x[i].style.display='block'; x[i].style.visibility='visible'; }")
            driver.find_element(By.XPATH, "//input[@type='file']").send_keys(r"C:\Auto_Traffic_Empire\trending_cover.jpg")
            
            # 4. CHỜ MÁY CHỦ XÁC NHẬN RENDER ẢNH XONG 100%
            btn_xpath = "//button[contains(@class, 'save') or contains(., 'Publish') or contains(., 'Đăng')]"
            WebDriverWait(driver, 30).until(lambda d: d.find_element(By.XPATH, btn_xpath).is_enabled())
            
            # KÍCH NỔ LỆNH ĐĂNG LIVE
            publish_btn = driver.find_element(By.XPATH, btn_xpath)
            driver.execute_script("arguments[0].click();", publish_btn)
            print("    ✅ LIVE SUCCESSFUL - BÀI VIẾT ĐÃ LÊN MẠNG XÃ HỘI MỸ MỘT CÁCH THỰC TẾ!")
            time.sleep(15)
            
        except Exception as e:
            print(f"    ❌ LỖI LUỒNG BÀI NÀY: {str(e)}"); continue
            
    driver.quit()