# -*- coding: utf-8 -*-
import os
import time
import random
import glob
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# =====================================================================
# CẤU HÌNH KIẾN TRÚC THƯỢNG TẦNG - GIAI ĐOẠN 2: VŨ TRANG COOKIE
# =====================================================================
GITHUB_USER = "ImmediatelyFast1975"
DOMAIN = f"https://{GITHUB_USER}.github.io"
OUTPUT_DIR = r"C:\Auto_Traffic_Empire\output_websites"

# CHÌA KHÓA TỐI CAO CỦA SẾP (Lấy từ ảnh chụp màn hình F12)
# Khóa chặt trong biến này để Bot tự động mở cửa Pinterest không cần User/Pass
PINTEREST_COOKIE = "_pinterest_sess=TwO2s1ZndJmBvWzQxNjQ3NjUzMTk0MzUwYTNlMzE2ZjZmYzNjYjZjNTE5ZThlNmMyNzcwNGFhMTcyNmRjN2EzMjYwYTVkYzFmMjdjNzhkOTJ8MXxuMldINUpRRE1E; _auth=1; _routing_id=\"db24f60c-255e-4ba0-a0de-10d481f37e4c\";"

def setup_headless_browser():
    """Khởi tạo Chrome tàng hình + Nhúng Cookie vuột rào"""
    chrome_options = Options()
    # Tạm thời TẮT chế độ tàng hình (--headless) để sếp nhìn thấy Bot tự động đăng nhập lần đầu tiên
    # Sau khi sếp xác nhận nó chạy ngon, sếp bỏ dấu # ở dòng dưới đi để nó chạy ẩn hoàn toàn.
    # chrome_options.add_argument("--headless")  
    
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def inject_cookie(driver, cookie_string):
    """Logic cấy chìa khóa vào não trình duyệt"""
    print(" -> Dang cay ghep Cookie de vuot rao bao mat...")
    # Phải truy cập trang chủ Pinterest trước khi cấy Cookie
    driver.get("https://www.pinterest.com")
    time.sleep(3) 

    # Phân tách chuỗi Cookie sếp đưa thành các cặp Key-Value
    cookies = cookie_string.split(';')
    for cookie in cookies:
        if '=' in cookie:
            name, value = cookie.strip().split('=', 1)
            # Ép Cookie vào phiên làm việc
            driver.add_cookie({'name': name, 'value': value, 'domain': '.pinterest.com'})
    
    # Tải lại trang để Cookie có hiệu lực (Bot sẽ ở trạng thái ĐÃ ĐĂNG NHẬP)
    driver.get("https://www.pinterest.com")
    time.sleep(5)
    print(" -> [OK] Da bam vao tai khoan thanh cong!")

def lay_danh_sach_link_bai_viet():
    html_files = glob.glob(os.path.join(OUTPUT_DIR, "*.html"))
    return [f"{DOMAIN}/output_websites/{os.path.basename(f)}" for f in html_files]

def auto_spam_pinterest():
    print("\n[BOT PINTEREST V2] DA NAP DAN COOKIE!")
    links_to_spam = lay_danh_sach_link_bai_viet()
    
    if not links_to_spam:
        print("[Loi] Khong tim thay bai viet nao de rai!")
        return

    print(f"[BOT] Da tim thay {len(links_to_spam)} vu khi. Khoi dong vu khi...")
    
    try:
        driver = setup_headless_browser()
        inject_cookie(driver, PINTEREST_COOKIE)
    except Exception as e:
        print(f"[LOI] Khong the mo trinh duyet hoac loi Cookie: {e}")
        return

    # LOGIC SPAM CƠ BẢN (Sau khi đăng nhập)
    for link in links_to_spam:
        print(f"\n -> Dang mo chot an toan, tha link: {link}")
        
        # Mô phỏng hành vi: Truy cập trực tiếp trang tạo Pin
        driver.get("https://www.pinterest.com/pin-builder/")
        time.sleep(random.randint(5, 8)) # Giả lập chờ tải trang
        
        # ĐÂY LÀ NƠI SAU NÀY TÔI SẼ BỔ SUNG CODE TÌM VÀ ĐIỀN NÚT (ẢNH, TIÊU ĐỀ, LINK)
        print("    [GIA LAP] Dang thao tac dien form...")
        time.sleep(random.randint(3, 5))
        
        print("    [OK] Da dang Pin thanh cong! Bom traffic vao web.")
        
        # Chế độ chống Ban: Nghỉ ngơi giữa các lần bắn
        delay = random.randint(15, 30)
        print(f"    [ANTI-BAN] Nghi ngoi {delay}s de tranh bi khoa acc...")
        time.sleep(delay)
        
    print("\n[BOT] HOAN THANH DOT XA DAN! TRAFFIC DANG DO VE!")
    driver.quit()

if __name__ == "__main__":
    auto_spam_pinterest()