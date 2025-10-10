import streamlit as st
from resume_analyzer import extract_text_from_pdf, load_keywords, analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", page_icon="icon.png", layout="centered")

st.title("🤖 AI Resume Analyzer")
st.write("Upload your resume and get an instant skill match report for your chosen role!")

uploaded_file = st.file_uploader("📂 Upload your Resume (PDF only)", type=["pdf"])
role = st.selectbox("🎯 Choose Target Job Role:", ["Select Role", "Data Analyst", "Web Developer", "AI Engineer"])

if st.button("🔍 Analyze Resume"):
    if uploaded_file and role != "Select Role":
        with st.spinner("Analyzing your resume..."):
            text = extract_text_from_pdf(uploaded_file)
            keywords = load_keywords(role)
            found, missing, score = analyze_resume(text, keywords)

            st.success(f"✅ Resume Match Score: {score}%")
            st.progress(score / 100)

            st.subheader("🧠 Found Skills:")
            st.write(", ".join(found) if found else "No relevant skills found")

            st.subheader("❌ Missing Skills:")
            st.write(", ".join(missing) if missing else "None, great job!")

            st.subheader("💬 Suggestions:")
            if missing:
                st.info(f"Add {', '.join(missing)} to improve your {role} resume.")
            else:
                st.balloons()
                st.success("Your resume perfectly matches this role!")
    else:
        st.warning("Please upload a resume and select a job role.")
