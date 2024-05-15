import streamlit as st
import pandas as pd
import numpy as np
import os

from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

#For animation
import json
from streamlit_lottie import st_lottie



#Wide format
st.set_page_config(layout="wide")


# Option menu in the top bar


testing = option_menu(
    menu_title=None,
    options=["About Me", "Education" , "Certifications", "Experience", "Technical Skills", "Projects", 'Contacts'],
    icons=["person fill","book half", "clock history","tools" ,"clipboard", "lightbulb", 'envelope'],
    orientation='horizontal',
    styles={
        "container": {"padding": "0!important", "background-color": "#F7F9F9"},
        "icon": {"color": "#189AB4", "font-size": "18px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#B8DCE7",
        },
        "nav-link-selected": {"background-color": "#020659"},
    },
)

#Insert Animations

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_welcome = load_lottiefile("lottiefiles/welcome.json")
lottie_ai_1 = load_lottiefile("lottiefiles/ai_1.json")
lottie_ai_2 = load_lottiefile("lottiefiles/ai_2.json")
lottie_prediction = load_lottiefile("lottiefiles/prediction.json")
lottie_doctor = load_lottiefile("lottiefiles/doctor.json")
lottie_consulting = load_lottiefile("lottiefiles/consulting.json")



#Home message
if testing == "About Me":
        #st.write("---")
    st.header("About Me")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.lottie(lottie_doctor, speed=1, width=150, height=150)
        with text_column:
            st.subheader("Medical Doctor")
            st.markdown("""
            As a licensed medical doctor, I play a crucial role in the healthcare system, serving as a medical superintendent and sub-county medical officer of health in a rural county in Kenya. My dedication to improving healthcare access and quality is driven by the numerous health needs of my community.""")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.lottie(lottie_consulting, speed=1, width=150, height=150)
        with text_column:            
            st.subheader("Health systems consultant")
            st.markdown("""
            I am not only a medical practitioner but also a passionate advocate for the improvement of health systems. My expertise extends to policy development at the national level, where I have actively contributed to shaping healthcare policies, ensuring that they are comprehensive and effective in meeting the needs of the population.""")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.lottie(lottie_ai_2, speed=1, width=150, height=150)
        with text_column:           
            st.subheader("Artificial Intelligence Consultant")
            st.markdown("""
           As a licensed medical doctor, I have combined my medical knowledge with computer programming. My passion lies in exploring the potential of Artificial Intelligence in revolutionizing health systems, particularly in developing economies. I firmly believe that AI can play a transformative role in delivering more efficient and accessible healthcare services.

By integrating my medical expertise and my passion for health systems and artificial intelligence, I strive to make a significant impact on healthcare, empowering communities and improving lives. Together, let's envision a healthier and more equitable future.
""")
            
                        
            


    with st.sidebar:
        st.image("logos/fred-logo.png")
        st.image('logos/fred_1.jpg')
        





      




if testing == "Education":
    st.header("Education")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image('logos/iubh.png')
        with text_column:
            st.subheader("MASTERS IN DATA SCIENCE & ARTIFICIAL INTELLIGENCE |IUBH- University Germany ")
            st.write("Dates Attended: Ongoing")
            st.subheader("Knowledge gained")
            st.markdown("""
           During my MSc in Data Science journey, I've encountered an enriching curriculum that has provided me with a strong foundation in essential mathematical concepts, including calculus and linear algebra. These mathematical tools have been instrumental in understanding the complexities of data analysis and manipulation. As I progressed through the program, I delved into the captivating world of machine learning, where I gained insights into various algorithms and techniques for data-driven decision-making.

Moreover, the exploration of deep learning has been particularly fascinating, as I've learned to uncover intricate patterns and structures in vast datasets, paving the way for cutting-edge applications. Additionally, the data engineering component has equipped me with the skills to build and manage efficient data pipelines, enabling seamless data processing.

Now, as I prepare to embark on my thesis journey focusing on computer vision, I feel exhilarated to delve deeper into this captivating field. Computer vision offers endless possibilities for understanding and interpreting visual data, and I am eager to explore applications such as image recognition and object detection.

Overall, my MSc in Data Science has been a transformative experience, providing me with a versatile skill set to tackle real-world data challenges and contribute to the advancement of computer vision and data science as a whole. I am excited about the opportunities ahead and the potential to make a meaningful impact in the ever-evolving data science landscape.
            """)



    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image('moi_logo.jpg', width=150)
        with text_column:
            st.subheader("MASTERS IN FIELD EPIDEMIOLOGY | Moi University")
            st.write("Dates Attended: Ongoing")
            st.subheader("Knowledge gained")
            st.markdown("""
           As an FELTP resident, I have gained a wealth of knowledge and skills in the field of public health. Throughout the program, I have delved into various essential subjects, such as epidemiology, biostatistics, environmental health, health policy, and management, as well as social and behavioral sciences. These areas of study have provided me with a comprehensive understanding of disease prevention, health promotion, and the planning and management of healthcare systems.

Moreover, the program has highlighted the importance of addressing health disparities and focusing on community health. I have learned to analyze and assess the health needs of diverse populations and design effective health programs and policies to meet those needs. Additionally, global health has been a significant aspect of my learning, allowing me to comprehend the complexities of health challenges on an international scale.

As I approach the end of my FELTP journey, I feel equipped and prepared to make a meaningful impact in the field of public health. I am excited to utilize my expertise to advocate for the improvement of health and well-being in communities and contribute to positive changes in healthcare systems. The skills I have acquired during this program will undoubtedly play a crucial role in my future career, as I strive to create a healthier and more equitable world for everyone.
            """)            
    
    

    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image('logos/uon.jpg')
        with text_column:
            st.subheader("BACHELORS IN MEDICINE AND SURGERY | Univeristy of Nairobi")
            st.write("Dates Attended: 20008-2013")
            st.subheader("Knowledge gained")
            st.markdown("""
           
Throughout my journey pursuing a degree in Medicine and Surgery, I have been immersed in a captivating curriculum that has prepared me for a fulfilling career in the medical field. From the very beginning, I delved into foundational subjects such as anatomy, physiology, and biochemistry, which provided a solid understanding of the human body's intricacies and functions.

As I progressed in my studies, I delved deeper into clinical subjects, such as pathology, pharmacology, and internal medicine, where I learned to diagnose and treat a wide range of medical conditions. Additionally, my training in surgery has honed my surgical skills and techniques, equipping me to perform essential surgical procedures and interventions.

One of the most rewarding aspects of my degree has been the clinical rotations and hands-on experience in various medical specialties, including pediatrics, obstetrics, and emergency medicine. These practical experiences have allowed me to witness the real-life impact of medical care on patients' lives, solidifying my passion for healthcare.
            """)            
    


if testing == "Certifications":
    # Non-Medical Training and Certification Data
    non_medical_data = {
        "Certifying Organization": ["Yale University", "Nairobi Securities Exchange", "Nairobi Securities Exchange", "University of Nairobi-Kenya Sign Language Training Program"],
        "License / Certificate Number": ["Certificate on Coursera-Financial Markets", "Derivatives- Options & Futures", "Certificate- Securities Markets and its products", "Basic Sign Language Skills"],
        "Dates Valid": [2017, 2019, 2016, 2007]
    }

    # Short Term Medical Training and Certification Data
    short_term_medical_data = {
        "Certifying Organization": ["JohnsHopkins-Bloomberg School of Public Health", "Imperial College London", "Imperial College London", "Imperial College London", "Imperial College London", "NASCOP", "JohnsHopkins-Bloomberg School of Public Health", "University of Cape Town", "JohnsHopkins-Bloomberg School of Public Health", "JohnsHopkins-Bloomberg School of Public Health", "JohnsHopkins-Bloomberg School of Public Health", "NASCOP", "Resuscitation Council of Kenya"],
        "License / Certificate": ["Introduction to Systematic Review and Meta-Analysis- Certificate on Coursera", "Survival Analysis in R for Public Health- Certificate on Coursera", "Linear & Logistic Regression in R for Public Health- Certificate on Coursera", "Introduction to Statistics and Data Analysis in Public Health- Certificate on Coursera", "NHITC- National HIV Integrated Training Course for Health Workers", "Hypothesis Testing in Public Health- Certificate on Coursera", "Understanding Clinical Research- Certificate on Coursera", "Data and Health Indicators in Public Health (License FR9WMV24WS7X)", "Design and Interpretation of Clinical Trials- Certificate on Coursera", "HIV treatment Guidelines- Trainer of Trainers", "Advanced Trauma Life Support", "", None],
        "Grade": ["100%", "96%", "92.2%", "99.6%", "Na", "94.7%", "92.8%", "95.7%", "90%", "2016 & 2018", "2014", "", ""],
        "Duration": ["6 weeks", "4 weeks", "8 weeks", "4 weeks", "12 weeks", "4 weeks", "6 weeks", "4 weeks", "6 weeks", "4 weeks", "4 weeks", "", ""],
        "Year": [2020, 2020, 2020, 2020, 2019, 2019, 2019, 2019, 2018, 2019, 2019, 2018, 2014]
    }

    # Create DataFrames
    non_medical_df = pd.DataFrame(non_medical_data)
    short_term_medical_df = pd.DataFrame(short_term_medical_data)

    # Streamlit App
    st.title("Training and Certification")

    st.header("NON-MEDICAL TRAINING AND CERTIFICATION")

    for _, row in non_medical_df.iterrows():
        st.write(f"**Certifying Organization:** {row['Certifying Organization']}")
        st.write(f"**License / Certificate Number:** {row['License / Certificate Number']}")
        st.write(f"**Dates Valid:** {row['Dates Valid']}\n")

    st.header("SHORT TERM MEDICAL TRAININGS AND CERTIFICATIONS")

    for _, row in short_term_medical_df.iterrows():
        st.write(f"**Certifying Organization:** {row['Certifying Organization']}")
        st.write(f"**License / Certificate:** {row['License / Certificate']}")
        st.write(f"**Grade:** {row['Grade']}")
        st.write(f"**Duration:** {row['Duration']}")
        st.write(f"**Year:** {row['Year']}\n")
        



# LinkedIn Experience Data
experience_data = [
    {
        "Position": "Data/Artificial Intelligence consultant",
        "Company": "Consultancy",
        "Duration": "Apr 2019 - Present · 4 yrs 4 mos",
        "Location": "Nairobi County, Kenya",
        "Projects": [
            {
                "Project": "Artificial Intelligence",
                "Scope": "Developing a chat bot that would recommend health specialists and professionals based on symptoms.",
                "Role": "Backend developer working with python",
                "Duration": "2022"
            },
            {
                "Project": "Health data analyst",
                "Scope": "Data cleaning and analysis in R, Python, Stata and SPSS",
                "Role": "Methodology advisory and data analysis in over 10 health care related research projects.",
                "Duration": "2019-2022"
            },
            {
                "Project": "Telemedicine consultant",
                "Scope": "Electronic stethoscope for telemedicine",
                "Role": "Developing a study protocol to compare an electronic stethoscope with conventional stethoscope models.",
                "Duration": "2019"
            }
        ]
    },
    {
        "Position": "Health Systems Consultant",
        "Company": "Self · Part-time",
        "Duration": "Jan 2016 - Present · 7 yrs 7 mos",
        "Location": "Nairobi County, Kenya",
        "Projects": [
            {
                "Project": "HIV Care",
                "Scope": "Kenyan National ART guidelines 2022 / Adolescent Package of Care/ Advanced HIV disease",
                "Role": "Part of the teams that created the training material and conducted the dissemination.",
                "Duration": "2022"
            },
            {
                "Project": "Technical advisor on EMR",
                "Scope": "Multinational electronic medical records system being implemented in 4 countries: Kenya, Tanzania, Haiti, and India.",
                "Role": "Technical advisor/ End user advisor. Guided the team on the UI/UX requirements of the EMR system particularly for local implementation.",
                "Duration": "2016-2019"
            },
            {
                "Project": "Health Financing consultant",
                "Scope": "Financial turnaround plan for a health facility in Kenya",
                "Role": "Advisory on financial turn around plan",
                "Duration": "2016"
            },
            {
                "Project": "Human resource for health consultant",
                "Scope": "Advisory on establishing an alternative system for managing health system",
                "Role": "Part of a team of professionals seeking alternative avenues of managing human resource in health",
                "Duration": "2017"
            }
        ]
    },
    {
        "Position": "Health Facility Manager",
        "Company": "Narok County",
        "Duration": "Nov 2018 - Present · 4 yrs 9 mos",
        "Location": "Narok County",
        "Projects": [
            {
                "Project": "Medical Superintendent",
                "Scope": "In charge of a Level 4 hospital in Narok County.",
                "Role": "Clinical duties in Inpatient and Outpatient client care as Second on call. | Fiduciary responsibility over the hospital's accounts. | Team lead of over 60 healthcare and affiliated workers.",
                "Duration": "2018 - Present"
            },
            {
                "Project": "Medical Officer of Health",
                "Scope": "Medical supervision of Sub County",
                "Role": "Supervision of over 10 health facilites",
                "Duration": "2023 - Present"
            }
        ]
    },
    {
        "Position": "Co Chair- Regional HIV Technical Working Group",
        "Company": "SRV (South Rift Valley) Region- Counties under HJF Medical Research International · Part-time",
        "Duration": "May 2019 - Present · 4 yrs 3 mos",
        "Location": "SRV (South Rift Valley) Region- Counties under HJF Medical Research International · Part-time",
        "Projects": [
            {
                "Project": "Scope",
                "Scope": "7 Counties in Kenya- Nandi, Kericho, Bomet, Nakuru, Samburu, Baringo, and Narok with a catchment population of over 6 million.",
                "Role": "Team lead of a multidisciplinary team from the Ministry of Health, Walter Reed Program, and various County Departments of Health offering technical expertise in HIV care.",
                "Duration": ""
            },

        ]
    },
    {
        "Position": "CHAIR- Narok County HIV Technical Working Group",
        "Company": "Ministry of Health",
        "Duration": "May 2019 - Present · 4 yrs 3 mos",
        "Location": "Ministry of Health",
        "Projects": [
            {
                "Project": "Scope",
                "Scope": "Team lead of diverse professionals from Narok County offering technical expertise in HIV care",
                "Role": "",
                "Duration": ""
            }
        ]
    },
    {
        "Position": "Medical Doctor",
        "Company": "Narok County",
        "Duration": "2015 - 2018 · 3 yrs",
        "Location": "Narok County",
        "Projects": [
            {
                "Project": "Scope",
                "Scope": "Conducted daily ward rounds in the adult and pediatric wards. Managed obstetric and minor surgical emergencies. Advanced evidence-based medicine by coordinating CMEs and supervising research.",
                "Role": "",
                "Duration": ""
            }
        ]
    },
    {
        "Position": "2016 NASCOP HIV Guidelines Trainer",
        "Company": "Ministry of Health SRV (South Rift Valley) Region- Counties under HJF Medical Research International · Contract",
        "Duration": "Jul 2016 - Aug 2016 · 2 mos",
        "Location": "Ministry of Health SRV (South Rift Valley) Region- Counties under HJF Medical Research International · Contract",
        "Projects": [
            {
                "Project": "Scope",
                "Scope": "Use of small groups in training healthcare workers on the 2016 guidelines.",
                "Role": "",
                "Duration": ""
            }
        ]
    },
    {
        "Position": "Medical Intern",
        "Company": "PCEA Kikuyu",
        "Duration": "Apr 2014 - Apr 2015 · 1 yr 1 mo",
        "Location": "Kenya",
        "Projects": [
            {
                "Project": "Scope",
                "Scope": "On-job training for clinical workers on evidence-based HIV management.",
                "Role": "",
                "Duration": ""
            }
        ]
    }
]




if testing == "Experience":
    # Streamlit App
    st.title("Professional Work Experience")

    for exp in experience_data:
        st.header(exp["Position"])
        st.write(exp["Company"])
        st.write(exp["Duration"])
        st.write(exp["Location"])
        
        for i, project in enumerate(exp["Projects"], 1):
            st.subheader(f"{i}. {project['Project']}")
            st.info(f"Project scope- {project['Scope']}")
            st.info(f"Project role- {project['Role']}")
            if project["Duration"]:
                st.info(f"Duration: {project['Duration']}")
            st.write("\n")



if testing == "Technical Skills":
    st.image('logos/skills.png')

if testing == "Projects":
    st.image('logos/apache.png')



if testing == "Contacts":
    st.header("Contacts")
    st.subheader("Name: Dr. Fred Mutisya")
    st.subheader("KMPDB No. - A9338")
    st.subheader(":email: E-mail Address: fredmutisya11@gmail.com")
    st.subheader(":phone: Business Phone: 0112299772")
    st.subheader(":telephone: Personal Phone: 0720624395")
    st.subheader("Linkedin: Dr. Fred Mutisya")





