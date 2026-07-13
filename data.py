words = [
    # --- الشحن والنقل ---
    {"en": "Shipment", "ar": "الشحنة", "pronunciation": "شِيبْمِينْت", "ex_en": "The shipment will arrive tomorrow morning.", "ex_ar": "ستصل الشحنة صباح الغد.", "category": "🚛 الشحن والنقل"},
    {"en": "Cargo", "ar": "البضائع / الحمولة", "pronunciation": "كَارْجُو", "ex_en": "The ship is carrying heavy cargo.", "ex_ar": "السفينة تحمل بضائع ثقيلة.", "category": "🚛 الشحن والنقل"},
    {"en": "Freight Forwarder", "ar": "وكيل الشحن", "pronunciation": "فْرِيت فَوْرْوَرْدَر", "ex_en": "Our freight forwarder handled the sea freight smoothly.", "ex_ar": "تولى وكيل الشحن الخاص بنا عملية الشحن البحري بسلاسة.", "category": "🚛 الشحن والنقل"},
    {"en": "Bill of Lading", "ar": "بوليصة الشحن", "pronunciation": "بِلْ أُوف لَيْدِينْج", "ex_en": "The Bill of Lading is a mandatory document for export.", "ex_ar": "بوليصة الشحن هي وثيقة إلزامية للتصدير.", "category": "🚛 الشحن والنقل"},
    {"en": "Waybill", "ar": "بوليصة نقل", "pronunciation": "وَيْبِل", "ex_en": "Make sure the air waybill is attached to the package.", "ex_ar": "تأكد من إرفاق بوليصة النقل الجوي بالطرد.", "category": "🚛 الشحن والنقل"},
    {"en": "Fleet Management", "ar": "إدارة الأسطول", "pronunciation": "فْلِيت مَانِيجْمِينْت", "ex_en": "Effective fleet management reduces fuel costs.", "ex_ar": "إدارة الأسطول الفعّالة تقلل تكاليف الوقود.", "category": "🚛 الشحن والنقل"},
    {"en": "Cross-docking", "ar": "عبور رصيف الشحن / الترانزيت المباشر", "pronunciation": "كْرُوس دُوكِينْج", "ex_en": "Cross-docking eliminates the need for long-term storage.", "ex_ar": "العبور المباشر يلغي الحاجة للتخزين طويل الأمد.", "category": "🚛 الشحن والنقل"},
    
    # --- المستودعات والتنفيذ ---
    {"en": "Warehouse", "ar": "المستودع / المخزن", "pronunciation": "وِيرْ هَاوْس", "ex_en": "We store all spare parts in the main warehouse.", "ex_ar": "نحن نخزن جميع قطع الغيار في المستودع الرئيسي.", "category": "🏢 المستودعات والتنفيذ"},
    {"en": "Inventory", "ar": "المخزون", "pronunciation": "إِنْفِنْتُورِي", "ex_en": "We need to do a full inventory count this weekend.", "ex_ar": "نحتاج إلى إجراء جرد كامل للمخزون نهاية هذا الأسبوع.", "category": "🏢 المستودعات والتنفيذ"},
    {"en": "Pallet", "ar": "طبلية / منصة نقالة", "pronunciation": "بَالِيت", "ex_en": "Please load these boxes onto the wooden pallet.", "ex_ar": "الرجاء تحميل هذه الصناديق على الطبلية الخشبية.", "category": "🏢 المستودعات والتنفيذ"},
    {"en": "Forklift", "ar": "رافعة شوكية", "pronunciation": "فُورْك لِفْت", "ex_en": "The worker is driving the forklift in the warehouse.", "ex_ar": "العامل يقود الرافعة الشوكية في المستودع.", "category": "🏢 المستودعات والتنفيذ"},
    {"en": "Out of Stock", "ar": "نفد من المخزون", "pronunciation": "آوْت أُوف سْتُوك", "ex_en": "I am sorry, this item is currently out of stock.", "ex_ar": "أنا آسف، هذا العنصر غير متوفر في المخزون حالياً.", "category": "🏢 المستودعات والتنفيذ"},
    {"en": "Fulfillment Center", "ar": "مركز تنفيذ الطلبات", "pronunciation": "فُولْفِيلْمِينْت سِينْتَر", "ex_en": "The fulfillment center processes thousands of orders daily.", "ex_ar": "يقوم مركز تنفيذ الطلبات بمعالجة آلاف الطلبات يومياً.", "category": "🏢 المستودعات والتنفيذ"},
    {"en": "Safety Stock", "ar": "مخزون الأمان", "pronunciation": "سَيْفْتِي سْتُوك", "ex_en": "We maintain safety stock to avoid shortages.", "ex_ar": "نحتفظ بمخزون أمان لتفادي أي نقص.", "category": "🏢 المستودعات والتنفيذ"},

    # --- التتبع وخدمة العملاء ---
    {"en": "Tracking Number", "ar": "رقم التتبع", "pronunciation": "تْرَاكِينْج نَمْبَر", "ex_en": "Please send me the tracking number for my order.", "ex_ar": "من فضلك أرسل لي رقم التتبع الخاص بطلبي.", "category": "📍 التتبع وخدمة العملاء"},
    {"en": "Consignee", "ar": "المستلم / المرسل إليه", "pronunciation": "كَانْسَايْ نِي", "ex_en": "The consignee must sign the delivery receipt.", "ex_ar": "يجب على المستلم التوقيع على إيصال الاستلام.", "category": "📍 التتبع وخدمة العملاء"},
    {"en": "Courier", "ar": "ساعي البريد / شركة التوصيل", "pronunciation": "كُورِيَر", "ex_en": "The courier will deliver the documents today.", "ex_ar": "شركة التوصيل ستقوم بتسليم المستندات اليوم.", "category": "📍 التتبع وخدمة العملاء"},
    {"en": "Last Mile Delivery", "ar": "توصيل الميل الأخير", "pronunciation": "لَاسْت مَايْل دِيلِيفِري", "ex_en": "Last mile delivery is the most critical part of logistics.", "ex_ar": "توصيل الميل الأخير هو الجزء الأكثر أهمية في اللوجستيات.", "category": "📍 التتبع وخدمة العملاء"},
    {"en": "Delivery Failure", "ar": "فشل التوصيل", "pronunciation": "دِيلِيفِري فَيْليِر", "ex_en": "The delivery failure was due to an incorrect address.", "ex_ar": "كان فشل التوصيل بسبب عنوان غير صحيح.", "category": "📍 التتبع وخدمة العملاء"},
    {"en": "Address Update", "ar": "تحديث العنوان", "pronunciation": "أَدْرِيس أَبْدَيْت", "ex_en": "Please request an address update from the customer.", "ex_ar": "الرجاء طلب تحديث العنوان من العميل.", "category": "📍 التتبع وخدمة العملاء"},

    # --- سلاسل الإمداد والتخطيط ---
    {"en": "Supply Chain", "ar": "سلسلة الإمداد", "pronunciation": "سَبْلَايْ تَشِين", "ex_en": "A strong supply chain is key to business success.", "ex_ar": "سلسلة الإمداد القوية هي مفتاح نجاح الأعمال.", "category": "⚙️ التخطيط وسلاسل الإمداد"},
    {"en": "Lead Time", "ar": "فترة التوريد / وقت التنفيذ", "pronunciation": "لِيدْ تَايْم", "ex_en": "The lead time for this product is 3 weeks.", "ex_ar": "فترة التوريد لهذا المنتج هي 3 أسابيع.", "category": "⚙️ التخطيط وسلاسل الإمداد"},
    {"en": "Procurement", "ar": "المشتريات / الاستخلاص", "pronunciation": "بْرُوكْيُورْمِينْت", "ex_en": "The procurement team is looking for new suppliers.", "ex_ar": "فريق المشتريات يبحث عن موردين جدد.", "category": "⚙️ التخطيط وسلاسل الإمداد"},
    {"en": "Customs Clearance", "ar": "التخليص الجمركي", "pronunciation": "كَاسْتَمْز كْلِيرَانْس", "ex_en": "Customs clearance usually takes two business days.", "ex_ar": "التخليص الجمركي يستغرق عادةً يومي عمل.", "category": "⚙️ التخطيط وسلاسل الإمداد"},
    {"en": "3PL (Third-Party Logistics)", "ar": "اللوجستيات الطرف الثالث", "pronunciation": "ثْرِي بِي إل", "ex_en": "We outsourced our warehousing to a 3PL company.", "ex_ar": "قمنا بإسناد التخزين لدينا إلى شركة لوجستيات طرف ثالث.", "category": "⚙️ التخطيط وسلاسل الإمداد"},
    {"en": "Just-In-Time (JIT)", "ar": "الإنتاج في الوقت المحدد تماماً", "pronunciation": "جَاسْت إِن تَايْم", "ex_en": "JIT strategy helps reduce inventory holding costs.", "ex_ar": "تساعد استراتيجية JIT في تقليل تكاليف الاحتفاظ بالمخزون.", "category": "⚙️ التخطيط وسلاسل الإمداد"}
]
