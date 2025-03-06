import streamlit as st
import random
import time
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Drink Dress", page_icon="☕", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #6F4E37;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #4B382A;
        color: white;
    }
    .stSelectbox>div>div>div {
        background-color: #6F4E37;
        color: white;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #4B382A;
        text-align: center;
    }
    .stApp {
        background-color: #D2B38C;
    }
    .welcome-title {
        font-size: 48px;
        font-weight: bold;
        color: #4B382A;
        text-align: center;
    }
    .welcome-subtitle {
        font-size: 24px;
        color: #4B382A;
        text-align: center;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

class DrinkDressApp:
    def __init__(self):
        if "selected_answers" not in st.session_state:
            st.session_state.selected_answers = {}
        if "selected_drink" not in st.session_state:
            st.session_state.selected_drink = None
        if "selected_size" not in st.session_state:
            st.session_state.selected_size = None
        if "screen" not in st.session_state:
            st.session_state.screen = "welcome"
        if "beverage_options" not in st.session_state:
            st.session_state.beverage_options = []
        if "heart_rate" not in st.session_state:
            st.session_state.heart_rate = None
        if "user_name" not in st.session_state:
            st.session_state.user_name = ""  # To store the user's name

    def welcome_screen(self):
        st.markdown('<div class="welcome-title">Drink Dress</div>', unsafe_allow_html=True)
        st.markdown('<div class="welcome-subtitle">Your Perfect Brew, Tailored Just For You</div>', unsafe_allow_html=True)
        st.markdown("---")  # This is the line

        # Use columns to center the button horizontally
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            pass  # Empty column for spacing
        with col2:
            pass  # Empty column for spacing
        with col4:
            pass  # Empty column for spacing
        with col5:
            pass  # Empty column for spacing
        with col3:
            if st.button("Touch to get started"):
                st.session_state.screen = "questions"
                st.rerun()

    def show_questions(self):
        st.title("Customize Your Preferences")
        st.markdown("---")

        questions = [
            ("How are you feeling today?", ["", "Relaxed", "Energetic", "Stressed", "Neutral"]),
            ("What kind of vibe are you looking for in your drink?", ["", "Calm and soothing", "Refreshing and invigorating", "Sweet and indulgent", "Neutral and balanced"]),
            ("How does the weather affect your drink choice?", ["", "It doesn’t affect my choice", "I prefer drinks suited to the season"]),
            ("Do you prefer a drink that matches or changes your mood?", ["", "Matches my mood", "Changes my mood", "Neutral preference"]),
            ("What’s your energy level like right now?", ["", "Low", "Moderate", "High", "I want to stay at my current level"]),
            ("What level of sweetness do you prefer?", ["", "Not sweet at all","Mildly sweet","Moderately sweet","Very sweet"]),
            ("What kind of flavor profile are you in the mood for?",["", "Fruity","Creamy","Nutty","Herbal or spicy"]),
            ("What's your preferred drink temperature?",["", "Hot","Warm","Cold","I don't mind"]),
            ("Do you enjoy any of the following textures in your drink?",["", "Smooth and creamy","Plain liquid"]),
            ("Do you have a preference for caffeine content?",["", "Decaffeinated","Low caffeine","Moderate caffeine","High caffeine"])
        ]

        for question, options in questions:
            st.session_state.selected_answers[question] = st.selectbox(question, options, index=options.index(st.session_state.selected_answers.get(question, "")))

        if st.button("Submit"):
            st.session_state.screen = "biometric"
            st.rerun()

    def show_biometric_screen(self):
        st.title("Biometric Scanner")
        st.markdown("---")

        st.write("Please place your fingers on the sensors.")

        if st.button("Start Scanning"):
            st.session_state.screen = "countdown"
            st.rerun()

        if st.button("Skip Biometric"):
            st.session_state.screen = "beverage_selection"
            st.rerun()

    def show_countdown(self):
        st.title("Get Ready to Scan")
        st.markdown("---")

        st.write("Position your index and middle fingers on the sensors. Scanning will begin in:")

        # 3-second countdown
        countdown_duration = 5  # Change this value to adjust the countdown duration
        countdown_text = st.empty()

        for i in range(countdown_duration, 0, -1):
            countdown_text.write(f"**{i}**")
            time.sleep(1)

        # After countdown, proceed to scanning
        st.session_state.screen = "scanning"
        st.rerun()

    def show_scanning_screen(self):
        st.title("Scanning...")
        st.markdown("---")

        st.write("Please keep your fingers on the sensors. This will take about 10 seconds.")

        # Simulate scanning for 10 seconds (you can change this value)
        loading_duration = 10  # Change this value to adjust the loading duration
        progress_bar = st.progress(0)
        status_text = st.empty()

        for i in range(loading_duration):
            time.sleep(1)
            progress_bar.progress((i + 1) / loading_duration)
            status_text.text(f"Scanning in progress... {loading_duration - i - 1} seconds remaining")

        # Generate a random heart rate between 60 and 100
        st.session_state.heart_rate = random.randint(60, 100)
        st.session_state.screen = "scanning_results"
        st.rerun()

    def show_scanning_results(self):
        st.title("Scanning Results")
        st.markdown("---")

        st.write(f"Heart rate: **{st.session_state.heart_rate} bpm**")

        if st.button("Continue to Beverage Selection"):
            st.session_state.screen = "beverage_selection"
            st.rerun()

    def show_beverage_selection(self):
        st.title("Choose Your Beverage")
        st.markdown("---")

        beverages = [
            {"name": "Yemeni Mocha Delight", "ingredients": "Dark chocolate, Yemeni coffee, milk", "temp": "Warm", "price": "$5.00", "image": "yemani.png"},
            {"name": "Spiced Qishr Latte", "ingredients": "Yemeni coffee husk, ginger, cinnamon", "temp": "Cold", "price": "$5.50", "image": "latte.png"},
            {"name": "Honey Cardamom Cold Brew", "ingredients": "Yemeni coffee, honey, cardamom", "temp": "Cold", "price": "$4.99", "image": "honey.png"},
            {"name": "Rose Almond Cappuccino", "ingredients": "Almond milk, rose syrup, Yemeni coffee", "temp": "Warm", "price": "$5.50", "image": "rose.png"},
            {"name": "Saffron Pistachio Latte", "ingredients": "Yemeni coffee, saffron, pistachio syrup", "temp": "Cold", "price": "$6.00", "image": "pist.png"}
        ]

        if not st.session_state.beverage_options:
            st.session_state.beverage_options = random.sample(beverages, 3)

        for drink in st.session_state.beverage_options:
            st.subheader(drink["name"])
            # Display drink image
            try:
                st.image(drink["image"], width=200)  # Adjust width as needed
            except FileNotFoundError:
                st.error(f"Image for {drink['name']} not found. Please ensure '{drink['image']}' is in the correct directory.")
            st.write(f"Ingredients: {drink['ingredients']}")
            st.write(f"Temperature: {drink['temp']}")
            st.write(f"Price: {drink['price']}")
            if st.button(f"Select {drink['name']}"):
                st.session_state.selected_drink = drink
                st.session_state.screen = "size_selection"
                st.rerun()

    def show_size_selection(self):
        st.title("Choose Your Drink Size")
        st.markdown("---")

        if st.session_state.selected_drink:
            st.subheader(st.session_state.selected_drink["name"])
            st.write(f"Ingredients: {st.session_state.selected_drink['ingredients']}")
            st.write(f"Temperature: {st.session_state.selected_drink['temp']}")
            st.write(f"Price: {st.session_state.selected_drink['price']}")

            st.subheader("Choose your drink size")
            size = st.radio("Size", ["12oz", "16oz"], index=0 if st.session_state.selected_size is None else ["12oz", "16oz"].index(st.session_state.selected_size))
            st.session_state.selected_size = size

            base_price = float(st.session_state.selected_drink["price"].strip("$"))
            size_multiplier = {"12oz": 1.0, "16oz": 1.5}
            final_price = base_price * size_multiplier[st.session_state.selected_size]
            st.write(f"Price: ${final_price:.2f}")

            # Collect the user's name
            st.session_state.user_name = st.text_input("Please enter your name:")

            if st.button("Place order"):
                if st.session_state.user_name.strip() == "":
                    st.error("Please enter your name before placing the order.")
                else:
                    st.success(f"Thank you, {st.session_state.user_name}! Your {st.session_state.selected_size} {st.session_state.selected_drink['name']} is being prepared. Please continue to the checkout counter to complete the transaction.")
                    if st.button("Start New Order"):
                        # Reset session state and restart the app
                        st.session_state.clear()
                        st.session_state.screen = "welcome"
                        st.rerun()

def main():
    app = DrinkDressApp()

    if st.session_state.screen == "welcome":
        app.welcome_screen()
    elif st.session_state.screen == "questions":
        app.show_questions()
    elif st.session_state.screen == "biometric":
        app.show_biometric_screen()
    elif st.session_state.screen == "countdown":
        app.show_countdown()
    elif st.session_state.screen == "scanning":
        app.show_scanning_screen()
    elif st.session_state.screen == "scanning_results":
        app.show_scanning_results()
    elif st.session_state.screen == "beverage_selection":
        app.show_beverage_selection()
    elif st.session_state.screen == "size_selection":
        app.show_size_selection()

if __name__ == "__main__":
    main()
