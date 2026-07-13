import streamlit as st
import random
from data import words
from gtts import gTTS
import io

# 1. إعدادات الصفحة المهيأة للجوال
st.set_page_config(
    page_title="LogiLingo Light",
    page_icon="🦉",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. تصميم CSS الفاتح والمبهج (Duolingo Light Theme)
st.markdown("""
<style>
/* إعداد الخلفية العامة الفاتحة للتطبيق */
.stApp { background-color: #FAFAFA !important; color: #3C3C3C !important; }

/* إلغاء الفراغات العلوية للجوال */
.block-container { padding-top: 1rem; padding-bottom: 2rem; max-width: 460px; }

/* العناوين الأساسية ستايل دولينجو الملون */
.duo-title { font-size: 2.2rem; font-weight: 800; text-align: center; color: #58CC02; margin-bottom: 0px; text-shadow: 1px 1px 0px #46A302; }
.duo-sub { text-align: center; color: #777777; font-size: 0.95rem; margin-bottom: 15px; font-weight: 500; }

/* بطاقة اللعبة التفاعلية الفاتحة ثلاثية الأبعاد */
.game-card { 
    background-color: #FFFFFF; 
    border: 2px solid #E5E5E5; 
    border-bottom: 6px solid #E5E5E5; 
    border-radius: 20px; 
    padding: 22px; 
    text-align: center; 
    margin-bottom: 15px;
}

.term-en { font-size: 2.2rem; font-weight: bold; color: #1B86FF; margin: 10px 0; }
.term-pron { font-size: 1.05rem; color: #FF9600; font-weight: bold; margin-bottom: 5px; }

/* صناديق الإجابة والسياق الملونة والزاهية */
.answer-box { 
    background-color: #E8F5E9; 
    border: 2px solid #A5D6A7; 
    border-radius: 16px; 
    padding: 15px; 
    margin-top: 12px;
}
.term-ar { font-size: 1.7rem; font-weight: bold; color: #2E7D32; direction: rtl; }

.email-box {
    background-color: #E3F2FD; 
    border: 2px solid #90CAF9; 
    border-radius: 16px; 
    padding: 15px; 
    margin-top: 12px;
    text-align: left;
}
.email-title-text { font-size: 1rem; font-weight: bold; color: #1565C0; margin-bottom: 8px; }
.email-content { background-color: #FFFFFF; padding: 10px; border-radius: 8px; font-family: monospace; font-size: 0.85rem; color: #333333; white-space: pre-wrap; border: 1px solid #BBDEFB; }

/* شريط التميز العلوي */
.streak-banner {
    background-color: #FFF3E0;
    border: 1px solid #FFE0B2;
    border-radius: 15px;
    padding: 5px 15px;
    display: inline-block;
    font-size: 0.9rem;
    color: #E65100;
    font-weight: bold;
    margin-bottom: 15px;
}
.center-wrapper { text-align: center; }

/* تخصيص أزرار Streamlit لتشبه أزرار الألعاب */
div.stButton > button {
    border-radius: 12px !important;
    font-weight: bold !important;
    font-size: 1.05rem !important;
    padding: 10px 20px !important;
    border: none !important;
}
</style>
""", unsafe_allow_html=True)

# 3. إدارة الحالة لحفظ الكلمة الحالية وخطوات التعليم المتبعة
if 'word_index' not in st.session_state:
    st.session_state.word_index = 0
if 'edu_step' not in st.session_state:
    st.session_state.edu_step = 1 # الخطوة 1: الكلمة فقط، 2: كشف الترجمة، 3: كشف الإيميل المهني
if 'streak' not in st.session_state:
    st.session_state.streak = 0

def go_next_word():
    st.session_state.word_index = (st.session_state.word_index + 1) % len(words)
    st.session_state.edu_step = 1

def advance_step():
    st.session_state.edu_step += 1
    if st.session_state.edu_step == 2:
        st.session_state.streak += 1

# 4. الواجهة الرسومية العلوية
st.markdown("<div class='duo-title'>🦉 LogiLingo Light</div>", unsafe_allow_html=True)
st.markdown("<div class='duo-sub'>تعلم الإنجليزية اللوجستية بأسلوب ذكي وسريع</div>", unsafe_allow_html=True)

st.markdown(f"<div class='center-wrapper'><div class='streak-banner'>🔥 مجموع الكلمات المتقنة: {st.session_state.streak}</div></div>", unsafe_allow_html=True)

# جلب بيانات الكلمة الحالية
current_word = words[st.session_state.word_index]

# شريط التقدم التعليمي الديناميكي
progress_percentage = (st.session_state.word_index + 1) / len(words)
st.progress(progress_percentage)
st.caption(f"المستوى الحالي: {st.session_state.word_index + 1} / {len(words)}")

# --- المرحلة الأولى: عرض بطاقة المصطلح الرئيسي ---
st.markdown(f"""
<div class="game-card">
    <div style="color: #999999; font-size: 0.8rem; font-weight: bold; letter-spacing: 0.5px;">{current_word['category']}</div>
    <div class="term-en">{current_word['en']}</div>
    <div class="term-pron">🗣️ {current_word['pronunciation']}</div>
</div>
""", unsafe_allow_html=True)

# --- نظام كشف الإجابات المتتابع تفاعلياً ---
if st.session_state.edu_step >= 2:
    # المرحلة الثانية: ظهور الترجمة والأمثلة السياقية
    st.markdown(f"""
    <div class="answer-box">
        <div style="color: #558B2F; font-size: 0.8rem; font-weight: bold;">🎯 الترجمة المعتمدة:</div>
        <div class="term-ar">{current_word['ar']}</div>
        <div style="height: 1px; background-color: #C8E6C9; margin: 8px 0;"></div>
        <div style="color: #558B2F; font-size: 0.8rem; font-weight: bold; text-align: right;">💡 السياق اليومي:</div>
        <div style="font-size: 0.95rem; color: #2E7D32; text-align: left;"><b>EN:</b> {current_word['ex_en']}</div>
        <div style="font-size: 0.95rem; color: #2E7D32; text-align: right;" dir="rtl"><b>AR:</b> {current_word['ex_ar']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # تشغيل نطق الكلمة صوتياً بصيغة عالية الجودة
    try:
        tts = gTTS(text=current_word['en'], lang='en')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        st.audio(fp, format='audio/mp3')
    except:
        pass

if st.session_state.edu_step == 3:
    # المرحلة الثالثة: كشف إيميل العمل التطبيقي
    st.markdown(f"""
    <div class="email-box">
        <div class="email-title-text">{current_word['email_title']}</div>
        <div class="email-content">{current_word['email_body']}</div>
        <div style="font-size: 0.75rem; color: #1565C0; margin-top: 5px; text-align: right; font-weight: bold;">💡 يمكنك نسخ هذا الإيميل لاستخدامه في شركتك!</div>
    </div>
    """, unsafe_allow_html=True)

st.write(" ")

# --- أزرار التحكم التفاعلية الكبيرة المريحة للجوال ---
if st.session_state.edu_step == 1:
    if st.button("🔎 تحقق من الترجمة والمعنى", use_container_width=True, type="primary"):
        advance_step()
        st.rerun()

elif st.session_state.edu_step == 2:
    if st.button("✉️ كيف أكتبها في إيميل رسمي للشركة؟", use_container_width=True, type="secondary"):
        advance_step()
        st.rerun()

elif st.session_state.edu_step == 3:
    if st.button("المصطلح التالي ➡️", use_container_width=True, type="primary"):
        go_next_word()
        st.rerun()

# --- قسم تصفح سريع إضافي بالأسفل مقفل داخل حاوية ---
st.write("---")
with st.expander("🔍 قائمة البحث الفوري عن المصطلحات والإيميلات"):
    search_query = st.text_input("ابحث باسم المصطلح (e.g. Stock):").strip().lower()
    if search_query:
        found = [w for w in words if search_query in w['en'].lower() or search_query in w['ar']]
        if found:
            for w in found:
                st.info(f"🔹 **{w['en']}** = {w['ar']}")
                st.caption(f"**نموذج الإيميل المتاح:**\n{w['email_body']}")
        else:
            st.warning("لا توجد نتائج مطابقة لبحثك.")
