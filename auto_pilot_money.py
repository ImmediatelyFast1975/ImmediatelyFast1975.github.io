# -*- coding: utf-8 -*-
# Path: C:/Auto_Traffic_Empire/auto_pilot_money.py
import os
import time
import random
import datetime
import xml.etree.ElementTree as ET
import re
import requests
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor

# =====================================================================
# CẤU HÌNH KIẾN TRÚC THƯỢNG TẦNG GÁC CỔNG
# =====================================================================
AMAZON_LINK_FILE = "Amazon_Link.txt"
GITHUB_USER = "ImmediatelyFast1975"
METAMASK_WALLET = "0xfb6Db0A7D69f739e7f85aEc0676BADcAe04ED66B"
OUTPUT_DIR = "output_websites"

def thiet_lap_ha_tang_tu_dong():
    folders = ["src", "src/scrapers", "src/processors", "src/publishers", OUTPUT_DIR]
    for f in folders:
        if not os.path.exists(f): 
            os.makedirs(f)
    with open("src/scrapers/__init__.py", "w") as f: f.write("")
    with open("src/processors/__init__.py", "w") as f: f.write("")
    with open("src/publishers/__init__.py", "w") as f: f.write("")

thiet_lap_ha_tang_tu_dong()

def doc_link_amazon_ngau_nhien():
    if not os.path.exists(AMAZON_LINK_FILE):
        return "https://www.amazon.com/s?k=trending&tag=immediately0a-20"
    try:
        with open(AMAZON_LINK_FILE, 'r', encoding='utf-8') as f:
            links = [line.strip() for line in f if line.strip().startswith('http')]
        if links:
            return random.choice(links)
    except:
        pass
    return "https://www.amazon.com/s?k=trending&tag=immediately0a-20"

def make_safe_filename(text):
    return re.sub(r'[^a-z0-9_-]', '', text.lower().strip().replace(" ", "_"))

def clear_old_cache(output_dir):
    if os.path.exists(output_dir):
        try:
            shutil.rmtree(output_dir)
        except:
            pass
    os.makedirs(output_dir, exist_ok=True)

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})

def cao_google_trends():
    try:
        res = session.get("https://trends.google.com/trending/rss?geo=US", timeout=5)
        root = ET.fromstring(res.text)
        return [{"kw": item.find('title').text, "src": "Google"} for item in root.findall('.//item')][:15]
    except: 
        return []

def cao_pinterest_trends():
    try:
        res = session.get("https://www.pinterest.com/trending.rss", timeout=5)
        root = ET.fromstring(res.text)
        return [{"kw": item.find('title').text, "src": "Pinterest"} for item in root.findall('.//item')][:15]
    except:
        return [
            {"kw": "Home Decor Upgrades", "src": "Pinterest_Backup"},
            {"kw": "Summer Fashion US", "src": "Pinterest_Backup"}
        ]

def nha_may_noi_dung_hang_loat(item):
    kw = item["kw"]
    src = item["src"]
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    safe_name = make_safe_filename(kw)
    file_name = f"{OUTPUT_DIR}/article_{safe_name}.html"
    link_amazon_cua_sep = doc_link_amazon_ngau_nhien()
    
    html = f"""<html>
<head><meta charset='utf-8'><title>US Viral Trend: {kw}</title></head>
<body style='font-family:Arial,sans-serif; background:#0f172a; color:#f8fafc; padding:40px; margin:0;'>
    <script src="https://pl29501995.effectivecpmnetwork.com/2e/98/26/2e98268e726a9051ec5b2a4135031afd.js"></script>

    <div style='max-width:700px; margin:auto; background:#1e293b; padding:40px; border-radius:12px;'>
        <h1 style='color:#38bdf8; margin-top:0;'>🔥 Hot US Trend: {kw}</h1>
        <p style='color:#94a3b8;'><b>Source:</b> {src} | <b>Verified:</b> {now_str}</p>
        <div style='background:#f43f5e; padding:18px; border-radius:8px; text-align:center; margin:25px 0;'>
            <a href='{link_amazon_cua_sep}' style='color:white; font-weight:bold; text-decoration:none;' target='_blank'>
                🛒 Shop Trending {kw} On Amazon Now &rarr;
            </a>
        </div>
        <div style='background:#0f172a; padding:15px; border-radius:6px; text-align:center;'>
            <p style='color:#10b981; font-weight:bold;'>[PAYMENT METHOD] Crypto Destination:</p>
            <code style='color:#38bdf8;'>{METAMASK_WALLET}</code>
        </div>
    </div>
</body>
</html>"""
    with open(file_name, "w", encoding="utf-8") as f: 
        f.write(html)
    return {"kw": kw, "file": f"article_{safe_name}.html", "src": src}

def build_seo_infrastructure(results):
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    domain = "https://" + GITHUB_USER + ".github.io"

    html = f"""<html><head><meta charset='utf-8'><title>LIVE BOARD</title></head>
<body style='font-family:Arial,sans-serif; background:#0f172a; color:#f8fafc; padding:40px;'>
    <div style='max-width:800px; margin:auto;'>
        <h1 style='color:#38bdf8; text-align:center;'>🚀 LIVE TRAFFIC BOARD (US MARKET)</h1>"""
    for r in results:
        html += f"""<div style='background:#1e293b; padding:20px; border-radius:8px; margin-bottom:15px;'>
            <h3 style='margin:0;'><a href='{OUTPUT_DIR}/{r["file"]}' style='color:#38bdf8; text-decoration:none;'>{r["kw"]} ➔</a></h3>
        </div>"""
    html += "</div></body></html>"
    with open("index.html", "w", encoding="utf-8") as f: f.write(html)

    sitemap = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    for r in results: sitemap += f'<url><loc>{domain}/{OUTPUT_DIR}/{r["file"]}</loc></url>'
    sitemap += '</urlset>'
    with open("sitemap.xml", "w", encoding="utf-8") as f: f.write(sitemap)

    # KHÓA CHẶT BẢO MẬT: KHÔNG NHÚNG TOKEN VÀO CODE NỮA
    try:
        if not os.path.exists(".git"):
            subprocess.run(["git", "init"], stdout=subprocess.DEVNULL)
            safe_url = f"https://github.com/{GITHUB_USER}/{GITHUB_USER}.github.io.git"
            subprocess.run(["git", "remote", "add", "origin", safe_url], stdout=subprocess.DEVNULL)
        
        subprocess.run(["git", "add", "."], stdout=subprocess.DEVNULL)
        subprocess.run(["git", "commit", "-m", "Auto-Sync-" + now_str], stdout=subprocess.DEVNULL)
        subprocess.run(["git", "push", "-u", "origin", "main", "--force"], stdout=subprocess.DEVNULL)
        print(" -> [SERVER SYNC OK] Da tu dong push du lieu an toan.")
    except:
        pass

def execute_one_cycle():
    clear_old_cache(OUTPUT_DIR)
    all_items = cao_google_trends() + cao_pinterest_trends()
    if not all_items: all_items = [{"kw": "Next-Gen Retail Boom", "src": "Backup_Core"}]
        
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(nha_may_noi_dung_hang_loat, all_items))
        
    build_seo_infrastructure(results)
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] -> [CYCLE OK] Hoan thanh chu ky.")

if __name__ == "__main__":
    print("[MÁY IN TIỀN v41.0] BẢO MẬT TOKEN TUYỆT ĐỐI")
    vong_lap = 1
    while True:
        execute_one_cycle()
        sleep_seconds = random.randint(15, 45) * 60
        while sleep_seconds > 0:
            mins, secs = divmod(sleep_seconds, 60)
            print(f" -> Tự động vận hành... {mins:02d}:{secs:02d}...", end="\r")
            time.sleep(1)
            sleep_seconds -= 1
        vong_lap += 1