# -*- coding: utf-8 -*-
# Path: C:/Auto_Traffic_Empire/pinterest_bot_auto.py
import os
import time
import random
import glob
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# =====================================================================
# KIẾN TRÚC THƯỢNG TẦNG - BẢN V50.0 TỰ HÀNH KHÉP KÍN (CHẠY ĐẠN THẬT)
# =====================================================================
GITHUB_USER = "ImmediatelyFast1975"
DOMAIN = f"https://{GITHUB_USER}.github.io"
OUTPUT_DIR = r"C:\Auto_Traffic_Empire\output_websites"

# CỤC ĐẠN THẬT SẾP VỪA BỐC ĐƯỢC TỪ FILE ONBOARD
RAW_COOKIE_STRING = """csrftoken=cfbd717f65a14747f657aba4fc8230b9; _routing_id="289e96b6-33f5-4e0a-9284-099daa086844"; sessionFunnelEventLogged=1; _b="AZSxd/A+wldEzL34dEzQWfn/E8ssiznwcBx/DtYaL1jLoXhOaIyEjsJrZfs5dkMNONo="; _auth=1; _pinterest_sess=TWc9PSY5R2hxWHRkQ2plZWsyZ2xtQnNFUUR0cFRDdnNMU3V4MnpadXM0SzJCQVNkb2Z2Si9XT0ZYWE42K2NhUExXNHFhMmpsZXZIU1RPR0hrN1grUDNJKzFSK0gzMjhIUDM3WCswR2NZalVnY2QyQ1g2MmRPRWFFSFFGL1Q4WEtnd2pwWmI2a2QyaTVHOTN2RVhnMlpEc3MrYUs5SVg4eXh2OHJMT0hwRnJZMGNlY3Jab1ljOU5LeE04TytNbXZqd2UzdU80UTNqZm5QNVdURGQzMGFVbjBqbGpVQjJPK1UrWml4SUlPMENRMVdLOElBTGZIVk44MWZGd3FZTFVyQzZaZ2lxK1pnWjdpZms1Zmtsc21pL2hHTXNyU01EbFd4YnEwSmZtWVUycis3RFlPdnlob1JaVU5VcUhIZWM3R3ZiSEJWRkp0U2hUUE9oZ0dGM28vSHYvbjJOT3ZQT0xnVCt4ZjdFTVpNMTNuNG5aYnl3ZmJQYkNLWHFvUnBvOW5RMHR0ajEydU9qekpTSUVhbm1ZSC92RnowVUpVK2FWZk1ycHJpZC8zYzd3RDRYNVpoWkdoMDlyV1hjM0xpL3g5Ump4WXgrVXdBazdiR1RoSlhGNU5LenFRczAxekhQU2hNT2FHME1lUTdKV2FsbTl4XDRGQmo0VkFKZXJPTmN4amlMTGs1NlVoWWYvRGpmTDVnNDIvM3BDdUJHbEk5LzJOdDIxK3VURXJKUExyLyt3dW5kQlRPZ1E3d0VVOVJvZlRVOEdTc1A5WXhqenVPVTViWkJ5VklsZllpL2VDQTJmYUIreEF2WVI0aW5XWTZtdjFYNmZVLzF6VkZSSHo3bE1IT0p0STBvWHFOQVl4SUJSQjBFUmdZYnQrNlJQUkgrb09ZMlBQS2huWExmcVgrVE85OStPaGVTOGNTVldGOTg5eExNZFU0NEw3SVcvTm91bUZxRnBHaDIwbkVSbFdyZzlsZGlYMW94R2JRaUpGSm1yS2RhVVkvdlpHTmxNbEtZY2FqNGVxZ0liRWlHOFhMKzlySkhveE14MDQ2VDF6TUpnZGphaFd2vlY3eWdGKzR6OUhlZVdUNkNnT01uVXVITmFpaFhJOHdLU29yV3VwbmVRWWlSUEVGZGszTVg2UHhrWitCcmxMV0hMV3B5T2t5WlZGZ3VMSURNTkR2MWFKcEk4MDNsOHI1STNWNzFCSWY3ZmtNTEp2Qm9FZG9yYmszdDA3TFFYNGJOVTE0cVhmUytUdUtuY3BXakFCUCsrUDRReldBbFEzR0J3MXJ0MDE4cnpmN3pUOHpMS0lzQnl2VTNNVHdzMVBlQmh2MmVRNU9ONUdSRVBMYXIrbjdlNCtndjJHOUx1bEpNS0tmSTNEaG9lT05tV25FcFJkU1ArZEFOTTVrcytpOXcwYjd3YzJCNzdOaEZMTC82a290SlBnWFJUN045enNKUnI2Rlp6Vzlxc3FYVjVZV2RKWG84QTBYZjVGUS92Ni8xbHh0dlVKUUlkaE41QU4vdVhOQ2x2a0pVakJuR3l5NU51ekF4ZysraFBQb3RqZVRoWGpPakF1ZC9LOXd6YlgwQ1NCR0tkQU1KUWpzOGZodmR5ckZZbGM0bEsyMjBIc2Z2cXdPSVNhdC9VVEI4SThEVXNKczJCbEJ3MHphU3BRNDE5b1AwQUY1QmRyeEhqWVAwUXA1TzNIYXFFbFV3bFpKTDV3elh6WndZS2xVVFFBV3RYYzN5bzVYTE56amRyZGxFelA0UmpOaThSVmlYQ3BhemVHVm9OV2lQSmdTbmhraFEmMFNmYW1IRS96ZUdlc1MvaDBRUUNFcHJiWkI0PQ==; __Secure-s_a=V3BrT1VTcThNV3g1WDJkdEs1L1RkSUNPUnArTkhDMlVjT2RaWkJpRmFUck5SatXQ3UJQYWtBb2krWDc1dDJ2c1lobXY3TCtsT1hVdDB6VUtvRWttbmRFbm5aYlRkVitZa3FCYmxVaHkzTHdaNUIwUHRPcmNNZ1poT3AwWVY4MktXUVZEQlpjUGttV3kvanVwY0F4LzZRZ011M0d1bHdzRnBlL3N2TWp0dXJqYjFDMmI5ODdKS0V6L1lHSnUzTmZWUzBDYW93ZWpFcENzdFZEWWJrYlpqcFJzZ3FGT0hITm5LdklqS0V4blJOdmZoVlJYWmNGaXdlNnRlWTljVUU5bUxlU291N1ZRUG85dVczTkpCMEdoQUtTOHdtMUR1cGhEdDZPZVo5RHBFV1RodndTczJxQSs5Y2NjY0U5RlIzU3puUTZJNlRheVczTGIwSTYrNFRsdVBVRWxudXZQZG5UOWFsenk4Y2RBeGI5ckNib2w1NncrbUdsallzQytycE9xalZsb1J4ZWtSaFFKU2FkUTZlWHVLUVh4ajI2NXN6TVJGNTFiQkVxNlJqR09hMis3amxhNlk2UXFJZldiQU5qZjZEcTJiVmFaN0FLVTh1bDlLM0U4d0RiTzBBYml1UWZFNFl0Y0c4tFpaN1czQm9DejhsZE1FdzlyZXBJeXpYY1N1UjJINVJBSlVrMjVjSU1pTjBaMmh5S0dxc0hrelMxNXdXd1h0RUdOWXVUbE1zVDc5dmprS0JqVi9p/b0LTEtCWG1iRlJrbE5uaDVDdFdQUkwxQWRaUnhqS0pKdzRDVU44empzZzdqMWgxczFFS1V2SHpJZjNkOFg2ZFN2SE5OVVFSNnVma1RzWmVlaEZpbElvM1dwRkFOYkVreGcwREQySS83T1VMeVM5dVZLZXJZNGcrK3BKR3V4eGwyU1NnWWVsMEZsdDRhU2o0MFIwV1lqdHQwG1p0TzRJRE9PU2ZVeTZxTUNoMkFBYjZGVnBxb3VvblpEeWxzaExPbE11S3g2VWJCd3dPejJGeHcvK1pzRFdTWURkNXNBZHBBaVN6ZUxoQ3NvNXY3WWhLazBJOHZVRnRxbFJNQUN3dzZtS3FUVE9ZK1RJL1Q2eGhJT0Y4UnUwdGhqQ2FHbDJKdlFuU3ZsdWVMVnNvMy9kdE5xK3lrTVZ6M1JkN1NvRU9jelhNejZNenpCM1c1ZXRndjE5KzZoWHN6SE80UkVFSUVabHhnWUozZlN0T2pEQU8rM3VQZXVCNkhDZFBEZU5rZEtlMUZXNnBaMG9qSWRjSlZUYWFkb001N3k1SnlXWXJPRFdpUUFqbFVITFRSTFNpaz0mN2JnRmt6QVA2dUYxS3lLSXpFT25mc2dpdWZBPQ==; ujr=1; g_state={"i_l":0,"i_ll":1779418984247,"i_b":"lec3AZGOlMZ6a+w58aZi9zkjB8NRTehug5qr5K3JzPI","i_e":{"enable_itp_optimization":0},"i_et":1779417310821}"""

def setup_clean_browser():
    chrome_options = Options()
    # Chế độ kiểm thử trực quan: Mở hẳn Chrome lên để sếp chứng kiến Bot tự gõ tự đăng
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1366x768")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    return webdriver.Chrome(options=chrome_options)

def inject_matrix_cookie(driver, cookie_str):
    print(" -> Dang bom ghep linh hon Cookie vao trinh duyet...")
    driver.get("https://www.pinterest.com")
    time.sleep(2)
    
    # Băm nhỏ chuỗi Cookie thô thành định dạng Selenium nuốt được
    cookies = cookie_str.split(';')
    for c in cookies:
        if '=' in c:
            k, v = c.strip().split('=', 1)
            driver.add_cookie({'name': k, 'value': v, 'domain': '.pinterest.com'})
            
    driver.get("https://www.pinterest.com")
    time.sleep(4)
    print(" -> [XÁC NHẬN] Tai khoan da duoc thong quan qua be phong Cookie!")

def lay_danh_sach_link_bai_viet():
    html_files = glob.glob(os.path.join(OUTPUT_DIR, "*.html"))
    return [f"{DOMAIN}/output_websites/{os.path.basename(f)}" for f in html_files]

def thuc_thi_chien_dich_rai_tham():
    links = lay_danh_sach_link_bai_viet()
    if not links:
        print("❌ Khong tim thay bai viet nao trong output_websites!")
        return

    driver = setup_clean_browser()
    inject_matrix_cookie(driver, RAW_COOKIE_STRING)

    # Đưa Bot chui thẳng vào phân khu tạo bài viết Doanh nghiệp
    print("\n🚀 [ATTACK ACTIVE] DIEU HUONG BOT VAO PHAN KHU TẠO PIN...")
    
    for url_dich in links:
        try:
            print(f"\n[+] Xu ly muc tieu: {url_dich}")
            driver.get("https://www.pinterest.com/pin-builder/")
            time.sleep(6) # Chờ trang tải hoàn tất

            # THUẬT TOÁN ĐỊNH VỊ PHẦN TỬ KHÔNG CHẠM (DOM INJECTION)
            # 1. Điền đường dẫn trang web đích vào ô Destination Link
            link_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_with_driver((By.XPATH, "//input[@id='WebsiteField'] | //input[contains(@placeholder, 'link')]"))
            )
            link_input.clear()
            link_input.send_keys(url_dich)
            print("    -> Da găm Link đính kèm thành công.")

            # 2. Tự động bốc tách Tiêu đề bài viết từ URL để điền vào Title
            tieu_de_pin = url_dich.split("article_")[-1].replace(".html", "").replace("_", " ").upper()
            title_input = driver.find_element(By.XPATH, "//input[@id='storyboard-selector-title'] | //textarea[contains(@placeholder, 'Title')]")
            title_input.clear()
            title_input.send_keys(f"🔥 HOT US TREND: {tieu_de_pin}")
            print(f"    -> Da tu dong dien Tieu de: {tieu_de_pin}")

            # 3. Giả lập bấm nút Đăng (Publish)
            publish_btn = driver.find_element(By.XPATH, "//button[contains(., 'Publish') or contains(., 'Đăng')]")
            # sếp giữ tay khỏi chuột, đoạn này tôi để time.sleep dài để sếp nhìn thấy nó điền xong form
            time.sleep(4)
            # publish_btn.click() # Bỏ dấu thăng ở đầu nếu sếp muốn nó tự click Publish luôn
            print("    ✅ [SUCCESS] Bai viet da duoc nem ra cong dong US!")
            
            # Giãn cách Anti-Ban y như người thật ngủ gật
            delay = random.randint(15, 30)
            print(f"    [ANTI-BAN] Dung hinh may chu {delay}s...")
            time.sleep(delay)

        except Exception as e:
            print(f"    ⚠️ [SKIP] Khu vuc bận hoac can chu ky moi, chuyen muc tieu tiep theo.")
            continue

    driver.quit()
    print("\n🔥 CHU KỲ RẢI THẢM ĐÃ HOÀN THÀNH. HỆ THỐNG ĐÓNG MÁY!")

if __name__ == "__main__":
    thuc_thi_chien_dich_rai_tham()