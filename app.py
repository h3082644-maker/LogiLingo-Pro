import streamlit as st
from data import words  # نستدعي الكلمات فقط
from gtts import gTTS
import io

# وضعنا الإيميلات هنا مباشرة لتجنب خطأ الاستدعاء
emails = [
    {
        "title": "تأخير الشحنة (Shipment Delay)",
        "en": "Dear Client,\n\nWe regret to inform you that your shipment is delayed due to bad weather.\n\nBest regards,\nLogistics Team",
        "ar": "عزيزي العميل،\n\nنأسف لإبلاغك بأن شحنتك قد تأخرت بسبب سوء الأحوال الجوية.\n\nأطيب التحيات،\nفريق اللوجستيات"
    },
    {
        "title": "إشعار وصول (Arrival Notice)",
        "en": "Dear Customer,\n\nYour cargo has arrived at the destination port and is ready for pickup.\n\nRegards,\nOperations Dept",
        "ar": "عزيزي العميل،\n\nلقد وصلت بضاعتك إلى ميناء الوجهة وهي جاهزة للاستلام.\n\nتحياتنا،\nقسم العمليات"
    }
]

# إعداد الصفحة
st.set_page_config(page_title="LogiLingo Pro", page_icon="📦", layout="centered")

if "index" not in st.session_state:
    st.session_state.index = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

# دالة توليد الصوت
def get_audio_bytes(text):
    tts = gTTS(text=text, lang='en', tld='com')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()

st.title("🦉 LogiLingo Pro")
st.caption("مسارك الاحترافي لتعلم الإنجليزية اللوجستية")

# إنشاء تبويبات (Tabs)
tab1, tab2 = st.tabs(["📚 البطاقات التعليمية", "📧 تدريب الإيميلات"])

# ================= التبويب الأول: الكلمات والجمل =================
with tab1:
    st.progress((st.session_state.index + 1) / len(words))
    
    current_word = words[st.session_state.index]
    
    st.markdown(f"<h1 style='text-align: center; color: #1E88E5;'>{current_word['en']}</h1>", unsafe_allow_html=True)
    
    # مشغل الصوت للكلمة
    col_audio, col_blank = st.columns([1, 3])
    with col_audio:
        try:
            st.audio(get_audio_bytes(current_word['en']), format="audio/mp3")
        except:
            st.caption("🔊 تعذر تحميل الصوت")

    st.divider()

    if not st.session_state.show_answer:
        if st.button("👁️ إظهار الترجمة والجملة", use_container_width=True, type="primary"):
            st.session_state.show_answer = True
            st.rerun()
    else:
        st.markdown(f"<h2 style='text-align: center; color: #4CAF50;'>🇸🇦 {current_word['ar']}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: #FF9800;'>🗣️ النطق: <b>{current_word['pronunciation']}</b></p>", unsafe_allow_html=True)
        
        # إضافة الجملة
        st.info(f"**Example:** {current_word.get('ex_en', '')}")
        st.success(f"**الترجمة:** {current_word.get('ex_ar', '')}")
        
        # تشغيل صوت الجملة
        try:
            if 'ex_en' in current_word:
                st.audio(get_audio_bytes(current_word['ex_en']), format="audio/mp3")
        except:
            pass
        
        if st.button("🙈 إخفاء الترجمة", use_container_width=True):
            st.session_state.show_answer = False
            st.rerun()

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅ السابق", use_container_width=True):
            if st.session_state.index > 0:
                st.session_state.index -= 1
                st.session_state.show_answer = False
                st.rerun()
    with col2:
        if st.button("التالي ➡", use_container_width=True):
            if st.session_state.index < len(words) - 1:
                st.session_state.index += 1
                st.session_state.show_answer = False
                st.rerun()

# ================= التبويب الثاني: الإيميلات =================
with tab2:
    st.header("تدريب المراسلات اللوجستية")
    st.write("اقرأ الإيميل باللغة الإنجليزية، وحاول فهمه قبل كشف الترجمة.")
    
    for email in emails:
        st.subheader(f"📌 {email['title']}")
        st.info(email['en']) # عرض الإيميل بالإنجليزي
        
        # زر قابل للطي لعرض الترجمة
        with st.expander("إظهار الترجمة العربية"):
            st.success(email['ar'])
        
        st.divider()