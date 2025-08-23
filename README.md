
AI Symptom Checker 🤖🩺

A conversational chatbot for quick, AI-powered health advice. Built with Streamlit, this tool empowers users to check everyday symptoms and get basic guidance—helping support the Sustainable Development Goal (SDG) 3: Good Health & Well-being.
🚀 Features

    Conversational AI medical assistant (not a substitute for real doctors!)

    Map-based “Find Nearby Doctors” (with location detection)

    Multiple languages (easy to extend)

    Completely open source and easy to deploy

    Trust & privacy first: No user data stored

🛠️ Setup & Running

1. Clone this repository:

bash
git clone https://github.com/your-username/global_ai_hackathon.git
cd ai-symptom-checker
video link :- https://drive.google.com/file/d/1tMVB3QxvHSQ6u8OPvPiPzlSGB54-yKEe/view?usp=sharing
2. Install dependencies:

bash
pip install streamlit streamlit-folium folium streamlit-geolocation google-generativeai

3. Get your Google Generative AI API key!

    Sign in, create a key, and copy it.

4. Add your API key

    Open app.py

    Paste your API key in the api_key = "..." line

5. Run the app:

bash
streamlit run app.py

The app opens in your browser at http://localhost:8501.
🧪 Sample Conversations
User input	AI Response (suggestion)
fever	Advice: A fever is a common sign of infection. Rest and drink plenty of fluids. If your fever is very high or persists for more than a few days, you should see a doctor.
Care Level: Non-urgent
I have a bad cough and a headache	Advice: A cough can be caused by many things, from a common cold to more serious conditions. If your cough is severe, persistent, or you are coughing up blood, seek medical attention.
Care Level: Non-urgent
chest pain	Advice: Chest pain can have many causes, some of which are serious. If you are experiencing sudden, severe chest pain, especially with other symptoms like shortness of breath, pain in your arms, back, neck, jaw or stomach, you should seek emergency medical care immediately.
Care Level: Emergency
🗺️ Find Doctors Near You

    Click “Find Nearby Doctors” in the sidebar

    Allow browser location access

    See your position on the map (future: list of actual doctors nearby — see Improvements)

⚠️ Ethical Use & Limitations

    Important:
    This tool is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment.

    Always consult a qualified health provider about your symptoms.

    Never ignore or delay seeking medical advice based on AI output.

    The chatbot cannot diagnose or manage emergencies.

    AI responses are based on general symptom patterns and public health sources.

🌟 Suggestions for Enhancement

    Use a more advanced model: Integrate the latest Gemini/GPT or domain-specific healthcare models.

    Show real nearby doctors: With APIs like Google Places or Foursquare.

    Multiple language support: Make the interface and chatbot advice available in more than English and Spanish.

    User accounts: Personalize experience, show symptom history, optionally enable reminders.

    Connect to online healthcare: Allow video calls with professionals or online booking.

📢 Contributing

Pull requests & ideas are welcome! Open an issue for discussion.
📄 License

MIT License – use, modify, and share freely.
🙏 Acknowledgments

    Streamlit

    Google Generative AI (Gemini)

    Unsplash / GIPHY for demo GIFs

Stay healthy. AI can help — but doctors save lives.
