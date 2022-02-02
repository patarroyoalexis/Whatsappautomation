import pywhatkit
try:
    pywhatkit.sendwhatmsg("+573102429874","Mensaje desde Python",23,54, 15, True, 2)
    print("Mensaje enviado")

except:
    print("Ocurrio un Error")