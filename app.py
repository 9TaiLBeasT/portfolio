import streamlit as st
import base64

def img_decode(path):
    with open(path, "rb") as img_file:
        return "data:image/png;base64," + base64.b64encode(img_file.read()).decode()
    
def social_media_icons(data):
    social_icons_html = [
        f"<a href='{data[platform][0]}' target='_blank' style='margin-right: 10px;'>"
        f"<i class='{data[platform][1]}' style='color: {data[platform][2]};'></i>"
        f"</a>" for platform in data
    ]
    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", unsafe_allow_html=True)

    

def home():
    
    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="G Taraka Shiva Ganesh Portfolio",
        page_icon="☠️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.sidebar.header("Configuration")
    
    
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
                        <img src="{img_decode(r"assets/gun.png")}" alt="Ganesh">
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, 
    unsafe_allow_html=True)

    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Machine Learning and Software Engineer</div>""", unsafe_allow_html=True)

    st.markdown("""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">""", unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
    "Kaggle": ["https://www.kaggle.com/auu23egcse045", "fa-brands fa-kaggle fa-bounce fa-xl", "#20beff"],
    "LinkedIn": ["https://www.linkedin.com/in/gtsganesh/", "fa-brands fa-linkedin fa-beat-fade fa-xl", "#108bea"],
    "GitHub": ["https://github.com/9TaiLBeasT", "fa-brands fa-github fa-beat fa-xl", "#000000"],
    "X": ["https://x.com/GGanesh192349?t=wCMPvfh1d8_aHT4IuTxP_g&s=09", "fa-brands fa-square-x-twitter fa-bounce fa-xl", "#000000"], 
}

    
    social_media_icons(social_icons_data)

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
