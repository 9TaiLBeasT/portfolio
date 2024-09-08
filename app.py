import streamlit as st
import base64
import time

import base64

def img_decode(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')


def background():
    background = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
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
        transition: transform 0.5s ease, background-position 0.5s ease, box-shadow 0.5s ease;
        box-shadow: 
            0 0 10px rgba(0, 191, 255, 0.6),    
            0 0 20px rgba(70, 130, 180, 0.4),   
            0 0 30px rgba(0, 255, 255, 0.3),   
            0 0 40px rgba(25, 25, 112, 0.2);
    }}

    [data-testid="stHorizontalBlock"]:hover {{
        transform: scale(1.05);
        background-position: 50% 50%;
        box-shadow: 
            0 0 20px rgba(0, 191, 255, 0.8),    
            0 0 40px rgba(70, 130, 180, 0.6),   
            0 0 60px rgba(0, 255, 255, 0.5),   
            0 0 80px rgba(25, 25, 112, 0.4);
        animation: pulse 2s infinite;
    }}
    
    @keyframes pulse {{
        0% {{
            box-shadow: 
                0 0 10px rgba(0, 191, 255, 0.6),    
                0 0 20px rgba(70, 130, 180, 0.4),   
                0 0 30px rgba(0, 255, 255, 0.3),   
                0 0 40px rgba(25, 25, 112, 0.2);
        }}
        50% {{
            box-shadow: 
                0 0 20px rgba(0, 191, 255, 0.8),    
                0 0 40px rgba(70, 130, 180, 0.6),   
                0 0 60px rgba(0, 255, 255, 0.5),   
                0 0 80px rgba(25, 25, 112, 0.4);
        }}
        100% {{
            box-shadow: 
                0 0 10px rgba(0, 191, 255, 0.6),    
                0 0 20px rgba(70, 130, 180, 0.4),   
                0 0 30px rgba(0, 255, 255, 0.3),   
                0 0 40px rgba(25, 25, 112, 0.2);
        }}
    }}

    [data-testid="stBaseButton-secondary"] {{
        background-color: lightblue;
        border-color: #FFD700; 
        color: #fff;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease, background-position 0.5s;
        background-image: linear-gradient(135deg, lightskyblue, darkblue);
        background-size: 200% 200%;
    }}

    [data-testid="stBaseButton-secondary"]:hover {{
        background-position: 100% 0; 
        transform: scale(1.1); 
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.5); 
    }}
    
    [data-testid="stBaseButton-secondary"]:active {{
        transform: scale(0.95);
        background-color: #FF4500; 
        box-shadow: 0 0 10px rgba(255, 69, 0, 0.8); 
    }}
    
    [data-testid="stTab"] {{
        background-color: orangered; 
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.4s ease, box-shadow 0.4s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }}

    [data-testid="stTab"]:hover {{
        background-color: #001f3f; /* Black-blue background on hover */
        box-shadow: 0 8px 16px rgba(0, 31, 63, 0.7), 0 0 30px rgba(255, 69, 0, 0.8);
    }}

    [data-testid="stTab"]:active {{
    background-color: #001f3f; 
    box-shadow: 0 4px 8px rgba(0, 31, 63, 0.5);
    }}
    

    [data-testid="stHeader"] {{
        background-color: black;
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        transition: transform 0.5s ease, background-position 0.5s ease, box-shadow 0.5s ease;
        box-shadow:
        0 0 10px rgba(0, 191, 255, 0.6),    
        0 0 20px rgba(70, 130, 180, 0.4),   
        0 0 30px rgba(0, 255, 255, 0.3),   
        0 0 40px rgba(25, 25,112, 0.2);
        animation: pulse 2s infinite;
        background-size: 200% 200%;
        color: white;
        justify-content: flex-end;
        position: sticky;
        z-index: 100;
        
        
    }}
    </style>
    <div data-testid="stHeader">
        <a href="#about-me" class="small-text" style="padding-right: 400px;">About Me</a>
        <a href="#skills" class="small-text" style="padding-right: 300px;">Skills</a>
        <a href="#projects" class="small-text" style="padding-right: 180px;">Projects</a>
        <a href="app-breast-cancer-prediction-57kxxffcgbweunup2azemk.streamlit.app" class="small-text" style="padding-right: 80px;">Blog</a>
        <a href="#Ganesh" class="small-text" style="padding-right: 1320px; font-size: 20px;">⊙ Ganesh</a>
    </div>

    </style>
    """
    st.markdown(background, unsafe_allow_html=True)      
                

def skills():
    with st.container():
        col1 = st.columns(1)
        with col1[0]:
            st.write("")
            st.markdown('<h2 class="textpad" style="color:white;">Skills</h2>', unsafe_allow_html=True)
            st.markdown('<h8 class="textpad" style="color:lightcyan;">My technical & miscellaneous skills</h8>', unsafe_allow_html=True)

            st.markdown(
                """
                <style>
                .container {
                    padding-left: 20px;
                }
                .progress {
                    width: 400px;
                    background-color: #f3f3f3;
                    border-radius: 5px;
                    overflow: hidden;
                    height: 18px;
                    margin-bottom: 10px;
                    padding: 2px;
                }
                .progress-bar {
                    height: 100%;
                    background-color: #4caf50;
                    text-align: center;
                    line-height: 15px;
                    color: white;
                    width: 0%;
                    transition: width 0.5s;
                }
                .stTabs {
                    padding: 10px;
                }
                </style>
                """, unsafe_allow_html=True
            )

            tab1, tab2, tab3 = st.tabs([":material/Memory: AI & Data Science ", ":material/Code: Programming", ":material/Neurology: Miscellaneous"])

            with tab1:
                skill_list = [("Machine Learning", 85), ("Deep Learning", 75), ("Data Analysis", 50)]
                for skill, percent in skill_list:
                    st.markdown(f"**{skill}**", unsafe_allow_html=True)
                    st.markdown(f"""
                    <div class="progress">
                        <div class="progress-bar" style="width: {percent}%;">{percent}%</div>
                    </div>
                    """, unsafe_allow_html=True)

            with tab2:
                skill_list = [("Python", 95), ("Java", 60), ("SQL", 50), ("C", 50)]
                for skill, percent in skill_list:
                    st.markdown(f"**{skill}**", unsafe_allow_html=True)
                    st.markdown(f"""
                    <div class="progress">
                        <div class="progress-bar" style="width: {percent}%;">{percent}%</div>
                    </div>
                    """, unsafe_allow_html=True)

            with tab3:
                skill_list = [("Communication", 90), ("Teamwork", 85), ("Problem-Solving", 80)]
                for skill, percent in skill_list:
                    st.markdown(f"**{skill}**", unsafe_allow_html=True)
                    st.markdown(f"""
                    <div class="progress">
                        <div class="progress-bar" style="width: {percent}%;">{percent}%</div>
                    </div>
                    """, unsafe_allow_html=True)
    
            st.write("")
            st.write("")

def projects():
    st.markdown('<link rel="stylesheet" href="styles.css">', unsafe_allow_html=True)
    with st.container():
        st.write("")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<h2 class="textpad" style="color:white;">Projects</h2>', unsafe_allow_html=True)
            
            st.markdown(
                f"""
                <div class="flip-container">
                    <div class="flip-card">
                        <div class="flip-card-front">
                            <img src="data:image/png;base64,{img_decode(r"./assets/background1.jpg")}" width="250" height="300">
                        </div>
                        <div class="flip-card-back">
                            <h8>Project Details: <a href="https://example.com" target="_blank" style="color: #1e90ff; text-decoration: underline;">click here</a></h8> 
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            st.markdown('<h9 class="textpad" style="color:lightcyan;">Coming Soon.....</h9>', unsafe_allow_html=True)

        st.write("")

    
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
    
def social_media_icons(data):
    social_icons_html = [
        f"<a href='{data[platform][0]}' target='_blank' style='margin-right: 10px;'>"
        f"<i class='{data[platform][1]}' style='color: {data[platform][2]};'></i>"
        f"</a>" for platform in data
    ]
    return "".join(social_icons_html)

# Footer function
def add_footer(data):
    footer = f"""
    <div class="footer">
        <p>&copy; 2024 Ganesh's Portfolio | Follow me on:</p>
        {social_media_icons(data)}
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)

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
        col1, col2 = st.columns(2, vertical_alignment="center")
        
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
                        <div class="profile-container">
                            <img src="data:image/png;base64,{img_decode(r"./assets/gun.png")}" class="profile-pic" alt="Profile Picture">
                        </div>
                    """, unsafe_allow_html=True)
            

        
    st.write("##")
    
    with st.container(border=False):
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("")
            st.markdown('<h2 class="textpad" style="color:white;">Any type of question & Discussion...</h2>', unsafe_allow_html=True)
            st.markdown('<h4 class="textpad" style="color:white;">Let\'s Talk  <span style="color:darkorange;">______________________</span></h4>', unsafe_allow_html=True)
            st.write("")
            st.markdown('<h3 class="textpad" style="color:darkorange;">gtsganesh2005@outlook.com</h3>', unsafe_allow_html=True)
            st.markdown('<h3 class="textpad" style="color:white;">Whatsapp: 7842329947</h3>', unsafe_allow_html=True)
            st.write("")
        
        with col2:
            st.write("")
            st.markdown('<h2 style="color:white;">About Me</h2>', unsafe_allow_html=True)
            st.markdown('<h8  style="color:lightcyan;">I am a passionate Computer Science and Engineering student with a keen interest in Artificial Intelligence and Machine Learning.</h8>', unsafe_allow_html=True)
            st.write("")
            st.markdown('<h9  style="color:lightcyan;">Name      :      G. Taraka Shiva Ganesh</h9>', unsafe_allow_html=True)
            st.markdown('<h9  style="color:lightcyan;">Email     :      gtsganesh2005@outlook.com</h9>', unsafe_allow_html=True)
            st.markdown('<h9  style="color:lightcyan;">website   :      ganesh-portfolio.streamlit.app</h9>', unsafe_allow_html=True)
            st.write('')
            st.download_button(
            label="Download CV",
            data=pdf_bytes,
            file_name="Ganesh_Resume.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            key="CV"
            )
            st.write("")
            
    st.write("##")
    
    skills()
    
    st.write("##")
    
    projects()
    
    st.write("##")
    
    add_footer(social_icons_data)
    

    
if __name__ == "__main__":
    home()
