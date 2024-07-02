# Write a function called find_words() that takes a string given a string s of consonants, and returnsa list of all the English words (from wordlist.txt) that have those consonants in that order, whenvowels (a, e, i, o, u) are excluded. There should be no other consonants in the word besides the onesin the input string. For instance, given bt, it would return bat, bit, boat, and abate, among other#
words."""
def find_words(s):
    vowels = set('aeiou')
    result = []
    
    with open('wordlist.txt', 'r') as f:
        wordlist = [line.strip().lower() for line in f]
    
    for word in wordlist:
        word_lower = word.lower()
        
        if all((c in s) for c in word_lower if c not in vowels):
            result.append(word)
    
    return result
