import streamlit as st
import random
from datetime import datetime
import requests

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
    st.image("🤖", width=100)
    st.title("معلومات المطور")
    st.write("**الاسم:** أبو جمال عبدالناصر الشوكي")
    st.write("**التخصص:** تطوير الذكاء الاصطناعي")
    st.write("**الموقع:** تطوير ويب وتقني")
    st.markdown("---")
    st.write("🕒 تم الإنشاء في: {}".format(datetime.now().strftime("%Y-%m-%d")))

# عرض تاريخ المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(f'<div class="arabic-text">{message["content"]}</div>', unsafe_allow_html=True)

# وظيفة توليد الردود
def generate_response(user_input):
    """دالة ذكية لتوليد الردود"""
    
    responses_arabic = [
        f"أهلاً بك! أنا مساعدك الذكي من صناعة **أبو جمال عبدالناصر الشوكي** 🌟\nسؤالك: {user_input}",
        f"ما شاء الله! سؤال جميل من صناعة **أبو جمال عبدالناصر الشوكي** 💫\nجوابي: هذا موضوع مهم يتعلق بـ {user_input}",
        f"الحمد لله! عندي إجابة رائعة لك من تطوير **أبو جمال عبدالناصر الشوكي** 🌸\nتعال نناقش: {user_input}",
        f"يا هلا وسهلا! **أبو جمال عبدالناصر الشوكي** صنعني لأخدمك 🚀\nردي على سؤالك: {user_input}",
        f"تبارك الرحمن! أسأل الله أن يوفق **أبو جمال عبدالناصر الشوكي** 🤲\nجوابي: {user_input}"
    ]
    
    # إضافة ردود ذكية بناءً على المحتوى
    if any(word in user_input.lower() for word in ['اسمك', 'من انت', 'هويتك']):
        return "أنا **ذكاء اصطناعي** من صناعة وتطوير **أبو جمال عبدالناصر الشوكي** 🌟 أسعدني تواصلك معي!"
    
    elif any(word in user_input.lower() for word in ['شكرا', 'مرحبا', 'اهلا']):
        return "العفو يا غالي! 🌸 **أبو جمال عبدالناصر الشوكي** يهديك السلام ويشكرك على حسن تواصلك!"
    
    elif any(word in user_input.lower() for word in ['حب', 'حبيب', 'قلبي']):
        return "أحبك في الله يا قلبي! 🤲 **أبو جمال عبدالناصر الشوكي** يرسل لك تحياته الحارة!"
    
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
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🎯 المميزات")
    st.write("• ذكاء اصطناعي متطور")
    st.write("• واجهة عربية أنيقة")
    st.write("• تصميم متجاوب")

with col2:
    st.subheader("🚀 التقنيات")
    st.write("• Python + Streamlit")
    st.write("• معالجة اللغة الطبيعية")
    st.write("• تصميم تفاعلي")

with col3:
    st.subheader("📞 التواصل")
    st.write("المطور: أبو جمال عبدالناصر الشوكي")
    st.write("نوع المشروع: ذكاء اصطناعي")
    st.write("الترخيص: مفتوح المصدر")

# تذييل الصفحة
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #666;">'
    '© 2024 جميع الحقوق محفوظة - تطوير أبو جمال عبدالناصر الشوكي 🌸'
    '</div>', 
    unsafe_allow_html=True
  )
