import streamlit as st
import random
from data import words
from gtts import gTTS
import io
import base64

# 1. إعدادات الصفحة المهيأة للجوال وبدون مسافات علوية مقصوصة
st.set_page_config(
    page_title="LogiLingo Premium",
    page_icon="📦",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. حزمة الـ CSS العصري الفاتح (بدون أي تداخل مع الأكواد)
st.markdown("""
<style>
/* تهيئة الخلفية العامة وتناسق العناصر */
.stApp { background-color: #F8FAFC !important; color: #1E293B !important; }
.block-container { padding-top: 2rem !important; padding-bottom: 2rem; max-width: 480px; }

/* الهوية البصرية */
.brand-header { text-align: center; margin-bottom: 15px; }
.brand-title { font-size: 2.1rem; font-weight: 800; color: #0F172A; letter-spacing: -0.5px; }
.brand-tagline { font-size: 0.9rem; color: #64748B; font-weight: 500; margin-top: 2px; }

/* العداد وشريط التقدم */
.stats-pill {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.05);
    border-radius: 9999px;
    padding: 6px 16px;
    display: inline-block;
    font-size: 0.85rem;
    color: #0284C7;
    font-weight: 600;
    margin-bottom: 10px;
}
.center-box { text-align: center; margin-top: 5px; }

/* بطاقات المهارة (Glassmorphism Light) */
.main-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    box-shadow: 0px 10px 25px -5px rgba(0, 0, 0, 0.03);
    border-radius: 24px;
    padding: 22px;
    margin-bottom: 15px;
    text-align: center;
}

.category-tag { font-size: 0.75rem; font-weight: 700; color: #0EA5E9; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px; }
.word-display { font-size: 2.4rem; font-weight: 800; color: #0F172A; margin: 10px 0; }
.pronounce-tag { font-size: 1.05rem; color: #64748B; font-weight: 500; background: #F1F5F9; padding: 4px 12px; border-radius: 8px; display: inline-block; }

/* عناصر كشف المحتوى التفاعلي النظيف */
.translation-box { font-size: 1.8rem; font-weight: 800; color: #10B981; direction: rtl; text-align: center; margin: 15px 0; padding-top: 15px; border-top: 1px solid #F1F5F9; }
.context-block { background: #F8FAFC; border-radius: 16px; padding: 14px; border-left: 4px solid #0EA5E9; margin-top: 12px; text-align: left; }
.context-en { font-size: 0.95rem; color: #334155; font-weight: 500; }
.context-ar { font-size: 0.95rem; color: #475569; text-align: right; direction: rtl; margin-top: 4px; }

.email-block { background: #F0FDF4; border-radius: 16px; padding: 14px; border: 1px dashed #BBF7D0; margin-top: 15px; text-align: left; }
.email-header { font-size: 0.85rem; font-weight: 700; color: #15803D; margin-bottom: 6px; }
.email-content { background: #FFFFFF; padding: 12px; border-radius: 12px; font-family: monospace; font-size: 0.85rem; color: #1E293B; white-space: pre-wrap; border: 1px solid #E2E8F0; }

/* تخصيص مظهر وحجم الأزرار بالكامل للعمل باللمس السريع */
div.stButton > button {
    border-radius: 16px !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    padding: 12px 20px !important;
    border: none !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

# 3. إدارة الجلسة (Session State) التفاعلية للأزرار والعدادات
if 'word_idx' not in st.session_state:
    st.session_state.word_idx = 0
if 'step' not in st.session_state:
    st.session_state.step = 1  # 1: الكلمة فقط، 2: الترجمة والسياق، 3: الإيميل الكامل
if 'score' not in st.session_state:
    st.session_state.score = 0

# دالات التنقل السلسة بين البطاقات
def do_next():
    st.session_state.word_idx = (st.session_state.word_idx + 1) % len(words)
    st.session_state.step = 1

def do_prev():
    st.session_state.word_idx = (st.session_state.word_idx - 1) % len(words)
    st.session_state.step = 1

def trigger_reveal():
    st.session_state.step += 1
    if st.session_state.step == 2:
        st.session_state.score += 1

# 4. رسم الهوية والـ Header العلوي
st.markdown('<div class="brand-header"><div class="brand-title">📦 LogiLingo Pro</div><div class="brand-tagline">مساعدك المهني التفاعلي لإتقان المصطلحات اللوجستية</div></div>', unsafe_allow_html=True)
st.markdown(f'<div class="center-box"><div class="stats-pill">⚡ النقاط الحالية: {st.session_state.score} مهارة</div></div>', unsafe_allow_html=True)

# جلب بيانات العنصر ومؤشر التقدم
current_item = words[st.session_state.word_idx]
progress_val = (st.session_state.word_idx + 1) / len(words)
st.progress(progress_val)
st.caption(f"المصطلح {st.session_state.word_idx + 1} من أصل {len(words)}")

# --- 5. عرض البطاقة الأساسية النظيفة (بدون تجميع متغيرات HTML الحاضنة للمشاكل) ---
st.markdown(f"""
<div class="main-card">
    <div class="category-tag">{current_item['category']}</div>
    <div class="word-display">{current_item['en']}</div>
    <div class="center-box"><span class="pronounce-tag">🗣️ {current_item['pronunciation']}</span></div>
</div>
""", unsafe_allow_html=True)

# تفريغ وعرض الترجمة والسياق برمجياً بشكل منفصل ومضمون عند تفعيل المرحلة الثانية
if st.session_state.step >= 2:
    st.markdown(f'<div class="translation-box">🎯 {current_item["ar"]}</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="context-block">
        <div class="context-en"><b>EN:</b> {current_item['ex_en']}</div>
        <div class="context-ar"><b>AR:</b> {current_item['ex_ar']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # ميزة النطق التلقائي بدون مشغل صوتي بشع
    try:
        tts = gTTS(text=current_item['en'], lang='en')
        sound_fp = io.BytesIO()
        tts.write_to_fp(sound_fp)
        sound_fp.seek(0)
        b64_audio = base64.b64encode(sound_fp.read()).decode()
        st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{b64_audio}"></audio>', unsafe_allow_html=True)
    except:
        pass

# عرض كود الإيميل التطبيقي النظيف عند تفعيل المرحلة الثالثة والأخيرة للكلمة
if st.session_state.step == 3:
    st.markdown(f"""
    <div class="email-block">
        <div class="email-header">{current_item['email_title']}</div>
        <div class="email-content">{current_item['email_body']}</div>
    </div>
    """, unsafe_allow_html=True)

st.write(" ")

# --- 6. لوحة أزرار التحكم والتنقل الدائمة والث
