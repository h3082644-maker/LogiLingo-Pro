import streamlit as st
from playwright.sync_api import sync_playwright
import time
import os

st.set_page_config(page_title="Fast Access Tracker", page_icon="📦", layout="wide")
st.title("📦 Fast Access Shipment Tracker (Naqel - Live Snapshot)")

tracking_numbers = st.text_area("أصق أرقام شحنات ناقل هنا (كل رقم في سطر):", height=150)

def capture_naqel_live(tracking_num):
    try:
        with sync_playwright() as p:
            # تشغيل المتصفح بوضع headless آمن لمنع تعليق الموارد
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            url = f"https://www.naqelexpress.com/en/tracking/?shipment={tracking_num}"
            
            # الانتقال والانتظار حتى يستقر الموقع تماماً
            page.goto(url, wait_until="load", timeout=35000)
            page.wait_for_timeout(3500)  # انتظر 3.5 ثانية كاملة لضمان اكتمال حقن البيانات
            
            img_path = f"shipment_{tracking_num}.png"
            
            # التقاط صورة للجزء العلوي من الصفحة الذي يحتوي على الجدول والبيانات
            page.screenshot(path=img_path, full_page=False)
            browser.close()
            return img_path
    except Exception:
        return None

if st.button("جلب صور التتبع الحية فوراً 🚀"):
    if tracking_numbers.strip():
        numbers_list = [num.strip() for num in tracking_numbers.split("\n") if num.strip()]
        
        progress_bar = st.progress(0)
        status_message = st.empty()
        
        for i, num in enumerate(numbers_list):
            status_message.text(f"⏳ جاري تصوير حالة الشحنة الرسمية ({i+1}/{len(numbers_list)}): {num}")
            
            img_result = capture_naqel_live(num)
            
            st.subheader(f"📦 شحنة رقم: {num}")
            if img_result and os.path.exists(img_result):
                # عرض الصورة الحية الملتقطة مباشرة للمستخدم
                st.image(img_result, caption=f"الحالة المباشرة للشحنة {num} من موقع ناقل الحقيقي", use_container_width=True)
                # تنظيف الملفات المؤقتة تلقائياً
                try: os.remove(img_result) except: pass
            else:
                st.error(f"❌ لم نتمكن من الاتصال بموقع ناقل للشحنة {num} حالياً")
                
            progress_bar.progress((i + 1) / len(numbers_list))
            time.sleep(1)
            
        status_message.success("✅ تم سحب الحالات الرسمية بنجاح وتخطي مشكلة الأكواد!")
    else:
        st.warning("الرجاء إدخال رقم شحنة واحد على الأقل.")