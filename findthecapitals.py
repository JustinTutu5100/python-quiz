#Complete the method that takes a sequence of objects with two keys each: country or state, and capital. Keys may be symbols or strings.
#The method should return an array of sentences declaring the state or country and its capital.
def capital(capitals):
    
    sentences = []
    
    for item in capitals:
        state = item.get('state') or item.get('country')
        capital = item.get('capital')
        
        sentences.append(f"The capital of {state} is {capital}")
        
    return sentences