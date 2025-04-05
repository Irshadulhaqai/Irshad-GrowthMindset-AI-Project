# Import necessary libraries
import streamlit as st  # For creating the web app interface
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For data visualization
import os  # For operating system related functions

# --- App Configuration ---
# Set page configuration including title, icon and layout
st.set_page_config(page_title="Growth Mindset With Ai", page_icon="🌱", layout="wide")
# Set the main title of the app
st.title("🌱 Growth Mindset With Ai")

# --- Sidebar Navigation ---
# Create sidebar title
st.sidebar.title("Navigation")
# Create radio buttons in sidebar for page navigation
page = st.sidebar.radio("Go to", ["Home", "Mindset Quiz", "Progress Tracker", "Resources"])

# --- Home Page ---
if page == "Home":
    # Display header for home page
    st.header("🚀 Welcome to the Growth Mindset Challenge!")
    # Display welcome message
    st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🌟")

    # --- Quote Section ---
    # Display header for quote section
    st.header("💡Today's Growth Mindset Quote")
    # Display a motivational quote
    st.write("Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill")

    # --- Challenge Section ---
    # Display header for challenge section
    st.header("🔧 What's Your Challenge Today?")
    # Create text input field for user to describe their challenge
    user_input = st.text_input("Describe a challenge you're facing:")

    # --- Condition Section --- 
    # Check if user has entered any input
    if user_input:
        # Display success message with user's input
        st.success(f"💪 You're facing: {user_input}. Keep pushing forward towards your goal🚀")
    else:
        # Display warning if no input is provided
        st.warning("Tell us about your challenge to get started!")

    # --- Reflecting Section ---
    # Display header for reflection section
    st.header("🧠 Reflect on Your Learning")
    # Display prompt for reflection
    st.write("Every experience teaches us something valuable. Share a lesson you've learned recently.💡")

    # Create text area for user reflections
    reflection = st.text_area("Write your reflections here:")

    # Check if reflection is provided
    if reflection:
        # Display success message with reflection
        st.success(f"✨ Great Insight! Your reflection: {reflection}")
    else:
        # Display info message prompting for reflection
        st.info("Reflecting on past experiences helps you grow! Share your difficulties.")

    # --- Achievements Section ---
    # Display header for achievements section
    st.header("🏆 Celebrate Your Wins!")
    # Create text input for achievements
    achievement = st.text_input("Share something you've recently accomplished:")

    # Check if achievement is provided
    if achievement:
        # Display success message with achievement
        st.success(f"🎉 Amazing! You achieved: {achievement}")
    else:
        # Display info message prompting for achievements
        st.info("Big or small, every achievement counts! Share one now 😍")

    # --- Footer ---
    # Add horizontal line
    st.markdown("- - -")
    # Display motivational message
    st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
    # Display creator information
    st.write("**⛔ Created by Irshad Ulhaq**")

    # Embed a YouTube video
    st.video("https://www.youtube.com/watch?v=hiiEeMN7vbQ")

    # Create expandable section with growth mindset information
    with st.expander("Why Adopt a Growth Mindset?"):
        st.markdown("""
        - 🌟 **Embrace Challenges:** View obstacles as opportunities
        - 📖 **Learn from Mistakes:** Errors are chances to improve
        - 🔥 **Persist Through Difficulties:** Stay determined
        - 🎉 **Celebrate Effort:** Reward the process, not just results
        - 🤯 **Keep an Open Mind:** Stay curious and adaptable
        """)

# --- Mindset Quiz ---
elif page == "Mindset Quiz":
    # Display header for quiz page
    st.header("Growth Mindset Quiz")
    # Display quiz description
    st.write("Assess your current mindset and identify areas for growth")

    # Define quiz questions
    questions = [
        "Your intelligence is something you can't change very much.",
        "You can learn new things, but you can't really change how intelligent you are.",
        "No matter how much intelligence you have, you can always change it quite a bit.",
        "You can always substantially change how intelligent you are."
    ]

    # Initialize empty list for answers
    answers = []
    # Loop through questions and create radio buttons for each
    for i, question in enumerate(questions):
        answer = st.radio(question, ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], key=f"quiz_q{i}")
        answers.append(answer)

    # Create button to calculate score
    if st.button("Calculate Score"):
        # Calculate score based on answers (reverse scoring for first 2 questions)
        score = sum([4 - ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"].index(ans) if i < 2 else ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"].index(ans) for i, ans in enumerate(answers)])

        # Display score
        st.success(f"Your Growth Mindset Score: {score}/20")

        # Provide feedback based on score range
        if score < 10:
            st.warning("🔴 You lean more toward a Fixed Mindset. Keep working on embracing challenges!")
        elif score < 15:
            st.info("🟡 You have a Mixed Mindset. Focus on seeing challenges as opportunities!")
        else:
            st.success("🟢 You have a strong Growth Mindset! Keep up the great attitude!")

    # Create button to restart quiz
    if st.button("Restart Quiz"):
        st.rerun()

# --- Progress Tracker ---
elif page == "Progress Tracker":
    # Display header for progress tracker
    st.header("Progress Tracker")
    # Define CSV file name for storing progress data
    csv_file = "progress_data.csv"

    try:
        # Try to read existing data from CSV file
        df = pd.read_csv(csv_file, on_bad_lines='skip')  # Skip malformed lines
        # Clean column names by removing whitespace
        df.columns = df.columns.str.strip()
        # Convert column names to lowercase
        df.columns = df.columns.str.lower()
        # Rename columns to standard format
        df.rename(columns={"date": "Date", "mindset score": "Mindset Score", "notes": "Notes"}, inplace=True)

        # Display column names for debugging
        st.write("### CSV Columns:", df.columns.tolist())

    except FileNotFoundError:
        # Create empty DataFrame if file doesn't exist
        df = pd.DataFrame(columns=["Date", "Mindset Score", "Notes"])

    # If DataFrame is not empty
    if not df.empty:
        # Convert Date column to datetime format
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        # Check if Mindset Score column exists and display line chart
        if "Mindset Score" in df.columns:
            st.line_chart(df.set_index("Date")["Mindset Score"])

    # Create form for new entry
    with st.form("new_entry"):
        # Create slider for mindset score input
        new_score = st.slider("Current Mindset Score", 0, 20, 10)
        # Create text area for notes
        notes = st.text_area("Reflection Notes")

        # Check if form is submitted
        if st.form_submit_button("Save Entry"):
            # Create new DataFrame with entry data
            new_data = pd.DataFrame({
                "Date": [pd.Timestamp.today()],
                "Mindset Score": [new_score],
                "Notes": [notes]
            })
            # Append data to CSV file (with header only if file doesn't exist)
            new_data.to_csv(csv_file, mode='a', header=not os.path.exists(csv_file), index=False)

            # Display success message and refresh page
            st.success("✅ Entry saved successfully!")
            st.rerun()

# --- Resources ---
elif page == "Resources":
    # Display header for resources page
    st.header("Growth Mindset Resources")
    # Display description for resources page
    st.write("Browse books, videos, and articles to expand your mindset.")