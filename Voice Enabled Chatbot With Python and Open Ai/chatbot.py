import openai
import speech_recognition as sr

openai.api_key = "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"

def get_voice_input():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Listening...")
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
    return text

def get_response(input):
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt=input
)
    return response['choices'][0]['text']

if __name__ == "__main__":
    print("Chatbot: Hii user!! How may I help you?")
    
    user_input = get_voice_input()
    # if user_input == 'exit':
    #     break
    response = get_response(user_input)
    print(response)

########## ASSIGNMENT ########
#Get response from chatbot as voice