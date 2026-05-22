# -*- coding: utf-8 -*-
# Path: C:/Auto_Traffic_Empire/crawler_builder.py
import os
import time
import glob
import random

# KHÓA CHỨNG ĐƯỜNG DẪN ĐÍCH ĐỒNG BỘ 100% VÀO THƯ MỤC CON
OUTPUT_DIR = r"C:\Auto_Traffic_Empire\output_websites"
os.makedirs(OUTPUT_DIR, exist_ok=True)

AMAZON_TRACKING_ID = "vucu2026-20" 

ADSENSE_CODE_BLOCK = """
    <div style="background: #f1f1f1; border: 1px solid #ccc; padding: 10px; margin: 15px 0; text-align: center; color: #777; font-size: 12px; font-weight: bold;">
        📢 SPONSORED ADVERTISING (US PREMIUM NETWORK)<br>
        <div style="width:100%; height:90px; background:#e2e2e2; display:flex; align-items:center; justify-content:center; color:#555;">
            [Banner Quảng Cáo Tự Động Tiền Đô La Mỹ CPC/CPM]
        </div>
    </div>
"""

def lay_san_pham_amazon(keyword):
    matrix = [
        {"name": f"Limited Edition {keyword} Premium T-Shirt", "price": "$24.99"},
        {"name": f"The Untold Story of {keyword} - Hardcover Book", "price": "$19.95"}
    ]
    sp = random.choice(matrix)
    return sp["name"], sp["price"], f"https://www.amazon.com/s?k={keyword.replace(' ', '+')}&tag={AMAZON_TRACKING_ID}"

def tao_money_page_html(trend_name):
    filename = f"article_20260522_{trend_name.lower().replace(' ', '_')}.html"
    file_path = os.path.join(OUTPUT_DIR, filename)
    sp_name, sp_price, amz_link = lay_san_pham_amazon(trend_name)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>{trend_name.upper()} - US Trends</title></head>
<body>
    {ADSENSE_CODE_BLOCK}
    <h1>🔥 HOT TRENDING: What Happened to {trend_name.upper()} Today?</h1>
    <p>Massive traffic searches detected in US for <strong>{trend_name}</strong>.</p>
    <div style="border: 2px dashed #ff9900; background: #fff9f0; padding: 20px; text-align: center;">
        <h3>🛒 AMAZON US DEALS</h3>
        <p><strong>{sp_name}</strong> - Price: {sp_price}</p>
        <a href="{amz_link}" target="_blank" style="background:#ff9900; color:#fff; padding:10px 20px; text-decoration:none; font-weight:bold;">Buy on Amazon USA</a>
    </div>
    {ADSENSE_CODE_BLOCK}
</body>
</html>"""
    with open(file_path, "w", encoding="utf-8") as f: f.write(html_content)

def cap_nhat_index_html_safe_atomic():
    """GỘP TÀI NGUYÊN VÀO KHU VỰC ĐỒNG BỘ: Ép đổi tên file để bẻ gãy bẫy khóa quyền file index của Windows"""
    try:
        html_files = glob.glob(os.path.join(OUTPUT_DIR, "*.html"))
        links_content = ""
        for f in html_files:
            name = os.path.basename(f)
            if "index" in name: continue
            title = name.replace("article_20260522_", "").replace(".html", "").replace("_", " ").upper()
            links_content += f'<li><a href="./{name}" style="color: #0066cc; font-weight: bold; text-decoration: none;">🔥 {title} [AdSense + Amazon Active]</a></li>\n'
            
        index_path = os.path.join(OUTPUT_DIR, "index.html")
        temp_index_path = os.path.join(OUTPUT_DIR, "index.tmp")
        
        # BƠM GIAO DIỆN QUẢNG CÁO HÁI TIỀN ĐÔ CỦA ẢNH 3 VÀO FILE TRONG THƯ MỤC CON
        html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>USA REAL-TIME TRAFFIC COMMAND CENTER</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #f9f9f9; color: #333; }}
        .command-card {{ max-width: 800px; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin: 0 auto; }}
        h1 {{ color: #d9534f; border-bottom: 2px solid #d9534f; padding-bottom: 12px; margin-top: 0; }}
        ul {{ padding-left: 20px; line-height: 2.2; font-size: 15px; }}
        .time-badge {{ background: #5cb85c; color: white; padding: 3px 8px; border-radius: 4px; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="command-card">
        {ADSENSE_CODE_BLOCK}
        
        <h1>🇺🇸 US Traffic Command Center - Time: <span class="time-badge">{time.strftime('%H:%M:%S')}</span></h1>
        <p style="font-style: italic; color: #666;">Active monetization network sync pages (Google SEO & Pinterest Core Ready).</p>
        
        <ul>
            {links_content}
        </ul>
        
        {ADSENSE_CODE_BLOCK}
    </div>
</body>
</html>"""
        
        with open(temp_index_path, "w", encoding="utf-8") as f:
            f.write(html_template)
            
        if os.path.exists(index_path):
            try: os.remove(index_path)
            except: pass
            
        os.replace(temp_index_path, index_path)
        print(f"📊 [ĐỒNG BỘ THÀNH CÔNG] index.html trong output_websites nhảy giây thời gian thực: {time.strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"⚠️ Hệ thống xử lý nghẽn mạch file: {str(e)}")

if __name__ == "__main__":
    mock_trends = ["6ix9ine", "Amy Sedaris", "Angels Game", "Athletics", "Aubrey Plaza", "CBS News"]
    while True:
        current_trend = random.choice(mock_trends)
        tao_money_page_html(current_trend)
        cap_nhat_index_html_safe_atomic()
        time.sleep(30)