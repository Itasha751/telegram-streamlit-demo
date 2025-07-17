import streamlit as st
import json
from datetime import datetime

st.set_page_config(page_title="עדכוני טלגרם", layout="centered")
st.title("📢 עדכוני טלגרם – דמו")

with open("data.json", "r", encoding="utf-8") as f:
    posts = json.load(f)

posts.sort(key=lambda x: x["timestamp"], reverse=True)

for post in posts:
    st.markdown("---")
    st.markdown(f"🕒 {post['timestamp']}")
    st.write(post["text"])

    if post.get("media_type") == "image":
        st.image(post["media_path"])
    elif post.get("media_type") == "video":
        st.video(post["media_path"])
