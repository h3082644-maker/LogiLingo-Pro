import streamlit as st
from data import words
from gtts import gTTS
import io

# 1. إعدادات الصفحة العامة
st.set_page_config(
    page_title="LogiLingo Pro",
    page_icon="📦",
    layout="centered"
)

# 2. تصميم الواجهة الرئيسية
st.title("📦 LogiLingo Pro")
st.markdown("#### تطبيقك الذكي لتعلم مصطلحات اللوجستيات وسلاسل الإمداد")
st.write("---")

# 3. قائمة اختيار الكلمات
word_options = [w['en'] for w in words]
selected_word_en = st.selectbox("🗂️ اختر مصطلحاً لتعلمه:", word_options)

# 4. جلب بيانات الكلمة المختارة
word_data = next(w for w in words if w['en'] == selected_word_en)

# 5. عرض الكلمة والترجمة في بطاقات ملونة وأنيقة
st.info(f"**المصطلح بالإنجليزية (Term):** {word_data['en']}")
st.success(f"**الترجمة بالعربية:** {word_data['ar']}")
st.warning(f"**النطق التقريبي:** {word_data['pronunciation']}")

# 6. عرض الأمثلة السياقية
st.write("### 📝 أمثلة سياقية (Context Examples):")
st.write(f"💡 **English:** {word_data['ex_en']}")
st.write(f"💡 **العربية:** {word_data['ex_ar']}")

# 7. تشغيل النطق الصوتي باستخدام مكتبة gTTS
st.write("---")
st.write("### 🔊 استمع إلى النطق الصحيح:")

try:
    tts = gTTS(text=word_data['en'], lang='en')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    st.audio(fp, format='audio/mp3')
except Exception as e:
    st.error("حدث خطأ أثناء تحميل الصوت، يرجى التحقق من اتصال الإنترنت.")
