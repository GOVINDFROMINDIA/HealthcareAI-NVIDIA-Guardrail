import google.generativeai as genai

genai.configure(api_key="AIzaSyDlXx9osW1GrSz16rW62lQlirfu-ouEQq4")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
convo = model.start_chat(history=[])

print("Chat with the AI model. Type 'QUIT' to exit.")

while True:
    user_input = input("You: ")
    
    if user_input.upper() == "QUIT":
        print("Exiting the chat. Goodbye!")
        break
    
    response = convo.send_message(user_input)
    print("AI:", response.text)