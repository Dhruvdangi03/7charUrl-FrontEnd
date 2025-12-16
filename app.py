import streamlit as st
from services.url_service import URLService
from utils.styles import load_styles

# ---------- Page Config ----------
st.set_page_config(
    page_title="7Char URL Shortener",
    page_icon="🔗",
    layout="centered"
)

st.markdown(load_styles(), unsafe_allow_html=True)

# ---------- Hero ----------
st.markdown(
    """
    <div class="hero">
        <h1>7CharURL</h1>
        <p>Minimal links • Maximum clarity</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- Tabs ----------
tab_auto, tab_custom = st.tabs(["Auto Shorten", "Custom Link"])

# ---------- Auto Shorten ----------
with tab_auto:
    st.subheader("Auto-generate short link")

    long_url = st.text_input(
        "Long URL",
        placeholder="https://example.com"
    )

    if st.button("Shorten", use_container_width=True):
        if not long_url:
            st.error("Please enter a URL")
        else:
            data, status = URLService.shorten(long_url)

            if status == 200:
                st.markdown(
                    f'<div class="result">{data["short_url"]}</div>',
                    unsafe_allow_html=True
                )
            else:
                st.error(data.get("error", "Something went wrong"))

# ---------- Custom Shorten ----------
with tab_custom:
    st.subheader("Create custom short link")

    custom_long = st.text_input(
        "Long URL",
        placeholder="https://example.com",
        key="custom_long"
    )

    custom_code = st.text_input(
        "Custom alias",
        placeholder="my-link"
    )

    if st.button("Create", use_container_width=True):
        if not custom_long or not custom_code:
            st.error("Both fields are required")
        else:
            data, status = URLService.custom(custom_long, custom_code)

            if status == 200:
                st.markdown(
                    f'<div class="result">{data["custom_url"]}</div>',
                    unsafe_allow_html=True
                )

            elif status == 409:
                st.warning("This custom alias is already taken. Try another one.")

            else:
                st.error(data.get("error", "Something went wrong"))

# ---------- Footer ----------
st.caption("Built with Go + Gin backend • Streamlit frontend")
