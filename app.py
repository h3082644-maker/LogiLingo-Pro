import streamlit as st
from data import words
from gtts import gTTS
import io

# إعدادات الصفحة المتقدمة
st.set_page_config(
    page_title="LogiLingo Pro v2",
    page_icon="📦",
    layout="centered"
)

# تحسين التصميم عبر CSS مخصص لإلغاء الهوامش الزائدة وترتيب النصوص
st.markdown("""
    <style>
    .main-title { font-size: 2.6rem; font-weight: bold; text-align: center; color: #FF4B4B; margin-bottom: 0.5rem; }
    .sub-title { text-align: center; color: #B0B0B0; margin-bottom: 2rem; }
    .card-label { font-size: 0.9rem; color: #888888; font-weight: bold; margin-bottom: 2px; }
    .card-content { font-size: 1.4rem; font-weight: bold; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown("<div class='main-title'>📦 LogiLingo Pro</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>المنصة التفاعلية المتقدمة لإتقان مصطلحات سلاسل الإمداد والعمليات اللوجستية</div>", unsafe_allow_html=True)

# --- قسم التحكم والتصفية (صندوق أدوات البحث) ---
st.write("### 🔍 أدوات البحث والتصفية")
col1, col2 = st.columns([1, 1])

with col1:
    # 1. التصفية حسب القسم
    categories = ["📌 الكل"] + list(set([w['category'] for w in words]))
    selected_cat = st.selectbox("اختر القسم اللوجستي:", categories)

with col2:
    # 2. شريط البحث النصي
    search_query = st.text_input("ابحث عن مصطلح (E.g. Fleet, Stock):").strip().lower()

# تصفية المصطلحات بناءً على المدخلات
filtered_words = words
if selected_cat != "📌 الكل":
    filtered_words = [w for w in filtered_words if w['category'] == selected_cat]
if search_query:
    filtered_words = [w for w in filtered_words if search_query in w['en'].lower() or search_query in w['ar']]

# --- عرض النتائج واختيار المصطلح ---
st.write("---")
if filtered_words:
    word_options = [w['en'] for w in filtered_words]
    selected_word_en = st.selectbox("📄 المصطلحات المتوفرة بناءً على بحثك:", word_options)
    
    # جلب بيانات الكلمة المختارة
    word_data = next(w for w in filtered_words if w['en'] == selected_word_en)
    
    # --- تصميم بطاقة العرض الاحترافية ---
    st.write(f"### 📋 تفاصيل المصطلح | `{word_data['category']}`")
    
    # كرت المصطلح والنطق
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<p class='card-label'>المصطلح بالإنجليزية (Term)</p>", unsafe_allow_html=True)
        st.info(f"✨ **{word_data['en']}**")
    with c2:
        st.markdown("<p class='card-label'>النطق التقريبي (Pronunciation)</p>", unsafe_allow_html=True)
        st.warning(f"🗣️ **{word_data['pronunciation']}**")
        
    # كرت الترجمة العربية
    st.markdown("<p class='card-label'>الترجمة المعتمدة بالعربية</p>", unsafe_allow_html=True)
    st.success(f"🎯 **{word_data['ar']}**")
    
    # كرت الأمثلة السياقية المشتركة
    st.write("#### 📝 السياق العملي (Context Example):")
    st.markdown(f"""
    <div style="background-color: #1E1E1E; padding: 15px; border-radius: 8px; border-left: 5px solid #FF4B4B;">
        <p style="margin-bottom: 8px; color: #E0E0E0;">🇬🇧 <b>EN:</b> {word_data['ex_en']}</p>
        <p style="margin-bottom: 0; color: #E0E0E0; text-align: right;" dir="rtl">🇸🇦 <b>AR:</b> {word_data['ex_ar']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # النطق الصوتي التفاعلي
    st.write(" ")
    st.write("🗣️ **استمع إلى النطق الصوتي الصحيح:**")
    try:
        tts = gTTS(text=word_data['en'], lang='en')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        st.audio(fp, format='audio/mp3')
    except Exception as e:
        st.error("يتعذر تشغيل الصوت حالياً، تأكد من اتصالك بالإنترنت.")
else:
    st.warning("⚠️ لم يتم العثور على مصطلحات تطابق بحثك الحالي، جرب إدخال حروف أخرى.")
