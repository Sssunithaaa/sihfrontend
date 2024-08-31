import streamlit as st
from streamlit_option_menu import option_menu
# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = "home"

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
            background-color: "fff000";
            
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

# with st.sidebar:
if st.session_state.page != "result":  # Skip menu logic if on result page
    selected = option_menu(
        menu_title=None,
        options=["Home","Upload", "About", "Team"],
        icons=["Home","Upload", "About", "Team"],
        orientation="horizontal"
    )

    # Set the page based on the selected option
    if selected == "Upload":
        st.session_state.page = "upload"
    elif selected == "About":
        st.session_state.page = "about"
    elif selected == "Team":
        st.session_state.page = "team"
    elif selected=="Home":
        st.session_state.page = "home"
    else:
        st.session_state.page = "home"
print(st.session_state.page)

def show_result_page():
    # Page title
    st.markdown("<h3 style='text-align: center; color: red;'>Keyword detected</h3>", unsafe_allow_html=True)


    # Adding custom CSS for styling
    st.markdown(
        """
        <style>
        .result-box {
            border: 2px solid black;
            padding: 20px;
            width: 300px;
            height: 200px;
            background-color: #f9f9f9;
            margin: 20px auto;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
            font-family: Arial, sans-serif;
            color: #333;
            text-align: center;
        }
         .resample-button {
            display: block;
            margin: 20px auto;
            padding: 10px 20px;
            background-color: #000000;
            color: white;
            border: white;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        .resample-button:hover {
            color:red;
            border:2px red;

        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Fetching data from the backend
    # For demonstration, we'll use a static string.
    # Replace this with actual data fetching logic.
    keyword_detected = "Keyword"

    # Display the fetched text in a styled box
    st.markdown(
        f"""
        <div  class="result-box">
            <p>{keyword_detected}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <button style='text-align: center;' class="resample-button">Resample</button>
        """,
        unsafe_allow_html=True
    )

# Set the page configuration to wide mode
# st.set_page_config(layout="wide")

# Function to display the hero section
def show_hero_section():
    st.markdown(
        f"""
        <style>
        body {{
            background-image: url('https://unsplash.com/photos/a-black-background-with-a-pink-and-blue-swirl-ZkzobNDayXo');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        .hero-text {{
            text-align: center;
            padding-top: 30px;
            
            font-size: 1.5em;
            max-width: 600px;
            margin: 0 auto;
        }}
        .hero-text h1 {{
          color:red;
        }}
        .hero-button {{
            display: inline-block;
            text-align: center;
            margin-top: 20px;
        }}
        .button {{
            background-color: transparent;
            color: white;
            border: 2px solid white;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            text-decoration: none;
        }}
        .button:hover {{
            background-color: white;
            color: black;
        }}
         .navbar {{
         position: absolute;
    top: 20px; /* Adjust this value to change the distance from the top */
    right: 20px; /* Adjust this value to change the distance from the right */
    display: flex;
    gap: 15px;
    }}
    .navbar button {{
        background-color: transparent;
        color: white;
        border: 2px solid white;
        padding: 10px 20px;
        margin: 0 10px;
        cursor: pointer;
    }}
    .navbar button:hover {{
        color: white;
    }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div>
        <div class="hero-text">
            <h1>FluffyPeanuts SIH 2024</h1>
            <h4>Problem Statement ID - 1680</h4>  
            <h3>Problem Statement Title - Few Shot Language Agnositic Key Word Spotting system (FSLAKWS) for audio files</h3>
            <h5>Organization - National Technical Research Organization (NTRO) </h5>
            <p style='color: red;'>*Click on the upload tab to upload your audio file</p>

        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Function to display the upload page
def show_upload_page():
    st.title("Upload")

    uploaded_files = st.file_uploader(
        "Drag & drop files or Browse",
        type=["mp4", "wav"],
        accept_multiple_files=True
    )

    if uploaded_files:
        st.write(f"Uploading: {len(uploaded_files)} files")
        for uploaded_file in uploaded_files:
            st.write(f"Uploaded: {uploaded_file.name}")

        if st.button("UPLOAD"):
            st.success("Files uploaded successfully!")

    keyword = st.text_input("Enter Keyword")

    language = st.selectbox(
        "Select Language",
        options=["English","Kannada","Hindi","Bangla","Tamil","Telugu", "Spanish", "French", "German", "Chinese"]
    )

    if st.button("SUBMIT"):
        st.session_state.page = "result"
        # st.write(f"Keyword: {keyword}")
        # st.write(f"Selected Language: {language}")
        # st.success("Form submitted successfully!")
        


# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "home"


if st.session_state.page == "home":
    show_hero_section()
elif st.session_state.page == "upload":
    show_upload_page()
elif st.session_state.page == "about":
    st.write("About Page - Content goes here")
elif st.session_state.page == "team":
    st.write("Team Page - Content goes here")
elif st.session_state.page == "result":
    show_result_page()
# Update session state when a navbar button is clicked

