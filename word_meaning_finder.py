import pyttsx3
from nltk.corpus import wordnet


class Speaking:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

    def speak(self, audio):
        # Just queue the audio to speak, don't run yet
        self.engine.say(audio)

    def run(self):
        # Run all queued speeches now
        self.engine.runAndWait()


class DictionaryApp:
    def __init__(self):
        self.speaker = Speaking()

    def get_meanings(self, word):
        synsets = wordnet.synsets(word)
        if not synsets:
            return None

        meanings = []
        for syn in synsets:
            meaning = syn.definition()
            if meaning not in meanings:
                meanings.append(meaning)
        return meanings

    def run(self):
        self.speaker.speak("Please enter a word to find its meaning.")
        self.speaker.run()  # Speak prompt first, then get input

        query = input("Enter a word to find its meaning: ").strip()

        meanings = self.get_meanings(query)

        if not meanings:
            self.speaker.speak("Sorry, I couldn't find the meaning of the word.")
            self.speaker.run()
            print("No meaning found.")
            return

        self.speaker.speak(f"Here are the meanings of {query}.")
        for meaning in meanings:
            print(meaning)
            self.speaker.speak(meaning)

        self.speaker.run()  # Run all queued speeches for the meanings


if __name__ == '__main__':
    app = DictionaryApp()
    app.run()
