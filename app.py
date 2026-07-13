import streamlit as st
from data import words
from gtts import gTTS
import io
import base64

# إعدادات الواجهة
st.set_page_config(page_title="LogiLingo Pro", layout="centered")

# CSS المخصص للإطار الواحد
st.markdown("""
<style>
.main-frame {
    border: 2px solid #E2E8F0;
    border-radius: 20px;
    padding: 20px;
    background-color: #FFFFFF;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}
.header-row { display: flex; justify-content: space-between; font-weight: bold; color: #64748B; margin-bottom: 10px; }
.word-title { font-size: 2.5rem; font-weight: 800; color: #0F172A; text-align: center; margin: 20px 0; }
div.stButton > button { width: 100%; border-radius: 12px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# إدارة الحالة
if 'idx' not in st.session_state: st.session_state.idx = 0
if 'show' not in st.session_state: st.session_state.show = False

item = words[st.session_state.idx]

# --- بدء الإطار الواحد ---
with st.container():
    st.markdown('<div class="main-frame">', unsafe_allow_html=True)
    
    # 1. الهيدر (العنوان + العدادات)
    st.markdown('<div class="header-row"><span>📦 LogiLingo Pro</span><span>🔥12 ⭐540</span></div>', unsafe_allow_html=True)
    
    # 2. شريط التقدم
    st.progress((st.session_state.idx + 1) / len(words))
    
    # 3. المصطلح
    st.markdown(f'<div class="word-title">🚚 {item["en"]}</div>', unsafe_allow_html=True)
    
    # 4. التفاعل (زر الكشف)
    if not st.session_state.show:
        if st.button("اضغط لإظهار الترجمة"):
            st.session_state.show = True
            st.rerun()
    else:
        st.success(f"🎯 {item['ar']}")
        # تشغيل الصوت
        try:
            tts = gTTS(text=item['en'], lang='en')
            fp = io.BytesIO(); tts.write_to_fp(fp); fp.seek(0)
            b64 = base64.b64encode(fp.read()).decode()
            st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{b64}"></audio>', unsafe_allow_html=True)
        except: pass
        if st.button("إخفاء الترجمة"):
            st.session_state.show = False
            st.rerun()

    # 5. أزرار التنقل (في صف واحد)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("◀ السابق"):
            st.session_state.idx = (st.session_state.idx - 1) % len(words)
            st.session_state.show = False
            st.rerun()
    with c2:
        if st.button("التالي ▶"):
            st.session_state.idx = (st.session_state.idx + 1) % len(words)
            st.session_state.show = False
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
