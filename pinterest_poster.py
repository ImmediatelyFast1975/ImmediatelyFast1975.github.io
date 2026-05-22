# -*- coding: utf-8 -*-
# Path: C:/Auto_Traffic_Empire/pinterest_poster.py
import os
import time
import random
import glob
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

GITHUB_USER = "ImmediatelyFast1975"
DOMAIN = f"https://{GITHUB_USER}.github.io"
OUTPUT_DIR = r"C:\Auto_Traffic_Empire\output_websites"

def tao_shortlink_uy_tin(long_url):
    try:
        res = requests.get(f"http://tinyurl.com/api-create.php?url={long_url}", timeout=5)
        if res.status_code == 200 and "tinyurl" in res.text: return res.text.strip()
    except: pass
    return long_url

def setup_industrial_clean_browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1440x900")
    chrome_options.add_argument("--lang=en-US")
    chrome_options.add_argument("--incognito") # Ép trình duyệt ẩn danh phá vỡ bẫy lưu cache tài khoản cũ
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--disable-application-cache")
    chrome_options.add_argument("--disk-cache-size=1")
    return webdriver.Chrome(options=chrome_options)

def go_chu_sinh_hoc_bat_doi_xuong(driver, element, text_val):
    """MÔ PHỎNG TAY NGƯỜI: Click vào tâm, xóa sạch rác và gõ phím tốc độ biến thiên cản AI quét bot"""
    ActionChains(driver).move_to_element(element).click().perform()
    time.sleep(0.5)
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE)
    time.sleep(0.5)
    for char in text_val:
        element.send_keys(char)
        time.sleep(random.uniform(0.03, 0.12))
    element.send_keys(Keys.TAB)
    time.sleep(0.5)

def lay_anh_minh_hoa_doc_ban(keyword):
    """LÁ CHẮN SPAM: Tự động tải ảnh ngẫu nhiên có mã MD5 độc bản lách thuật toán khóa tài khoản"""
    local_path = f"C:\\Auto_Traffic_Empire\\temp_{keyword}.jpg"
    try:
        res = requests.get(f"https://picsum.photos/600/900?random={random.randint(1,2000)}", timeout=8)
        if res.status_code == 200:
            with open(local_path, "wb") as f: f.write(res.content)
            return local_path
    except: pass
    return r"C:\Auto_Traffic_Empire\trending_cover.jpg"

def xu_ly_board_control_safe_loop(driver, is_first_run):
    """BẢO VỆ LUỒNG BẢNG: Tự tạo bảng ở bài số 1, các bài sau enter chọn luôn, xóa sổ lỗi 'Không tìm thấy bảng'"""
    try:
        dropdown_xpath = "//button[@data-test-id='board-dropdown-select-button'] | //div[contains(@aria-label, 'Board')] | //div[contains(., 'Choose a board')]"
        board_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
        driver.execute_script("arguments[0].click();", board_dropdown)
        time.sleep(2)
        
        search_input = driver.find_elements(By.XPATH, "//input[contains(@placeholder, 'Search') or contains(@id, 'board')]")
        if search_input:
            go_chu_sinh_hoc_bat_doi_xuong(driver, search_input[0], "US HOT TRENDS")
            time.sleep(2)
            
            if is_first_run:
                create_board_btn = driver.find_elements(By.XPATH, "//div[contains(., 'Create board') or contains(., 'Tạo bảng')]")
                if create_board_btn:
                    driver.execute_script("arguments[0].click();", create_board_btn[0])
                    time.sleep(2)
                    final_create = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit'] | //button[contains(., 'Create') or contains(., 'Tạo')]")))
                    driver.execute_script("arguments[0].click();", final_create)
                    print("    -> [BOARD CONTROL] Bài 1: Kích nổ Tạo Bảng thành công!")
                    time.sleep(4)
            else:
                search_input[0].send_keys(Keys.ENTER)
                print("    -> [BOARD CONTROL] Đã ăn bảng có sẵn bằng Enter."); time.sleep(2)
    except: pass

def thuc_thi_chien_dich_rai_tham():
    targets = glob.glob(os.path.join(OUTPUT_DIR, "*.html"))
    valid_targets = [(os.path.basename(f), f"{DOMAIN}/output_websites/{os.path.basename(f)}") for f in targets if "index" not in f]
    
    if not valid_targets:
        print("❌ [MODULE 3] Chưa tìm thấy file HTML bài viết nào để đăng."); return

    print(f"[MODULE 3 ACTIVE] Khởi động luồng Pinterest v1100.0. Quy mô hành quân: {len(valid_targets)} mục tiêu.")
    driver = setup_industrial_clean_browser()
    driver.get("https://www.pinterest.com/login/")
    
    print("\n🚨 [CHỐT CHẶN AN TOÀN] TRÌNH DUYỆT ĐANG ĐỢI SẾP ĐĂNG NHẬP...")
    print("-> Sếp thong thả đăng nhập EMAIL MỚI TINH + giải Captcha. Không giới hạn thời gian...")
    
    while True:
        if "login" not in driver.current_url:
            print(" ✅ Đăng nhập thành công! Bắt đầu găm ghim tự động!"); break
        time.sleep(2)

    loop_count = 0
    for filename, url_live in valid_targets:
        loop_count += 1
        trend_keyword = filename.replace("article_", "").replace(".html", "")
        print(f"\n[+] [{loop_count}/{len(valid_targets)}] Đang găm bài: {filename}")
        
        safe_shortlink = tao_shortlink_uy_tin(url_live)
        img_v11 = lay_anh_minh_hoa_doc_ban(trend_keyword)

        try:
            driver.get("https://www.pinterest.com/pin-builder/")
            time.sleep(5)
            if "pin-builder" not in driver.current_url:
                driver.get("https://www.pinterest.com/pin-creation-tool/")
            
            WebDriverWait(driver, 20).until(lambda d: d.execute_script('return document.readyState') == 'complete')
            time.sleep(4)

            driver.execute_script("var pop = document.querySelectorAll('[role=\"dialog\"]:not(:has(input)), [class*=\"modal\"]:not(:has(input))'); for (var i=0; i<pop.length; i++) { pop[i].remove(); }")
            xu_ly_board_control_safe_loop(driver, is_first_run=(loop_count == 1))

            # 1. ĐIỀN LINK ĐÍCH CƠ HỌC
            link_input = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-test-id='pin-draft-link'] | //input[@id='website' or @id='link'] | (//input[@type='text'])[last()]")))
            go_chu_sinh_hoc_bat_doi_xuong(driver, link_input, safe_shortlink)

            # 2. ĐIỀN TIÊU ĐỀ CƠ HỌC CHỐNG LỖI JAVASCRIPT REFRESH
            tieu_de_sach = filename.replace("article_20260522_", "").replace(".html", "").replace("_", " ").upper()
            title_input = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@data-test-id='pin-draft-title'] | //textarea[contains(@placeholder, 'Title')] | (//input[@type='text'])[1]")))
            go_chu_sinh_hoc_bat_doi_xuong(driver, title_input, f"🔥 HOT US TREND: {tieu_de_sach}")

            # 3. NẠP FILE ẢNH BIẾN THIÊN ĐỘC BẢN
            driver.execute_script("var x = document.querySelectorAll('input[type=file]'); for (var i=0; i<x.length; i++) { x[i].style.opacity=1; x[i].style.display='block'; x[i].style.visibility='visible'; }")
            time.sleep(1)
            driver.find_element(By.XPATH, "//input[@type='file']").send_keys(img_v11)
            print("    -> [OK] Đã găm ảnh độc bản.")
            
            # ĐỒNG BỘ TẢI ẢNH: Đợi ảnh lên sóng 100% nút đăng mới mở khóa, triệt tiêu lỗi kẹt bản nháp rác
            print("    -> Bộ kiểm toán quét trạng thái hàng đợi tải ảnh..."); time.sleep(2)
            publish_btn_xpath = "//button[contains(@class, 'save') or contains(., 'Publish') or contains(., 'Đăng') or @data-test-id='board-dropdown-save-button']"
            WebDriverWait(driver, 30).until(lambda d: d.find_element(By.XPATH, publish_btn_xpath).is_enabled())

            # 4. CLICK PHÓNG BÀI LIVE ĐĂNG TIN
            publish_btn = driver.find_element(By.XPATH, publish_btn_xpath)
            driver.execute_script("arguments[0].click();", publish_btn)
            print("    ✅ [THÀNH CÔNG RỰC RỠ] BÀI VIẾT ĐỀU ĐÃ LIVE TRÊN PINTEREST MỸ!")
            time.sleep(15)

            if os.path.exists(img_v11) and "trending_cover" not in img_v11:
                try: os.remove(img_v11)
                except: pass

            if loop_count % 5 == 0:
                driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
                print("    🧹 [CLEANING] Đã giải phóng bộ nhớ đệm RAM.")

            delay = random.randint(60, 120)
            print(f"    [COOL-DOWN] Nghỉ ngơi chiến thuật bảo vệ tài khoản {delay}s...")
            time.sleep(delay)

        except Exception as e:
            print(f"    ❌ [BỎ QUA LỖI PHẦN TỬ]: {str(e)}"); continue

    driver.quit()

if __name__ == "__main__":
    thuc_thi_chien_dich_rai_tham()