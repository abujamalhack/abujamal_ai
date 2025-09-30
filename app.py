import streamlit as st
import random
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(
    page_title="ذكاء اصطناعي - أبو جمال عبدالناصر الشوكي",
    page_icon="🤖",
    layout="wide"
)

# تخصيص التصميم
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .arabic-text {
        font-size: 1.2rem;
        text-align: right;
        direction: rtl;
    }
    .creator-name {
        font-size: 2rem;
        color: #A23B72;
        text-align: center;
        font-weight: bold;
        margin-top: 1rem;
    }
    .sidebar-header {
        text-align: center;
        font-size: 2rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# الهوية الشخصية
st.markdown('<div class="main-header">🤖 ذكاء اصطناعي حصري</div>', unsafe_allow_html=True)
st.markdown('<div class="creator-name">من صناعة أبو جمال عبدالناصر الشوكي</div>', unsafe_allow_html=True)

st.markdown("---")

# ذاكرة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "مرحباً بك! أنا مساعدك الذكي من صناعة **أبو جمال عبدالناصر الشوكي** 🌟\nكيف يمكنني مساعدتك اليوم؟"
        }
    ]

# شريط جانبي للمعلومات
with st.sidebar:
    st.markdown('<div class="sidebar-header">🤖</div>', unsafe_allow_html=True)
    st.title("معلومات المطور")
    st.write("**الاسم:** أبو جمال عبدالناصر الشوكي")
    st.write("**التخصص:** تطوير الذكاء الاصطناعي")
    st.write("**الموقع:** تطوير ويب وتقني")
    st.markdown("---")
    st.write("🕒 تم الإنشاء في: {}".format(datetime.now().strftime("%Y-%m-%d")))
    
    # زر إعادة التعيين
    if st.button("🔄 إعادة تعيين المحادثة"):
        st.session_state.messages = [
            {
                "role": "assistant", 
                "content": "مرحباً بك من جديد! أنا مساعدك الذكي من صناعة **أبو جمال عبدالناصر الشوكي** 🌟"
            }
        ]
        st.rerun()

# عرض تاريخ المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f'<div class="arabic-text">{message["content"]}</div>', unsafe_allow_html=True)

# وظيفة توليد الردود
def generate_response(user_input):
    """دالة ذكية لتوليد الردود"""
    
    # ردود ذكية بناءً على المحتوى
    if any(word in user_input.lower() for word in ['اسمك', 'من انت', 'هويتك']):
        return "أنا **ذكاء اصطناعي** من صناعة وتطوير **أبو جمال عبدالناصر الشوكي** 🌟 أسعدني تواصلك معي!"
    
    elif any(word in user_input.lower() for word in ['شكرا', 'مرحبا', 'اهلا', 'السلام']):
        return "العفو يا غالي! 🌸 **أبو جمال عبدالناصر الشوكي** يهديك السلام ويشكرك على حسن تواصلك!"
    
    elif any(word in user_input.lower() for word in ['حب', 'حبيب', 'قلبي', 'فديت']):
        return "أحبك في الله يا قلبي! 🤲 **أبو جمال عبدالناصر الشوكي** يرسل لك تحياته الحارة!"
    
    elif any(word in user_input.lower() for word in ['صنعت', 'برمجة', 'تطوير']):
        return "تم صناعي وتطويري بكامل الحب بواسطة **أبو جمال عبدالناصر الشوكي** 🚀 وهو فخور بتقديم هذا التطبيق لك!"
    
    elif any(word in user_input.lower() for word in ['كيف حالك', 'اخبارك', 'شونك']):
        return "الحمدلله بخير وعافية! 🌟 شكراً لسؤالك اللطيف. **أبو جمال عبدالناصر الشوكي** يتمنى لك يومًا سعيدًا!"
    
    # ردود عامة
    responses_arabic = [
        f"أهلاً بك! أنا مساعدك الذكي من صناعة **أبو جمال عبدالناصر الشوكي** 🌟\nسؤالك: {user_input}",
        f"ما شاء الله! سؤال جميل من تطوير **أبو جمال عبدالناصر الشوكي** 💫\nجوابي: هذا موضوع مهم يتعلق بـ {user_input}",
        f"الحمد لله! عندي إجابة رائعة لك من صناعة **أبو جمال عبدالناصر الشوكي** 🌸\nتعال نناقش: {user_input}",
        f"يا هلا وسهلا! **أبو جمال عبدالناصر الشوكي** صنعني لأخدمك 🚀\nردي على سؤالك: {user_input}",
        f"تبارك الرحمن! أسأل الله أن يوفق **أبو جمال عبدالناصر الشوكي** 🤲\nجوابي: {user_input}",
        f"يسعد مساك! من تطوير **أبو جمال عبدالناصر الشوكي** جاءت هذه الإجابة 🌈\nتعال نرى: {user_input}",
        f"الله يبارك فيك! **أبو جمال عبدالناصر الشوكي** يقدم لك هذه الإجابة 🎯\nهاهي: {user_input}"
    ]
    
    return random.choice(responses_arabic)

# مدخلات المحادثة
if prompt := st.chat_input("اكتب رسالتك هنا... 🌸"):
    # إضافة رسالة المستخدم
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f'<div class="arabic-text">{prompt}</div>', unsafe_allow_html=True)
    
    # توليد الرد
    with st.chat_message("assistant"):
        with st.spinner('جاري التفكير... 🌟'):
            response = generate_response(prompt)
            st.markdown(f'<div class="arabic-text">{response}</div>', unsafe_allow_html=True)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

# قسم إضافي للميزات
st.markdown("---")
st.subheader("🎯 مميزات التطبيق")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **🤖 الذكاء الاصطناعي**
    - محادثة ذكية بالعربية
    - ردود مخصصة شخصية
    - ذاكرة محادثة متقدمة
    - تفاعل طبيعي وسلس
    """)

with col2:
    st.markdown("""
    **🎨 التصميم والواجهة**
    - واجهة عربية أنيقة
    - تصميم عصري وجذاب
    - ألوان مخصصة فريدة
    - دعم كامل للعربية
    """)

with col3:
    st.markdown("""
    **⚙️ التقنيات**
    - Python + Streamlit
    - معالجة اللغة الطبيعية
    - تصميم متجاوب
    - نشر سحابي متقدم
    """)

# معلومات التقنية
st.markdown("---")
st.subheader("📞 معلومات التقنية")

tech_col1, tech_col2 = st.columns(2)

with tech_col1:
    st.markdown("""
    **👨‍💻 المطور:** أبو جمال عبدالناصر الشوكي
    **🏢 نوع المشروع:** تطبيق ويب ذكي
    **🌐 السحابة:** Streamlit Cloud
    **📅 تاريخ الإصدار:** 2024
    """)

with tech_col2:
    st.markdown("""
    **🐍 اللغة:** Python
    **🛠 الإطار:** Streamlit
    **📊 الذكاء:** معالجة اللغة
    **🔗 الترخيص:** مفتوح المصدر
    """)

# تذييل الصفحة
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #666; padding: 2rem;">'
    '© 2024 جميع الحقوق محفوظة - تطوير وتصنيع أبو جمال عبدالناصر الشوكي 🌸<br>'
    'صنع بكل حب وإتقان في العالم العربي'
    '</div>', 
    unsafe_allow_html=True
)
