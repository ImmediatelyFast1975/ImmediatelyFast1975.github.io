# -*- coding: utf-8 -*-
# Path: C:/Auto_Traffic_Empire/git_sync.py
import os
import time
import subprocess

PROJECT_DIR = r"C:\Auto_Traffic_Empire"

def thuc_thi_dong_bo_github():
    try:
        os.chdir(PROJECT_DIR)
        # Thực thi đẩy dữ liệu thông qua lệnh Shell của Windows
        subprocess.run("git add .", shell=True, check=True)
        
        commit_msg = f"Auto-Sync Money Infrastructure: {time.strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(f'git commit -m "{commit_msg}"', shell=True)
        
        subprocess.run("git push origin main", shell=True, check=True)
        print(f"🚀 [MODULE 2] Đã đẩy mẻ bài viết mới lên live GitHub Pages thành công!")
    except Exception as e:
        print(f"❌ [MODULE 2 LỖI KẾT NỐI GIT]: {str(e)} - Tự động thử lại ở chu kỳ sau...")

if __name__ == "__main__":
    print("[START] Module 2: Đường truyền GitHub Ready...")
    while True:
        thuc_thi_dong_bo_github()
        # Cứ 5 phút (300 giây) tự động đồng bộ đẩy toàn bộ bài viết lên mạng một lần
        time.sleep(300)