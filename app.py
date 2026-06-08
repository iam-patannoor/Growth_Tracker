import streamlit as st
import datetime

# Page Configuration
st.set_page_config(page_title="My Mind Detox & Growth Tracker", page_icon="🌙", layout="centered")

# Custom Styling for a Calm, Elegant Look
st.markdown("""
    <style>
    .main { background-color: #F8F9FA; }
    h1 { color: #2B3E50; font-family: 'Segoe UI', sans-serif; text-align: center; }
    h3 { color: #3A506B; }
    .stButton>button { background-color: #2B3E50; color: white; border-radius: 8px; width: 100%; }
    .success-box { background-color: #D4EDDA; color: #155724; padding: 15px; border-radius: 8px; text-align: center; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Title & Spiritual Reminder
st.title("🌙 MY DAILY MIND DETOX & GROWTH")
st.markdown("<p style='text-align: center; font-style: italic; color: #555;'>\"Indeed, Allah will not change the condition of a people until they change what is in themselves.\" (Quran 13:11)</p>", unsafe_allow_html=True)
st.markdown("---")

# Date Selection
today = datetime.date.today().strftime("%A, %B %d, %Y")
st.subheader(f"📅 Today's Entry: {today}")

# Layout Pillars using Tabs
tab1, tab2, tab3 = st.tabs(["放置🕌 Spiritual Core", "💻 Growth & Independence", "🛡️ Mind Detox Shield"])

with tab1:
    st.markdown("### Protect Your Foundation")
    fajr = st.checkbox("🌅 Fajr Prayer")
    dhuhr = st.checkbox("☀️ Dhuhr Prayer")
    asr = st.checkbox("🌤️ Asr Prayer")
    maghrib = st.checkbox("🌆 Maghrib Prayer")
    isha = st.checkbox("🌃 Isha Prayer")
    tahajjud = st.checkbox("✨ Tahajjud / Voluntary Sujood")
    islamic_time = st.number_input("📚 Islamic Class / Reading (Minutes)", min_value=0, step=5, key="islamic")

with tab2:
    st.markdown("### Build Your Future & Independence")
    tech_time = st.number_input("🚀 Technical Upskilling & Study (Minutes)", min_value=0, step=5, key="tech")
    workout_time = st.number_input("🏃‍♂️ Physical Workout / Brisk Walk (Minutes)", min_value=0, step=5, key="workout")

with tab3:
    st.markdown("### Intercept the Habit Loop")
    urge_overcome = st.radio(
        "🔥 Did you face a trigger or urge today and successfully outlast/overcome it?",
        ["No Urges Faced Today", "Yes - Faced an urge and STAYED STRONG! 💪", "I struggled today, but tomorrow is a new day."]
    )
    notes = st.text_area("📝 Daily Focus, Trigger Patterns, or Notes of Gratitude to Allah:")

# Calculate Daily Score
total_prayers = sum([fajr, dhuhr, asr, maghrib, isha])
growth_points = 1 if tech_time >= 30 else 0
fitness_points = 1 if workout_time >= 30 else 0
detox_points = 2 if "STAYED STRONG" in urge_overcome or urge_overcome == "No Urges Faced Today" else 0
total_score = total_prayers + growth_points + fitness_points + detox_points

# Submit Button & Interactive Feedback
st.markdown("---")
if st.button("💾 Save My Daily Progress"):
    st.balloons()
    st.markdown("<div class='success-box'>Entry Logged Successfully!</div>", unsafe_allow_html=True)
    
    if total_score >= 7:
        st.success("🌟 SubhanAllah! An incredible day of discipline and devotion. Your Creator sees your immense effort. Keep pushing forward!")
    elif total_score >= 4:
        st.info("👍 Solid progress today. Remember, consistency is built step by step. You are actively moving away from your past.")
    else:
        st.warning("🌱 Tomorrow is a fresh canvas gifted to you by Allah. Make istighfar, reset your intention, and step up for Fajr. You can do this!")
