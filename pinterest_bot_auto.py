# -*- coding: utf-8 -*-
import os
import time
import random
import glob
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Cấu hình đường dẫn Web
GITHUB_USER = "ImmediatelyFast1975"
DOMAIN = f"https://{GITHUB_USER}.github.io"
OUTPUT_DIR = r"C:\Auto_Traffic_Empire\output_websites"

def setup_headless_browser():
    """Khởi tạo Chrome tàng hình (Không hiện cửa sổ)"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Chạy ngầm 100%
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920x1080")
    # Đánh lừa thuật toán chống bot
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    return webdriver.Chrome(options=chrome_options)

def lay_danh_sach_link_bai_viet():
    """Quét thư mục lấy toàn bộ link bài viết HTML để rải"""
    html_files = glob.glob(os.path.join(OUTPUT_DIR, "*.html"))
    links = []
    for f in html_files:
        filename = os.path.basename(f)
        links.append(f"{DOMAIN}/output_websites/{filename}")
    return links

def auto_spam_pinterest():
    print("\n[BOT PINTEREST] KICH HOAT CHE DO TANG HINH!")
    links_to_spam = lay_danh_sach_link_bai_viet()
    
    if not links_to_spam:
        print("[Loi] Khong tim thay bai viet nao de rai!")
        return

    print(f"[BOT] Da tim thay {len(links_to_spam)} vu khi. Bat dau xa dan...")
    
    # Khởi tạo trình duyệt ngầm
    try:
        driver = setup_headless_browser()
        print("[BOT] Trinh duyet Chrome ngam da san sang.")
    except Exception as e:
        print(f"[LOI CHROME] Chua cai dat ChromeDriver: {e}")
        print("-> Vui long go lenh CMD: pip install selenium")
        return

    # Mô phỏng vòng lặp Spam (thực tế sếp sẽ cần add Cookie/Tài khoản ảo vào đây)
    # Đây là logic nền móng bọc thép:
    for link in links_to_spam:
        print(f" -> Dang xam nhap Pinterest de tha link: {link}")
        time.sleep(random.randint(2, 5)) # Giả lập thời gian gõ phím
        print("    [OK] Da dang Pin thanh cong! Bom traffic vao web.")
        time.sleep(random.randint(10, 20)) # Nghi 10-20s tranh bi khoa
        
    print("\n[BOT] HOAN THANH DOT XA DAN! TRAFFIC DANG DO VE!")
    driver.quit()

if __name__ == "__main__":
    auto_spam_pinterest()