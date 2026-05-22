import os
import glob
import datetime
import xml.etree.ElementTree as ET

print("\n==================================================")
print("[HỆ THỐNG] TIẾN HÀNH THU THẬP DATA VÀ TỰ ĐỘNG VIẾT BÀI...")
print("==================================================")

# 1. Tự động quét tìm file dữ liệu thô mới nhất từ mạng Mỹ
url = "https://trends.google.com/trending/rss?geo=US"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

try:
    import urllib.request
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as response:
        xml_data = response.read().decode('utf-8')
    
    root = ET.fromstring(xml_data)
    trends = []
    for item in root.findall('.//item'):
        title = item.find('title').text
        approx_traffic = item.find('{https://trends.google.com/trending/rss}approx_traffic')
        traffic = approx_traffic.text if approx_traffic is not None else "50,000+"
        trends.append({"kw": title, "traffic": traffic})
except Exception as e:
    print(f"[MẠNG] Không lấy được RSS mới, dùng data backup khẩn cấp. Lỗi: {e}")
    trends = [
        {"kw": "Memorial Day 2026", "traffic": "200,000+"},
        {"kw": "Whit Monday", "traffic": "50,000+"},
        {"kw": "Nuggets vs Timberwolves", "traffic": "50,000+展示"}
    ]

# 2. Xử lý đẻ bài viết hàng loạt chuẩn cấu trúc
os.makedirs("output_websites", exist_ok=True)
now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

print(f"[THÔNG BÁO] Phát hiện {len(trends)} chủ đề hot. Tiến hành xào bài...")

for trend in trends[:5]: # Tự động đẻ top 5 bài viết hot nhất
    kw = trend["kw"]
    safe_name = kw.lower().replace(' ', '_').replace(':', '').replace('/', '')
    file_name = f"output_websites/article_{safe_name}.html"
    
    html_content = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{kw} - Viral News Update</title>
        <style>
            body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #0f172a; color: #f8fafc; padding: 40px; margin: 0; }}
            .card {{ max-width: 700px; margin: auto; background: #1e293b; padding: 40px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); border: 1px solid #334155; }}
            h1 {{ color: #38bdf8; font-size: 2.2em; margin-top: 0; }}
            .badge {{ background: #f43f5e; color: white; padding: 4px 10px; font-weight: bold; border-radius: 4px; font-size: 0.9em; }}
            .time {{ color: #94a3b8; font-size: 0.9em; margin-bottom: 20px; }}
            p {{ line-height: 1.8; font-size: 1.1em; color: #cbd5e1; text-align: justify; }}
            .ad-box {{ background: #334155; border: 2px dashed #64748b; padding: 20px; text-align: center; margin: 25px 0; color: #94a3b8; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="card">
            <span class="badge">🔥 TOP TRENDING US</span>
            <h1>Massive Search Spike for: {kw}</h1>
            <div class="time">🚀 Auto-Generated Article | Captured at: {now} | Search Volume: {trend['traffic']}</div>
            
            <p>The online community across the United States is currently showing immense interest in <b>{kw}</b>. According to real-time search engine metrics, traffic for this topic surged rapidly, accumulating over <b>{trend['traffic']} searches</b> within a minimal timeframe.</p>
            
            <div class="ad-box">
                [ KHÔNG GIAN ĐẶT QUẢNG CÁO GOOGLE ADSENSE ĐỂ BÚ TIỀN TRAFFIC ]
            </div>
            
            <p>As <b>{kw}</b> dominates social feeds and news updates, our automated platform is gathering deeper insights to provide a full analysis. Stay tuned for deeper breakdowns regarding this breaking event.</p>
        </div>
    </body>
    </html>"""
    
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f" ➔ Đã đẻ bài viết xịn tại: {file_name}")

print("==================================================\n")