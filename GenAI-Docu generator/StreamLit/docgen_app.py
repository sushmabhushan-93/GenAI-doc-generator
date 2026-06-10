import streamlit as st
import requests
import re

st.set_page_config(page_title="DocGen AI", page_icon="📄", layout="centered")

N8N_WEBHOOK_URL = "https://sushmanb123.app.n8n.cloud/webhook/9fe50740-da5c-4dee-8a8f-78ea18177553"

st.title("🤖 AI Code Documentation Generator")
st.markdown("Paste any public GitHub repository URL and get AI-generated documentation instantly.")

repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/username/repository"
)

def is_valid_github_url(url):
    return bool(re.match(r'https?://github\.com/[\w\-]+/[\w\-\.]+', url))

if st.button("🚀 Generate Documentation", type="primary"):
    if not repo_url:
        st.warning("Please enter a GitHub URL first.")
    elif not is_valid_github_url(repo_url):
        st.error("That doesn't look like a valid GitHub URL.")
    else:
        with st.spinner("Triggering AI documentation pipeline..."):
            try:
                requests.post(
                    N8N_WEBHOOK_URL,
                    json={"repoUrl": repo_url},
                    timeout=180
                )
            except:
                pass

        st.success("✅ Documentation pipeline triggered successfully!")
        st.info("📧 Check your email — the documentation will be delivered with a Google Drive link shortly.")
        
        st.markdown("---")
        st.markdown("### What happens next?")
        st.markdown("""
        1. 🤖 **AI Agent** reads your GitHub repository
        2. 📝 **Gemini** generates structured documentation  
        3. ☁️ **Google Drive** saves the documentation file
        4. 📧 **Gmail** sends you the link
        """)

st.markdown("---")
st.caption("Built with n8n + Google Gemini + Streamlit | Sushma Bhushan")
