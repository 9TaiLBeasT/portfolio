import streamlit as st
import base64

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def home():
    
    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="G Taraka Shiva Ganesh Portfolio",
        page_icon="☠️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.sidebar.header("Configuration")
    
    img = get_img_as_base64(r".\assets\background1.jpg")
    
    background = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main{{
        background-image: url("https://mir-s3-cdn-cf.behance.net/project_modules/1400/b1489a55645295.5b463687dbf0a.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("https://cdnb.artstation.com/p/assets/images/images/054/594/479/4k/hue-teo-the-goat.jpg?1664901036");
     background-size: cover;
    background-position: center; 
    background-repeat: no-repeat;
    background-attachment: fixed;
    }}
    
    </style>
    """
    st.markdown(background, unsafe_allow_html=True)

    # CSS styles file
    with open(r"styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open(r"assets/gun.png", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    # PDF CV file
    with open(r"assets/Ganesh_Resume.docx", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    
    # Top title
    st.write(f"""<div class="title"><strong>Hi! My name is</strong> G. Taraka Shiva Ganesh👋</div>""", unsafe_allow_html=True)

    # Profile image
    st.write(f"""
    <div class="container">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Ganesh">
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, 
    unsafe_allow_html=True)

    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Machine Learning and Software Engineer</div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        # Platform: [URL, Icon]
        "Kaggle": ["https://www.kaggle.com/auu23egcse045", "https://www.kaggle.com/static/images/site-logo.svg"],
        "LinkedIn": ["https://www.linkedin.com/in/gtsganesh/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/9TaiLBeasT", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
        "Twitter": ["", "https://cdn-icons-png.flaticon.com/512/733/733579.png"],
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

    st.write("##")

    # About me section
    st.subheader("About Me")
    st.write("""
    - 🧑‍💻 I am a **Computer Science Engineering Student** 

    - ❤️ I am passionate about **Machine Learning/Deep Learning, MLOps, Data, Software Engineering, Computer Vision**, and more!
    
    - 📫 How to reach me: flameganesh7@gmail.com
    
    - 🏠 India
    """)

    st.write("##")

    # Download CV button
    st.download_button(
        label="📄 Download my resume",
        data=pdf_bytes,
        file_name="Ganesh_Resume.docx",
        mime="application/pdf",
    )

    st.write("##")
    
    st.write(f"""<div class="subtitle" style="text-align: center;">⬅️ Check out my Projects in the navigation menu! (Coming soon...)</div>""", unsafe_allow_html=True)

if __name__ == "__main__":
    home()
