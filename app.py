import streamlit as st
import random
from data import words
from gtts import gTTS
import io
import base64

# 1. إعدادات متطورة للجوال
st.set_page_config(
    page_title="LogiLingo Premium",
    page_icon="📦",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. تصميم عصري فاخر (Ultra-Modern Premium Light)
st.markdown("""
<style>
/* تهيئة الخلفية العامة وألوان الخطوط */
.stApp { background-color: #F8FAFC !important; color: #1E293B !important; }
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; max-width: 480px; }

/* الهوية البصرية الجديدة - عصرية وأنيقة */
.brand-header { text-align: center; margin-bottom: 20px; }
.brand-title { font-size: 2.2rem; font-weight: 800; color: #0F172A; letter-spacing: -0.5px; }
.brand-tagline { font-size: 0.95rem; color: #64748B; font-weight: 500; margin-top: 4px; }

/* العداد وشريط التقدم العصري */
.stats-pill {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.05);
    border-radius: 9999px;
    padding: 6px 16px;
    display: inline-block;
    font-size: 0.9rem;
    color: #0284C7;
    font-weight: 600;
    margin-bottom: 15px;
}
.center-box { text-align: center; }

/* بطاقات التعلم الزجاجية (Glassmorphism Light) */
.main-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    box-shadow: 0px 10px 25px -5px rgba(0, 0, 0, 0.05), 0px 8px 10px -6px rgba(0, 0, 0, 0.05);
    border-radius: 24px;
    padding: 24px;
    margin-bottom: 16px;
}

.category-tag { font-size: 0.75rem; font-weight: 700; color: #0EA5E9; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px; }
.word-display { font-size: 2.5rem; font-weight: 800; color: #0F172A; margin: 12px 0; }
.pronounce-tag { font-size: 1.1rem; color: #64748B; font-weight: 500; background: #F1F5F9; padding: 4px 12px; border-radius: 8px; display: inline-block; }

/* أقسام كشف المعلومات المتتابعة */
.reveal-section {
    border-top: 1px solid #F1F5F9;
    margin-top: 20px;
    padding-top: 20px;
}
.translation-text { font-size: 1.8rem; font-weight: 800; color: #10B981; direction: rtl; text-align: right; margin-bottom: 12px; }

.context-block { background: #F8FAFC; border-radius: 16px; padding: 14px; border-left: 4px solid #0EA5E9; margin-top: 10px; }
.context-en { font-size: 0.95rem; color: #334155; text-align: left; font-weight: 500; }
.context-ar { font-size: 0.95rem; color: #475569; text-align: right; direction: rtl; margin-top: 4px; }

.email-block { background: #F0FDF4; border-radius: 16px; padding: 14px; border: 1px dashed #BBF7D0; margin-top: 12px; text-align: left; }
.email-header { font-size: 0.9rem; font-weight: 700; color: #15803D; margin-bottom: 6px; }
.email-content { background: #FFFFFF; padding: 12px; border-radius: 12px; font-family: monospace; font-size: 0.85rem; color: #1E293B; white-space: pre-wrap; border: 1px solid #E2E8F0; }

/* تخصيص أزرار تفاعلية عصرية تلغي النظام القديم وتدعم نقرات الجوال */
div.stButton > button {
    background: #0F172A !important;
    color: #FFFFFF !important;
    border-radius: 16px !important;
    font-weight: 600 !important;
    font-size: 1.05rem !important;
    padding: 14px 24px !important;
    border: none !important;
    box-shadow: 0px 4px 12px rgba(15, 23, 42, 0.15) !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
}
div.stButton > button:active { transform: scale(0.98); }
</style>
""", unsafe_allow_html=True)

# 3. إدارة الحالة لضمان سلاسة التنقل والتفاعل
if 'word_idx' not in st.session_state:
    st.session_state.word_idx = 0
if 'step' not in st.session_state:
    st.session_state.step = 1  # 1: الكلمة، 2: الترجمة والسياق، 3: الإيميل المهني
if 'mastered_count' not in st.session_state:
    st.session_state.mastered_count = 0

def next_card():
    st.session_state.word_idx = (st.session_state.word_idx + 1) % len(words)
    st.session_state.step = 1

def prev_card():
    st.session_state.word_idx = (st.session_state.word_idx - 1) % len(words)
    st.session_state.step = 1

def advance_step():
    st.session_state.step += 1
    if st.session_state.step == 2:
        st.session_state.mastered_count += 1

# 4. بناء الهوية البصرية الرئيسية والـ Counter
st.markdown("""
<div class="brand-header">
    <div class="brand-title">📦 LogiLingo Pro</div>
    <div class="brand-tagline">منصة المحاكاة التفاعلية لمصطلحات سلاسل الإمداد</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"<div class='center-box'><div class='stats-pill'>⚡ الإنجاز الحالي: {st.session_state.mastered_count} نقاط مهارة</div></div>", unsafe_allow_html=True)

# جلب المصطلح النشط حالياً
item = words[st.session_state.word_idx]

# شريط التقدم العصري النحيف
progress_val = (st.session_state.word_idx + 1) / len(words)
st.progress(progress_val)
st.caption(f"المصطلح {st.session_state.word_idx + 1} من أصل {len(words)}")

# --- بطاقة التعلم العصرية الموحدة ---
card_html = f"""
<div class="main-card">
    <div class="category-tag">{item['category']}</div>
    <div class="word-display">{item['en']}</div>
    <div class="center-box"><span class="pronounce-tag">🗣️ {item['pronunciation']}</span></div>
"""

if st.session_state.step >= 2:
    card_html += f"""
    <div class="reveal-section">
        <div class="translation-text">🎯 {item['ar']}</div>
        <div class="context-block">
            <div class="context-en"><b>EN:</b> {item['ex_en']}</div>
            <div class="context-ar"><b>AR:</b> {item['ex_ar']}</div>
        </div>
    </div>
    """

if st.session_state.step == 3:
    card_html += f"""
    <div class="reveal-section">
        <div class="email-block">
            <div class="email-header">{item['email_title']}</div>
            <div class="email-content">{item['email_body']}</div>
        </div>
    </div>
    """

card_html += "</div>"
st.markdown(card_html, unsafe_allow_html=True)

# تفعيل النطق الصوتي التلقائي المخفي بدون مشغل صوتي مشوه للتصميم
if st.session_state.step >= 2:
    try:
        tts = gTTS(text=item['en'], lang='en')
        sound_fp = io.BytesIO()
        tts.write_to_fp(sound_fp)
        sound_fp.seek(0)
        b64_audio = base64.b64encode(sound_fp.read()).decode()
        audio_tag = f'<audio autoplay src="data:audio/mp3;base64,{b64_audio}"></audio>'
        st.markdown(audio_tag, unsafe_allow_html=True)
    except:
        pass

# --- أزرار التحكم والتنقل السلسة أسفل البطاقة ---
st.write(" ")
if st.session_state.step == 1:
    if st.button("👁️ كشف الترجمة الفورية والمعنى", key="btn_step_1"):
        advance_step()
        st.rerun()

elif st.session_state.step == 2:
    if st.button("📩 استعراض سياق الإيميل المهني", key="btn_step_2"):
        advance_step()
        st.rerun()

elif st.session_state.step == 3:
    # أزرار التنقل بين الكلمات السابقة والتالية عند إنهاء مراحل التعلم
    col_prev, col_next = st.columns(2)
    with col_prev:
        if st.button("⬅️ السابق", key="btn_prev"):
            prev_card()
            st.rerun()
    with col_next:
        if st.button("التالي ➡️", key="btn_next"):
            next_card()
            st.rerun()

# --- قسم تصفح إضافي للمحترفين ---
st.write("---")
with st.expander("🔍 محرك البحث الفوري عن المصطلحات"):
    query = st.text_input("ابحث عن أي مصطلح باللغة العربية أو الإنجليزية:").strip().lower()
    if query:
        res = [w for w in words if query in w['en'].lower() or query in w['ar']]
        if res:
            for w in res:
                st.success(f"🔹 **{w['en']}**: {w['ar']}")
        else:
            st.warning("لا توجد نتائج مطابقة لبحثك.")
