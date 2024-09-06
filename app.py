import streamlit as st
import base64

def background():
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
    
    [data-testid="stHorizontalBlock"] {{
    background-image: url("https://devsnap.nyc3.digitaloceanspaces.com/devsnap.me/codepen-VjrZWv.png");
    background-size: cover;
    background-position: center; 
    background-repeat: no-repeat;
    background-attachment: fixed;
    }}
    
    </style>
    """
    st.markdown(background, unsafe_allow_html=True)
    
    return background

    
    
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
    <div class="social-icons-container">
        {''.join(social_icons_html)}
    </div>""", unsafe_allow_html=True)
    

def home():
    
        # PDF CV file
    with open(r"assets/Ganesh_Resume.docx", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
    
    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Ganesh's Portfolio",
        page_icon="☠️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    with st.sidebar:
        st.download_button(
            label="📄 Download my resume",
            data=pdf_bytes,
            file_name="Ganesh_Resume.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
    
    #background UI
    background()

    # CSS styles file
    with open(r"styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.markdown("""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">""", unsafe_allow_html=True)

    social_icons_data = {
    "Kaggle": ["https://www.kaggle.com/auu23egcse045", "fa-brands fa-kaggle fa-bounce fa-xl", "#20beff"],
    "LinkedIn": ["https://www.linkedin.com/in/gtsganesh/", "fa-brands fa-linkedin fa-beat-fade fa-xl", "#108bea"],
    "GitHub": ["https://github.com/9TaiLBeasT", "fa-brands fa-github fa-beat fa-xl", "#000000"],
    "X": ["https://x.com/GGanesh192349?t=wCMPvfh1d8_aHT4IuTxP_g&s=09", "fa-brands fa-square-x-twitter fa-bounce fa-xl", "#000000"], 
    }

    with st.container(border=False):
        col1, col2 = st.columns(2)
        
        with col1:
            
            st.write(f"""<div class="title"><strong>Hi, I'm </strong>Ganesh</div>""", unsafe_allow_html=True)
            st.write("")
            st.markdown("""
                <p class='custom-text'>
                    I am a <strong>Computer Science Engineering</strong> student deeply fascinated by the world of technology and innovation. With a keen interest in <em>Machine Learning</em> and <em>Artificial Intelligence</em>, I am dedicated to understanding and mastering these transformative technologies. 
                    My academic journey has equipped me with a strong foundation in programming, data structures, and algorithms, while my passion drives me to explore advanced topics such as neural networks, natural language processing, and computer vision.
                </p>
            """, unsafe_allow_html=True)

            st.write("")
            st.write("")
            # Social Icons
            social_media_icons(social_icons_data)

        with col2:
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
    
    st.write(f"""<div class="subtitle" style="text-align: center;">⬅️ Check out my Projects in the navigation menu! (Coming soon...)</div>""", unsafe_allow_html=True)

if __name__ == "__main__":
    home()
