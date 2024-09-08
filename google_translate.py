from googletrans import Translator
translator = Translator(service_urls=[
      'translate.google.co.jp',
    ])

        

# one simple function to handle the translate process
# text is a string get by the user, the "dest" is the language that translate the text to it
# and the "src" is what is the language you translate from, its "auto" but you can change it
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

