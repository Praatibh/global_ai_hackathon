import streamlit as st
import folium
from streamlit_folium import st_folium
import google.generativeai as genai
from streamlit_geolocation import streamlit_geolocation
import os

def get_ai_response(api_key, prompt, lang):
    """
    Gets a response from the generative AI model.
    """
    try:
        genai.configure(api_key=api_key)
        # Replace with the exact string for your supported model (from list_models output)
        model = genai.GenerativeModel("models/gemini-2.5-pro")

        full_prompt = f"""
        You are an AI medical assistant. Analyze the following symptoms and provide advice.
        The user's language is: {lang}. Your response should be in the same language.
        Symptoms: "{prompt}"

        Provide two things in your response, clearly separated:
        1. **Advice:** A helpful, conversational explanation of what the symptoms could mean and what to do next.
        2. **Care Level:** Classify the situation as one of the following: 'Non-urgent', 'Urgent', or 'Emergency'.

        IMPORTANT: Start your response with a clear disclaimer that you are an AI and not a medical professional, and the user should consult a doctor for any health concerns.
        """

        response = model.generate_content(full_prompt)
        # Try both .text and the candidates/parts structure, depending on SDK version
        if hasattr(response, "text"):
            return response.text
        elif hasattr(response, "candidates") and response.candidates:
            return response.candidates[0].content.parts.text
        else:
            return "No response generated."
    except Exception as e:
        return f"An error occurred: {e}. Please ensure your API key and model name are valid."

def main():
    st.sidebar.title("Options")

    # Hardcoded API key - replace with your actual key!
    api_key = os.environ["api_key"]

    lang = st.sidebar.selectbox("Language", ["en", "es"])

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    def ask_example(question):
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)

        with st.spinner("The AI is thinking..."):
            response = get_ai_response(api_key, question, lang)

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

    if st.sidebar.button("I have a headache and a fever."):
        ask_example("I have a headache and a fever.")
    if st.sidebar.button("I have a sore throat and a cough."):
        ask_example("I have a sore throat and a cough.")
    if st.sidebar.button("I have a rash on my arm."):
        ask_example("I have a rash on my arm.")

    st.title("AI Symptom Checker")
    st.write("This tool is for informational purposes only and is not a substitute for professional medical advice.")

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Enter your symptoms here..."):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.spinner("The AI is thinking..."):
            response = get_ai_response(api_key, prompt, lang)

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

    if st.sidebar.button("Find Nearby Doctors"):

        # Get location only once and store in session_state
        if "user_location" not in st.session_state:
            location = streamlit_geolocation()

            if location and location.get("latitude") and location.get("longitude"):
                st.session_state.user_location = location
            else:
                st.session_state.user_location = None

        # Use stored location if available
        location = st.session_state.user_location

        if location:
            user_lat = location["latitude"]
            user_lon = location["longitude"]
            st.info(f"Displaying a map with your location.")
        else:
            user_lat, user_lon = 40.7128, -74.0060  # Default NYC location
            st.info("Could not fetch location. Showing default location.")

        m = folium.Map(location=[user_lat, user_lon], zoom_start=12)
        folium.Marker([user_lat, user_lon], popup="Your Location" if location else "Default Location",
                    tooltip="Your Location" if location else "Default Location").add_to(m)
        st_folium(m, width=700, height=500)



if __name__ == "__main__":
    main()
