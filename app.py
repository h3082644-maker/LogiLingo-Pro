elif choice == "📚 التعلم":
    st.title("📚 مستوى: عمليات الشحن")
    
    # تنسيق الـ CSS للبطاقة المتحركة
    st.markdown("""
    <style>
    .card-container {
        perspective: 1000px;
        width: 100%;
        max-width: 400px;
        margin: auto;
    }
    .card {
        background: #FFFFFF;
        border: 2px solid #E5E7EB;
        border-radius: 24px;
        padding: 40px 20px;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    .card:hover { transform: translateY(-5px); }
    .word-en { font-size: 2.5rem; font-weight: 800; color: #1F2937; margin-bottom: 10px; }
    .word-ar { font-size: 1.2rem; color: #6B7280; }
    </style>
    """, unsafe_allow_html=True)

    # عرض البطاقة
    st.markdown("""
    <div class="card-container">
        <div class="card">
            <div class="word-en">Shipment</div>
            <div class="word-ar">الشحنة</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("") # فراغ
    # أزرار التفاعل
    col1, col2 = st.columns(2)
    if col1.button("❌ لم أعرف"):
        st.session_state.hearts -= 1
        st.rerun()
    if col2.button("✅ عرفتها!"):

        # 1. قائمة المصطلحات اللوجستية الخاصة بك
logistics_words = [
    {"en": "Shipment", "ar": "شحنة"},
    {"en": "Warehouse", "ar": "مستودع"},
    {"en": "Inventory", "ar": "مخزون"},
    {"en": "Hub", "ar": "مركز توزيع"},
    {"en": "Carrier", "ar": "ناقل"},
    {"en": "Manifest", "ar": "بيان الشحنة"},
    {"en": "Reverse Shipment", "ar": "شحنة مرتجعة"},
    {"en": "Last Mile", "ar": "الميل الأخير"},
    {"en": "POD", "ar": "إثبات التسليم"},
    {"en": "COD", "ar": "الدفع عند الاستلام"},
    {"en": "Fulfillment", "ar": "تجهيز الطلبات"}
]

# 2. إدارة الحالة للتنقل
if 'current_word_idx' not in st.session_state:
    st.session_state.current_word_idx = 0

# 3. قسم التعلم المطور
elif choice == "📚 التعلم":
    st.title("📚 مستوى: عمليات الشحن")
    
    # التقدم (Progress Bar)
    progress = (st.session_state.current_word_idx + 1) / len(logistics_words)
    st.progress(progress)
    
    word_data = logistics_words[st.session_state.current_word_idx]

    # تصميم البطاقة التفاعلية
    st.markdown(f"""
    <div class="card-container">
        <div class="card">
            <div class="word-en">{word_data['en']}</div>
            <div class="word-ar">{word_data['ar']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # أزرار التفاعل مع منطق التنقل
    col1, col2 = st.columns(2)
    
    if col1.button("❌ لم أعرف"):
        st.session_state.hearts -= 1
        st.error("حاول التركيز، القلوب تنقص!")
        st.rerun()
        
    if col2.button("✅ عرفتها!"):
        st.session_state.xp += 10
        # الانتقال للكلمة التالية
        st.session_state.current_word_idx = (st.session_state.current_word_idx + 1) % len(logistics_words)
        st.success("+10 XP - أحسنت!")
        st.rerun()
        st.session_state.xp += 10
        st.success("+10 XP")
        elif choice == "📧 وضع العمل":
    st.title("📧 محاكي إيميلات العمل")
    
    # اختيار إيميل عشوائي لليوم
    email = random.choice(work_emails)
    
    st.info("💡 مهمة اليوم: اقرأ الإيميل التالي وحاول فهم معناه:")
    st.markdown(f"**{email['body']}**")
    
    if st.button("كشف المعنى"):
        st.success(f"الترجمة: {email['ar_meaning']}")
        
        st.write("---")
        st.write("✍️ الآن، حاول كتابة الإيميل بنفسك (اختبار الذاكرة):")
        user_text = st.text_area("اكتب الإيميل هنا:")
        
        if st.button("تحقق من الكتابة"):
            if user_text.strip() == email['body']:
                st.balloons()
                st.success("ممتاز! تطابق تام. +20 XP")
                st.session_state.xp += 20
            else:
                st.warning("هناك اختلاف بسيط، راجع الإملاء!")
