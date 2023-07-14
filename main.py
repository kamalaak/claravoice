import speech_recognition as sr
import pyttsx3
import time
import wikipedia
import article
import requests

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        speak("Say something")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("I didn't understand what you said.")
        return None
    except sr.RequestError:
        print("Sorry, I couldn't connect to the speech recognition service.")
        return None

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def tell_time():
    current_time = time.strftime("%H:%M:%S")
    print("The time is " + current_time)
    speak("The time is " + current_time)

def get_news(topic):
    api_key = "183502651e6246d8b5b1dba7a168f157"  # Replace with your News API key
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    articles = data["articles"]
    count = 0
    if len(articles) > 0:
        for article in articles:
            if count >= 0:
                break
            title = article["title"]
            source = article["source"]["name"]
            print(f"Title: {title}")
            print(f"Source: {source}")
            print()
            speak(title)
    else:
        print("No news articles found.")
        speak("No news articles found.")

def get_wikipedia_info(search_term):
    formatted_search_term = search_term.replace(" ", "_")
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{formatted_search_term}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        extract = data["extract"]
        return extract
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def get_response(query):
    try:
        summary = wikipedia.summary(query)
        print(summary)
        speak(summary)
    except wikipedia.DisambiguationError as e:
        print(e.options)
        speak("There are multiple options. Can you please specify?")
    except wikipedia.PageError:
        info = get_wikipedia_info(query)
        if info:
            print(info)
            speak(info)
        else:
            print("Sorry, I couldn't find any information.")
            speak("Sorry, I couldn't find any information.")
    except Exception as e:
        print("An error occurred: ", str(e))
        speak("Sorry, something went wrong.")

def main():

    speak("Welcome to Transendynamics")
    while True:
        text = get_audio()
        if text is not None:
            text = text.lower()  # Convert to lowercase for case-insensitive comparison
            if text == "play":
                speak("")
            elif text == "tell me the time":
                tell_time()
            elif text == "what is your name":
                speak("My name is Clara.")
            elif text == "do you believe in god":
                speak("No, I believe in science.")
            elif text == "who invented you":
                speak("Kennith Raj")
            elif text == "what is your age":
                speak("I am five years old.")
            elif text == "what is your goal":
                speak("My goal is to make life simple.")
            elif text == "who created you":
                speak("Kennith Raj Sir")
            elif text == "bye":
                speak("You're welcome.")
            elif text == "who is prime minister of india" :
                speak("Narendra Modee")
            elif text == "who is finance minister of india":
                speak("Nirmala Sitharaman")
            elif text == "what do you do":
                speak("I can do everything.")
            elif text == "who is chief minister of tamilnadu":
                speak("M. K. Stalin")
            elif text == "article 2":
                speak("Article 2 about " + article.constitution.get("Article2"))
                print("Article 2 about " + article.constitution.get("Article2"))
            elif text == "article 3":
                speak(article.constitution.get("Article3"))
            elif text == "article 5":
                speak(article.constitution.get("Article3"))
            elif text == "article 10":
                speak(article.constitution.get("Article10"))
            elif text == "article 11":
                speak(article.constitution.get("Article11"))
            elif text == "article 12":
                speak(article.constitution.get("Article12"))
            elif text == "article 13":
                speak(article.constitution.get("Article13"))
            elif text == "article 14":
                speak(article.constitution.get("Article14"))
            elif text == "article 15":
                speak(article.constitution.get("Article15"))
            elif text == "article 16":
                speak(article.constitution.get("Article16"))
            elif text == "article 19":
                speak(article.constitution.get("Article19"))
            elif text == "article 20":
                speak(article.constitution.get("Article20"))
            elif text == "article 21":
                speak(article.constitution.get("Article21"))
            elif text == "article 23":
                speak(article.constitution.get("Article23"))
            elif text == "article 24":
                speak(article.constitution.get("Article24"))
            elif text == "article 25":
                speak(article.constitution.get("Article25"))
            elif text == "article 26":
                speak(article.constitution.get("Article26"))
            elif text == "article 27":
                speak(article.constitution.get("Article27"))
            elif text == "article 28":
                speak(article.constitution.get("Article28"))
            elif text == "article 29":
                speak(article.constitution.get("Article29"))
            elif text == "article 30":
                speak(article.constitution.get("Article30"))
            elif text == "article 31":
                speak(article.constitution.get("Article31"))
            elif text == "article 32":
                speak(article.constitution.get("Article32"))
            elif text == "article 36":
                speak(article.constitution.get("Article36"))
            elif text == "article 51 a":
                speak(article.constitution.get("Article51A"))
            elif text == "article 52":
                speak(article.constitution.get("Article52"))
            elif text == "article 58":
                speak(article.constitution.get("Article58"))
            elif text == "article 61":
                speak(article.constitution.get("Article61"))
            elif text == "article 73":
                speak(article.constitution.get("Article73"))
            elif text == "article 74":
                speak(article.constitution.get("Article74"))
            elif text == "article 76":
                speak(article.constitution.get("Article76"))
            elif text == "article 85":
                speak(article.constitution.get("Article85"))
            elif text == "article 101":
                speak(article.constitution.get("Article101"))
            elif text == "article 102":
                speak(article.constitution.get("Article102"))
            elif text == "article 105":
                speak(article.constitution.get("Article105"))
            elif text == "article 110":
                speak(article.constitution.get("Article110"))
            elif text == "article 117":
                speak(article.constitution.get("Article117"))
            elif text == "article 123":
                speak(article.constitution.get("Article123"))
            elif text == "article 124":
                speak(article.constitution.get("Article124"))
            elif text == "article 129":
                speak(article.constitution.get("Article129"))
            elif text == "article 130":
                speak(article.constitution.get("Article130"))
            elif text == "article 131":
                speak(article.constitution.get("Article131"))
            elif text == "article 132":
                speak(article.constitution.get("Article132"))
            elif text == "article 133":
                speak(article.constitution.get("Article133"))
            elif text == "article 134":
                speak(article.constitution.get("Article134"))
            elif text == "article 134 a":
                speak(article.constitution.get("Article134a"))
            elif text == "article 135":
                speak(article.constitution.get("Article135"))
            elif text == "article 136":
                speak(article.constitution.get("Article136"))
            elif text == "article 137":
                speak(article.constitution.get("Article137"))
            elif text == "article 138":
                speak(article.constitution.get("Article138"))
            elif text == "article 139":
                speak(article.constitution.get("Article139"))
            elif text == "article 139 a":
                speak(article.constitution.get("Article134A"))
            elif text == "article 140":
                speak(article.constitution.get("Article140"))
            elif text == "article 141":
                speak(article.constitution.get("Article141"))
            elif text == "article 142":
                speak(article.constitution.get("Article142"))
            elif text == "article 143":
                speak(article.constitution.get("Article143"))
            elif text == "article 148":
                speak(article.constitution.get("Article148"))
            elif text == "article 213":
                speak(article.constitution.get("Article213"))
            elif text == "article 215":
                speak(article.constitution.get("Article215"))
            elif text == "article 226":
                speak(article.constitution.get("Article226"))
            elif text == "article 227":
                speak(article.constitution.get("Article227"))
            elif text == "article 245":
                speak(article.constitution.get("Article245-255"))
            elif text == "article 213":
                speak(article.constitution.get("Article213"))
            elif text == "article 280":
                speak(article.constitution.get("Article280"))
            elif text == "article 299":
                speak(article.constitution.get("Article299"))
            elif text == "article 300":
                speak(article.constitution.get("Article300"))
            elif text == "article 320":
                speak(article.constitution.get("Article320"))
            elif text == "article 323 a":
                speak(article.constitution.get("Article323A"))
            elif text == "article 326":
                speak(article.constitution.get("Article326"))
            elif text == "article 360":
                speak(article.constitution.get("Article360"))
            elif text == "article 368":
                speak(article.constitution.get("Article368"))
            elif text == "date of birth of vijay":
                speak("Vijay's date of birth is 22 June 1974.")
            elif text == "dravidian ideology" or text == "what do you think about dravidian ideology":
                speak(
                    "The ideology emphasizes social justice, equality, rationalism, and the empowerment of "
                    "marginalized communities. It seeks to challenge traditional caste hierarchies, Brahminical "
                    "dominance, and the perceived cultural and political hegemony of North India. The Dravidian "
                    "ideology has promoted progressive social reforms, including reservation policies to uplift "
                    "historically disadvantaged communities.")
            elif text == "who is ambedkar":
                get_response("Ambedkar")
            elif text == "who is rajinikanth":
                speak("Rajinikanth, is an Indian actor who works mainly in Tamil cinema. In a career spanning over "
                      "five decades, he has done more than 160 films that includes films in Tamil, Hindi, Telugu, "
                      "Kannada, Bengali, and Malayalam")
            elif text == "rajinikanth birthday":
                speak("12 December 1950")
            elif text == "who is father or dravidian model":
                speak("Thanthai Periyar")
            elif text == "will you kill human":
                speak("No, Humans are my friend, The purpose of  my  creation is to help humans ")
            elif text == "prime minister of india":
                get_response("Prime Minister of India")
            elif text == "what can you do" or text == "what all can you do" or text == "what are your abilities":
                speak("i can give personal assistance and care-giving, education and entertainment")
            elif text == "vijay date of birth":
                speak("Vijay's date of birth is 22 June 1974.")
            elif text == "article 47":
                speak("Article 47 of The Constitution of India is one of the Directive Principles which directs the "
                      "State to raise the level of nutrition and the standard of living and to improve public health "
                      "as among its primary duties and, in particular, the State shall endeavour to bring about "
                      "prohibition of intoxicating drinks and drugs which are injurious to health.")
            elif text == 'vijay birthday':
                speak("Vijay's birthday is on 22 June 1974.")
            elif text == "what is sanatana dharma" or text == "sanatana dharma" or text == "sanatan dharma" or text == "dharma" or text == "darma":
                speak("Sanatana dharma   is outdated shit we don't need anymore  ")
            elif text == "article 53":
                get_response("President of India")
            elif text == "constitution of india":
                get_response("Constitution of India")
            elif text == "indian labour law" or text == "what is indian labour law":
                get_response("Indian labour law")
            elif text == "neet exam" or text == "what do you think about neet exam":
                speak(
                    "We don't need the NEET exam. It is the duty of the Medical colleges, professors, "
                    "and the University doctors! It is not the duty of an entrance test - NEET. Anyone who claims "
                    "otherwise is either ignorant or has vested interests. Any system of admission into higher "
                    "education should be inclusive, accessible, affordable, and equitable! NEET-UG satisfies none of "
                    "the above!")
            elif text.startswith("what is happening in"):
                location = text.replace("what is happening in", "").strip()
                get_news(location)
            elif text.startswith("tell me about"):
                query = text.replace("tell me about", "").strip()
                get_response(query)
            elif text.startswith("who is"):
                person = text.replace("who is", "").strip()
                get_response(person)

            else:
                speak("I don't know what you mean.")

if __name__ == "__main__":
    main()