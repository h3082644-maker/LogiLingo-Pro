import streamlit as st
import random
from data import words
from gtts import gTTS
import io

# 1. إعدادات الصفحة المتقدمة جداً
st.set_page_config(
    page_title="LogiLingo Pro Premium",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. تصميم CSS مخصص للبطاقات والألوان وحواف العناصر التفاعلية
st.markdown("""
<style>
/* العناوين الأساسية */
.main-title { font-size: 3rem; font-weight: 800; text-align: center; color: #FF4B4B; margin-bottom: 0px; }
.sub-title { text-align: center; color: #AAAAAA; font-size: 1.2rem; margin-bottom: 30px; }

/* ستايل لوحة الإحصائيات العلوية */
.metric-card { background-color: #1A1C23; padding: 15px; border-radius: 12px; border: 1px solid #2D313E; text-align: center; }
.metric-val { font-size: 1.8rem; font-weight: bold; color: #FF4B4B; }
.metric-lbl { font-size: 0.9rem; color: #888888; }

/* بطاقة عرض تفاصيل المصطلح */
.term-box { background: linear-gradient(135deg, #1E2028 0%, #12131A 100%); padding: 25px; border-radius: 16px; border: 1px solid #3E4255; box-shadow: 0 8px 32px 0 rgba(0,0,0,0.3); }
.label-accent { color: #888888; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; font-weight: bold; }
.text-en { font-size: 2.2rem; font-weight: bold; color: #FFFFFF; margin-bottom: 15px; }
.text-ar { font-size: 1.8rem; font-weight: bold; color: #10B981; margin-bottom: 15px; text-align: right; }
.text-pron { font-size: 1.3rem; color: #F59E0B; margin-bottom: 20px; }

/* صندوق الأمثلة السياقية */
.context-box { background-color: #16171E; padding: 18px; border-radius: 10px; border-left: 4px solid #FF4B4B; margin-top: 15px; }
.ex-item { font-size: 1.05rem; color: #E2E8F0; margin-bottom: 8px; }
</style>
""", unsafe_allow_html=True)

# 3. القائمة الجانبية للتصفية والتحكم (Sidebar)
with st.sidebar:
    st.markdown("### 🛠️ لوحة التحكم والتصفية")
    st.write("استخدم الأدوات بالأسفل للوصول السريع للمصطلحات:")
    
    # فلتر التصنيفات اللوجستية
    categories_list = ["📌 استعراض كافة القطاعات"] + list(sorted(set([w['category'] for w in words])))
    selected_cat = st.selectbox("🗂️ اختر القطاع اللوجستي:", categories_list)
    
    # شريط البحث النصي الذكي
    search_query = st.text_input("🔍 ابحث عن مصطلح محدد (عربي/إنجليزي):").strip().lower()
    
    st.write("---")
    st.markdown("💡 **نصيحة مهنية:**\nإتقان هذه المصطلحات يجهزك للمقابلات الشخصية في كبرى شركات سلاسل الإمداد العالمية.")

# 4. واجهة التطبيق الرئيسية (Main Content)
st.markdown("<div class='main-title'>📦 LogiLingo Pro v3</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>المنصة المهنية الكبرى لتعلم وإتقان لغة سلاسل الإمداد والعمليات اللوجستية</div>", unsafe_allow_html=True)

# 5. لوحة الإحصائيات الذكية (Dashboard Ribbons)
c_metric1, c_metric2, c_metric3 = st.columns(3)
with c_metric1:
    st.markdown(f"<div class='metric-card'><div class='metric-val'>{len(words)}</div><div class='metric-lbl'>إجمالي المصطلحات الحالية</div></div>", unsafe_allow_html=True)
with c_metric2:
    st.markdown(f"<div class='metric-card'><div class='metric-val'>{len(categories_list)-1}</div><div class='metric-lbl'>القطاعات والعمليات المغطاة</div></div>", unsafe_allow_html=True)
with c_metric3:
    st.markdown("<div class='metric-card'><div class='metric-val'>100%</div><div class='metric-lbl'>دقة النطق والترجمة المعتمدة</div></div>", unsafe_allow_html=True)

st.write(" ")
st.write(" ")

# 6. تصفية ومعالجة البيانات بناءً على مدخلات المستخدم
filtered_words = words
if selected_cat != "📌 استعراض كافة القطاعات":
    filtered_words = [w for w in filtered_words if w['category'] == selected_cat]
if search_query:
    filtered_words = [w for w in filtered_words if search_query in w['en'].lower() or search_query in w['ar']]

# 7. آلية اختيار وعرض المصطلحات اللوجستية
if filtered_words:
    col_list, col_details = st.columns([1, 2])
    
    with col_list:
        st.write("### 📄 المصطلحات المتاحة")
        word_options = [w['en'] for w in filtered_words]
        
        # صندوق الاختيار الرئيسي للمصطلحات المفلترة
        selected_word_en = st.radio("اختر المصطلح لعرض تفاصيله ونطقه:", word_options, index=0)
        word_data = next(w for w in filtered_words if w['en'] == selected_word_en)
        
    with col_details:
        st.write("### 📋 لوحة تفاصيل المصطلح الاحترافية")
        
        # بناء حاوية التفاصيل الفاخرة عبر HTML و CSS المخصص (تمت محاذاته بالكامل لليسار ليعمل التصميم فوراً)
        st.markdown(f"""
<div class="term-box">
<div class="label-accent">القطاع اللوجستي المندرج تحته: {word_data['category']}</div>
<div style="height: 1px; background-color: #2D313E; margin-bottom: 15px;"></div>
<div class="label-accent">المصطلح بالإنجليزية (Term)</div>
<div class="text-en">✨ {word_data['en']}</div>
<div class="label-accent">الترجمة المهنية المعتمدة باللغة العربية</div>
<div class="text-ar" dir="rtl">🎯 {word_data['ar']}</div>
<div class="label-accent">النطق التقريبي باللغة العربية</div>
<div class="text-pron">🗣️ {word_data['pronunciation']}</div>
<div class="label-accent">💡 سياق الاستخدام العملي في الشركات (Context Examples)</div>
<div class="context-box">
<div class="ex-item">🇬🇧 <b>EN:</b> {word_data['ex_en']}</div>
<div class="ex-item" style="text-align: right;" dir="rtl">🇸🇦 <b>AR:</b> {word_data['ex_ar']}</div>
</div>
</div>
""", unsafe_allow_html=True)
        
        # 8. توليد النطق الصوتي التفاعلي الفوري (Audio Component)
        st.write(" ")
        st.markdown("🔊 **استمع الآن إلى النطق الصوتي البشري الصحيح:**")
        try:
            tts = gTTS(text=word_data['en'], lang='en')
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            st.audio(fp, format='audio/mp3')
        except Exception as e:
            st.error("يتعذر تشغيل الملف الصوتي حالياً، يرجى التحقق من اتصالك بالإنترنت.")
else:
    st.warning("⚠️ لم يتم العثور على أي مصطلحات تطابق بحثك الحالي، يرجى تغيير الكلمات الدليلية أو مسح شريط البحث.")
