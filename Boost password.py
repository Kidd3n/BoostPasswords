import re, random, string, base64, time

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + '!@#$%^&*'
    return ''.join(random.choice(characters) for _ in range(length))

def is_password_secure(password):
    if len(password) < 8:
        return False
    
    if not any(c.isupper() for c in password) and not any(c.isdigit() for c in password):
        return False
    
    return True

MIN_PASSWORD_LENGTH = 8
RANDOM_INITIAL_LENGTH = 2
RANDOM_END_LENGTH = 3

while True:
    user_input = input("\nContraseña (Min 8 Caracteres): ") #Password (Min 8 Characters)
    
    if len(user_input) < MIN_PASSWORD_LENGTH:
        print("\n[!] La contraseña o frase debe tener al menos 8 caracteres.") #The password or phrase must be at least 8 characters long.
        continue
    
    random_prefix = generate_random_password(RANDOM_INITIAL_LENGTH)
    random_suffix = generate_random_password(RANDOM_END_LENGTH)
    generated_password = random_prefix + user_input + random_suffix
    password64 = base64.b64encode(generated_password.encode()).decode()

    if is_password_secure(generated_password):
        print(f"\n[+] Contraseña Segura Encriptada: {password64}\n") #Secure encrypted password
        time.sleep(1.5)
        print("¿Quieres ver la contraseña desencriptada? ") # Do you want to see the decrypted password?
        if input("1) Si (Recomendado) \n2) No \n?): ").strip().lower() == "1": #1) Yes (Recommended) 2) No
            decrypted_password = base64.b64decode(password64).decode()
            print(f"\n[+] Contraseña Segura Desencriptada: {decrypted_password}\n") #Secure decrypted password
        break
        
    else:
        print("\n[?] Se ha producido un problema al crear la contraseña segura, inténtelo de nuevo..\n") #There was a problem creating the secure password, please try again





