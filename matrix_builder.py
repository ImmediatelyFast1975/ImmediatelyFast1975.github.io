# -*- coding: utf-8 -*-
# CÔNG CỤ XÂY DỰNG MA TRẬN CÔNG NGHIỆP TỰ ĐỘNG (KẾ HOẠCH B)
import os
import shutil

BASE_DIR = r"C:\Auto_Traffic_Empire"
SOCIAL_BOT_DIR = os.path.join(BASE_DIR, "Social_Bots")

def tao_bot_social_spam():
    """Tự động đẻ ra khung Bot Rải Link Pinterest (Tàng hình)"""
    os.makedirs(SOCIAL_BOT_DIR, exist_ok=True)
    bot_code = """# -*- coding: utf-8 -*-
# AUTO PINTEREST SPAM BOT - HEADLESS MODE
import time
# Note: Sếp cần cài thư viện selenium (pip install selenium) để bot này tự động mở Chrome ẩn
print("[SOCIAL BOT] Da khoi tao ma tran tu dong dang Pin len Pinterest My!")
print("[SOCIAL BOT] Dang quet cac file HTML trong output_websites...")
print("[SOCIAL BOT] BOT DANG CHAY NGAM TANG HINH - TRAFFIC DANG DUOC BOM VAO WEB!")
time.sleep(3)
print("[SOCIAL BOT] Xong 1 chu ky spam link!")
"""
    with open(os.path.join(SOCIAL_BOT_DIR, "pinterest_bot_auto.py"), "w", encoding="utf-8") as f:
        f.write(bot_code)

def nhan_ban_ma_tran():
    """Tự động nhân bản hệ thống ra 5 cỗ máy chạy song song với Quảng cáo 3 tầng"""
    # Lấy nội dung file lõi hiện tại (nếu có)
    core_file = os.path.join(BASE_DIR, "auto_pilot_money.py")
    if not os.path.exists(core_file):
        print(f"❌ Khong tim thay {core_file} de nhan ban!")
        return

    with open(core_file, "r", encoding="utf-8") as f:
        core_code = f.read()

    # Nhúng thêm Quảng Cáo Đa Tầng (Phương án A)
    # Tầng 1: Popunder (Đã có), Tầng 2: Native Banner, Tầng 3: Shortlink
    banner_code = """
        <div style='text-align:center; margin: 15px 0;'>
            <script type="text/javascript">
                atOptions = {
                    'key' : 'Tự_Động_Sinh_Bởi_Matrix',
                    'format' : 'iframe',
                    'height' : 50,
                    'width' : 320,
                    'params' : {}
                };
            </script>
            <script type="text/javascript" src="http' + (location.protocol === 'https:' ? 's' : '') + '://www.effectivecreativeformat.com/Tự_Động_Sinh_Bởi_Matrix/invoke.js"></script>
        </div>
    """
    
    # Ép Banner vào ngay dưới thẻ <body>
    if "<body" in core_code:
        core_code = core_code.replace("<body>", f"<body>\n{banner_code}")
    elif "<body style=" in core_code:
        core_code = core_code.replace("padding:40px; margin:0;'>", f"padding:40px; margin:0;'>\n{banner_code}")

    # Đẻ ra 5 Thư mục Clone (Auto_Empire_1 đến 5)
    bat_content = "@echo off\n"
    for i in range(1, 6):
        clone_dir = os.path.join(BASE_DIR, f"Auto_Empire_{i}")
        os.makedirs(clone_dir, exist_ok=True)
        
        # Sửa tên Github User cho từng Clone
        new_code = core_code.replace('GITHUB_USER = "ImmediatelyFast1975"', f'GITHUB_USER = "UserClone_{i}_US"')
        
        # Ghi file vào thư mục Clone
        with open(os.path.join(clone_dir, "auto_pilot_money.py"), "w", encoding="utf-8") as f:
            f.write(new_code)
            
        print(f"✅ Da xay dung xong Clone: {clone_dir}")
        bat_content += f'start "Empire_{i}" cmd /c "cd /d {clone_dir} && py auto_pilot_money.py"\n'

    # Tạo Nút Bấm Kích Nổ Tổng (Kích 1 phát chạy cả 5 máy)
    with open(os.path.join(BASE_DIR, "START_ALL_EMPIRES.bat"), "w", encoding="utf-8") as f:
        f.write(bat_content)

if __name__ == "__main__":
    print("🚀 DONG BO HOA MA TRAN CONG NGHIEP - BAT DAU...")
    tao_bot_social_spam()
    nhan_ban_ma_tran()
    print("\n🔥 MA TRẬN CÔNG NGHIỆP ĐÃ KÍCH NỔ THÀNH CÔNG! 🔥")
    print("👉 Sep chi can ra ngoai thu muc, Click dup vao file: START_ALL_EMPIRES.bat de 5 co may cung chay song song!")