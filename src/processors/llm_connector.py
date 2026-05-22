# -*- coding: utf-8 -*-
def bieu_dien_noi_dung(kw, src):
    vi = "0xfb6Db0A7D69f739e7f85aEc0676BADcAe04ED66B"
    link = f"https://www.amazon.com/s?k={kw.replace(' ','+')}&tag=your_tag-20"
    return f"<h1>🔥 Viral: {kw}</h1><p>Source: {src}</p><p><a href='{link}'>Buy on Amazon</a></p><code>Wallet: {vi}</code>"