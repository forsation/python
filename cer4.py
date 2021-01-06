def greet(lg):
    if lg == 'es':
        return "Hola Afiz"
    elif lg == 'en':
        return "hello"
    else :
        return "bonjour"
    
lg = input('where are u from : ')     
print(greet(lg))