#https://replit.com/join/uasonqrsbx-jacob-olafolaf
tex=str(input("Para activar a Alexa, di Alexa: "))
tex.count("Alexa")
if tex.count("Alexa")==1:
  print("¿Dime, cómo puedo ayudarte?")
elif tex.count("Alexa")>1:
  print("¡Tranquilo, solo di mi nombre una vez!")
