import streamlit as st
from utils.content_generator import generate_content

st.set_page_config(
    page_title="AI Social Media Generator",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Social Media Content Generator")
st.markdown("Generate platform-specific content using Ollama")

# -------------------
# Sidebar
# -------------------

st.sidebar.header("Configuration")

model = st.sidebar.selectbox(
    "Model",
    [
        "llama3.2",
        "mistral",
        "gemma",
        "phi3"
    ]
)

platform = st.sidebar.selectbox(
    "Platform",
    [
        "LinkedIn",
        "Instagram",
        "Twitter/X",
        "Facebook"
    ]
)

tone = st.sidebar.selectbox(
    "Tone",
    [
        "Professional",
        "Casual",
        "Friendly",
        "Motivational",
        "Humorous"
    ]
)

length = st.sidebar.radio(
    "Content Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)

# -------------------
# Main UI
# -------------------

topic = st.text_area(
    "Enter Topic",
    placeholder="Example: Future of Artificial Intelligence"
)

col1, col2 = st.columns(2)

with col1:
    generate_btn = st.button("Generate")

with col2:
    regenerate_btn = st.button("Regenerate")

if generate_btn or regenerate_btn:

    if not topic.strip():
        st.error("Please enter a topic.")
        st.stop()

    with st.spinner("Generating content..."):

        try:

            result = generate_content(
                topic,
                platform,
                tone,
                length,
                model
            )

            st.success("Content Generated Successfully")

            st.subheader("Generated Content")

            st.text_area(
                "Output",
                result,
                height=500
            )

            st.download_button(
                "Download TXT",
                result,
                file_name="social_media_content.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Error: {e}")

            st.info(
                """
                Make sure:

                1. Ollama is running
                2. Model is installed
                3. Internet is not required after model download
                """
            )

with st.expander("How Prompt Engineering Works"):

    st.markdown("""
### System Prompt

You are an expert social media marketing assistant.

### User Prompt

Platform-specific instructions.

### Prompt Chaining

Topic
→ Platform Rules
→ Tone
→ Length
→ Content Generation

### Prompt Refinement

Different prompts for:

- LinkedIn
- Instagram
- Twitter/X
- Facebook
""")