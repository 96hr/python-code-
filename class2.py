from string import punctuation

class Analyzer:
    def __init__(self, s):
      
        for c in punctuation:
            s = s.replace(c, '')
  
        s = s.lower()
        self.words = s.split()
    
    def number_of_words(self):
        return len(self.words)
    
    def starts_with(self, s):
        return len([w for w in self.words if w.startswith(s)])
    
    def number_with_length(self, n):
        return len([w for w in self.words if len(w) == n])

s = 'this is a test of class.'
analyzer = Analyzer(s)
print(analyzer.words)
print('Number of words:', analyzer.number_of_words())
print('Number of words starting with "t":', analyzer.starts_with('t'))
print('Number of two-letter words:', analyzer.number_with_length(2))
