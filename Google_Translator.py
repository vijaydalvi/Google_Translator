from googletrans import Translator
translator=Translator()
setence=input("Enter The Sentence:-")
to_language=input("To Language:-")
output=translator.translate(setence,dest=to_language)
print(output.text)