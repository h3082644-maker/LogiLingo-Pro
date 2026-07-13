import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="LogiLingo Pro", layout="wide", page_icon="📦")

# تهيئة البيانات الأساسية في الجلسة (لإدارة اللعبة)
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'streak' not in st.session_state: st.session_state.streak = 5
if 'hearts' not in st.session_state: st.session_state.hearts = 5

# --- القائمة الجانبية الاحترافية ---
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/logistics.png", width=80)
    st.title("LogiLingo Pro")
    
    menu = ["🏠 الرئيسية", "📚 التعلم", "📝 الاختبار", "🎧 الاستماع", "🏆 الإنجازات", "📧 وضع العمل", "🤖 AI Mode"]
    choice = st.radio("القائمة:", menu)
    
    st.markdown("---")
    st.write(f"❤️ القلوب: {st.session_state.hearts}/5")
    st.write(f"🔥 الستريك: {st.session_state.streak} يوم")

# --- عرض المحتوى بناءً على الاختيار ---
if choice == "🏠 الرئيسية":
    st.title("مرحباً حسين! 👋")
    st.subheader("جاهز لمهمة اليوم في سلاسل الإمداد؟")
    
    # شريط التقدم العام
    st.write("تقدمك العام:")
    st.progress(0.75)
    
    # بطاقات سريعة
    c1, c2, c3 = st.columns(3)
    c1.metric("XP المكتسبة", st.session_state.xp)
    c2.metric("التصنيف", "مستوى 12")
    c3.metric("الكلمات المتقنة", "540")

elif choice == "📚 التعلم":
    st.title("📚 قسم التعلم")
    # هنا سيتم لاحقاً وضع البطاقات المتحركة
    st.info("اختر درساً للبدء...")

elif choice == "🤖 AI Mode":
    st.title("🤖 المساعد اللوجستي الذكي")
    user_input = st.text_input("اكتب ما تريد صياغته (مثلاً: اطلب تحديث العنوان):")
    if user_input:
        st.write("جاري الكتابة بالإنجليزية الاحترافية...")
        # سيتم ربط هذا بـ AI لاحقاً

# ملاحظة: يمكنك إضافة باقي الصفحات هنا بنفس المنطق
