from googletrans import Translator
translator = Translator(service_urls=[
      'translate.google.co.jp',
    ])

        

# One simple function to handle the translation process
# text is a string get by the user, the "dest" is the language that translates the text to it
# and the "src" is what the language you translate from, it is "auto" but you can change it
def translate(text, dest="en", src="auto"):
    if not text:
        print("there is no text provided for translate")
        return
    try:
        trans = translator.translate(text, dest=dest, src=src)
        return trans.text
    # handle the errors 
    except TimeoutError:
        print("Timeout error, please check your internet connection")
        return None
    except Exception as error:
        print(f"An error occurred: {error}")
        return None

