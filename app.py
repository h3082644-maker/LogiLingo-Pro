import streamlit as st
import random
from data import words
from gtts import gTTS
import io

# 1. إعدادات الصفحة مهيأة بالكامل للجوال والـ Dark Mode
st.set_page_config(
    page_title="LogiLingo Go",
    page_icon="🦉",
    layout="centered", # تجعل المحتوى متناسقاً وعمودياً في منتصف الشاشة
    initial_sidebar_state="collapsed" # إخفاء القائمة الجانبية تلقائياً في الجوال لتوفر مساحة
)

# 2. تصميم CSS احترافي مستوحى من ألوان وتفاعل Duolingo (مخصص للهواتف)
st.markdown("""
<style>
/* إلغاء الفراغات العلوية لجعل التطبيق يبدأ من أعلى الشاشة في الجوال */
.block-container { padding-top: 1.5rem; padding-bottom: 1.5rem; max-width: 480px; }

/* العناوين الأساسية بججم مناسب للجوال */
.duo-title { font-size: 2rem; font-weight: 800; text-align: center; color: #FF4B4B; margin-bottom: 0px; }
.duo-sub { text-align: center; color: #888888; font-size: 0.95rem; margin-bottom: 20px; }

/* بطاقة اللعبة التفاعلية الرئيسية (Duolingo Card) */
.game-card { 
    background-color: #1E2028; 
    border: 2px solid #3E4255; 
    border-bottom: 6px solid #3E4255; /* تأثير الزر ثلاثي الأبعاد */
    border-radius: 18px; 
    padding: 20px; 
    text-align: center; 
    margin-bottom: 15px;
}

/* نصوص المصطلحات داخل البطاقة */
.term-en { font-size: 2.1rem; font-weight: bold; color: #FFFFFF; margin: 10px 0; letter-spacing: 0.5px; }
.term-pron { font-size: 1.1rem; color: #F59E0B; font-style: italic; margin-bottom: 10px; }

/* إجابة مخفية تظهر بشكل رائع */
.answer-box { 
    background-color: #0F172A; 
    border-radius: 12px; 
    padding: 15px; 
    margin-top: 15px; 
    border: 1px solid #10B981;
}
.term-ar { font-size: 1.6rem; font-weight: bold; color: #10B981; direction: rtl; }

/* سياق الجمل */
.context-title { font-size: 0.85rem; color: #888888; text-align: right; margin-top: 10px; font-weight: bold; }
.context-text { font-size: 0.95rem; color: #E2E8F0; text-align: left; margin: 5px 0; }
.context-text-ar { font-size: 0.95rem; color: #A7F3D0; text-align: right; direction: rtl; margin: 5px 0; }

/* عداد النقاط العلوي */
.streak-banner {
    background-color: #2D3142;
    border-radius: 20px;
    padding: 6px 15px;
    display: inline-block;
    font-size: 0.9rem;
    color: #FF9F43;
    font-weight: bold;
    margin-bottom: 15px;
}
.center-wrapper { text-align: center; }
</style>
""", unsafe_allow_html=True)

# 3. إدارة الحالة (State Management) لحفظ النقاط والكلمة الحالية وتفادي إعادة التحميل العشوائي
if 'word_index' not in st.session_state:
    st.session_state.word_index = 0
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False
if 'streak' not in st.session_state:
    st.session_state.streak = 0

# دالة للانتقال للكلمة التالية
def next_question():
    st.session_state.word_index = (st.session_state.word_index + 1) % len(words)
    st.session_state.show_answer = False

# دالة لكشف الإجابة وزيادة العداد
def reveal_answer():
    st.session_state.show_answer = True
    st.session_state.streak += 1

# 4. الواجهة الرئيسية والتصميم المستوحى من Duolingo
st.markdown("<div class='duo-title'>🦉 LogiLingo Go</div>", unsafe_allow_html=True)
st.markdown("<div class='duo-sub'>تحدي وممارسة مصطلحات سلاسل الإمداد اللوجستية</div>", unsafe_allow_html=True)

# عرض عداد الـ Streak والنقاط في المنتصف
st.markdown(f"<div class='center-wrapper'><div class='streak-banner'>🔥 متقن حالياً: {st.session_state.streak} مصطلحات</div></div>", unsafe_allow_html=True)

# جلب بيانات الكلمة الحالية بناء على العداد
current_word = words[st.session_state.word_index]

# شريط التقدم العلوي (Progress Bar) كمستوى تقدم داخل التطبيق
progress_percentage = (st.session_state.word_index + 1) / len(words)
st.progress(progress_percentage)
st.caption(f"المصطلح {st.session_state.word_index + 1} من أصل {len(words)}")

# --- بطاقة التحدي التفاعلية (Flashcard) ---
st.markdown(f"""
<div class="game-card">
    <div style="color: #888888; font-size: 0.8rem; font-weight: bold; text-transform: uppercase;">{current_word['category']}</div>
    <div class="term-en">{current_word['en']}</div>
    <div class="term-pron">🗣️ النطق التقريبي: {current_word['pronunciation']}</div>
</div>
""", unsafe_allow_html=True)

# أزرار التحكم التفاعلية بملء عرض الشاشة ومناسبة لإصبع الجوال
if not st.session_state.show_answer:
    if st.button("🎯 اكشف الترجمة والسياق", use_container_width=True, type="primary"):
        reveal_answer()
        st.rerun()
else:
    # عرض الإجابة والترجمة عند الضغط على الزر السابق
    st.markdown(f"""
    <div class="answer-box">
        <div style="color: #888888; font-size: 0.8rem; font-weight: bold;">الترجمة المهنية المعتمدة:</div>
        <div class="term-ar">🎯 {current_word['ar']}</div>
        <div style="height: 1px; background-color: #2D313E; margin: 10px 0;"></div>
        <div class="context-title">💡 مثال عملي في الشركات:</div>
        <div class="context-text"><b>EN:</b> {current_word['ex_en']}</div>
        <div class="context-text-ar"><b>AR:</b> {current_word['ex_ar']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # تشغيل الصوت تلقائياً أو عند الضغط لعدم استهلاك باقة الجوال
    try:
        tts = gTTS(text=current_word['en'], lang='en')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        st.audio(fp, format='audio/mp3')
    except:
        st.caption("🔊 تشغيل الصوت يتطلب اتصالاً بالإنترنت")

    st.write(" ")
    if st.button("التالي ➡️", use_container_width=True):
        next_question()
        st.rerun()

# --- خيارات سريعة إضافية بالأسفل تظهر بشكل أنيق ---
st.write("---")
with st.expander("🔍 هل تريد البحث عن مصطلح معين بدلاً من اللعب؟"):
    search_query = st.text_input("اكتب الكلمة هنا (مثال: Cargo):").strip().lower()
    if search_query:
        found_words = [w for w in words if search_query in w['en'].lower() or search_query in w['ar']]
        if found_words:
            for w in found_words:
                st.success(f"**{w['en']}** = {w['ar']} ({w['pronunciation']})")
        else:
            st.warning("لم يتم العثور على نتائج.")
