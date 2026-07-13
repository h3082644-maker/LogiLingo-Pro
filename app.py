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
        st.session_state.xp += 10
        st.success("+10 XP")
