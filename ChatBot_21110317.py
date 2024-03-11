import re
import random

Archivo = open("Respuestas.txt", "w")
Archivo.write("\t\nChatTOL.ver.10/03/24\n")

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response 

def message_probability(user_message,recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty)/float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob 
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola', ['hola', 'klk', 'Saludos', 'Buenas'], single_response = True)
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('Espero todo este bien!!', ['Bien', 'mal', 'masomenos'], single_response = True)
        response('Fui creado ubicados en la calle Los patos, colonia los maestros, numero 1510', ['Al es tu ubicacion', 'Donde te creadon', 'donde'], single_response = True)
        response('El nombre de mi creador es Rubén Tolentino Alcalá', ['creo', 'Quien ', 'papas'], single_response = True)
        response('Fue un gusto ayudarte, necesitas algo mas?', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)
        response('De acuerdo, me alegro ayudarte!', ['No gracias', 'por ahora no', 'Es todo gracias', 'Seria'], single_response = True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match
    
def unknown():
    response = ['Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres', 'Preguntale a ChatGPT', 'Perdon, no entendi'][random.randrange(4)]
    return response

while True:
    user_input = input('\nUsuario(: ')
    print("\t\nChatTOL: " + get_response(user_input))
    Archivo = open("Respuestas.txt", "a")
    Archivo.write("\n-Usuario: " + user_input)
    Archivo.write("\n-ChatTOL:" + get_response(user_input))
    Archivo.close()