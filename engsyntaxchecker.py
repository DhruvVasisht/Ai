def is_capitalized(sentence):
    return sentence[0].isupper()

def ends_with_punctuation(sentence):
    return sentence[-1] in ['.', '?', '!']
def grammar_check(sentence):
    if not is_capitalized(sentence):
        print("Error: Sentence should start with a capital letter.")
        return False
    if not ends_with_punctuation(sentence):
        print("Error: Sentence should end with a period, question mark, or exclamation mark.")
        return False
    return True

while True:
  
    user_sentence = input("Enter a sentence (type 'end' to finish): ")

  
    if user_sentence.lower() == 'end':
        break


    if grammar_check(user_sentence):
        print("Grammar is correct.")
    else:
        print("Grammar error(s) found.")