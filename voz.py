from gtts import gTTS
texto = input("Introduce el texto a convertir: ")
voz = gTTS(texto, lang='es-us')
voz.save("audio.mp3")
