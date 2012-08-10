import sys
import math

class InvalidWordError(Exception): pass
class RepetitionError(Exception): pass
class NoWordGivenError(Exception): pass

class convert():
    
    def __init__(self):
        self.temp = 0 #Stores temporary value of each unit in the word, eg: 'seven hundred' in seven hundred twenty one
	self.s = 0    #Resultant number
        self.key = {
	            'zero' : 0,
	            'one' : 1,
	            'two' : 2,
	            'three' : 3,
	            'four' : 4,
	            'five' : 5,
	            'six' : 6,
	            'seven' : 7,
	            'eight' : 8,
	            'nine' : 9,
	            'ten' : 10,
	            'eleven' : 11,
	            'twelve' : 12,
	            'thirteen' : 13,
	            'fourteen' : 14,
	            'fifteen' : 15,
	            'sixteen' : 16,
	            'seventeen' : 17,
	            'eighteen' : 18,
	            'nineteen' : 19,
	            'twenty' : 20,
	            'thirty' : 30,
	            'forty' : 40,
	            'fifty' : 50,
	            'sixty' : 60,
	            'seventy' : 70,
	            'eighty' : 80,
	            'ninety' : 90,
                  }

	self.hundreds = {
	                 'hundred' : 2,
			 'thousand' : 3,
			 'lakh' : 5,
			 'million' : 6,
			 'crore' : 7,
			 'billion' : 9,
			 'trillion' : 13,
			 'quadrillion' : 15,
			 'quintillion' : 18,
			 'sextillion' : 21,
			 'septillion' : 24,
			 'octillion' : 27,
			 'nonnillion' : 30,
			 'decillion' : 33,
			 'undecillion' : 36,
			 'duodecillion' : 39,
			 'tredecillion' : 42,
			 'quattuordecillion' : 45,
			 'quindecillion' : 48,
			 'sexdecillion' : 51,
			 'septendecillion' : 54,
			 'octodecillion' : 57,
			 'novemdecillion' : 60,
			 'vigintillion' : 63,
			 'unvigintillion' : 66,
			 'duovigintillion' : 69,
			 'tresvigintillion' : 72,
			 'quattuorvigintillion' : 75,
			 'quinquavigintillion' : 78,
			 'sesvigintillion' : 81,
			 'septemvigintillion' : 84,
			 'octovigintillion' : 87,
			 'novemvigintillion' : 90,
			 'trigintillion' : 93,
			 'untrigintillion' : 96,
			 'duotrigintillion' : 99,
			 'googol' : 100,
			 }

    def update(self):
        self.s += self.temp
	self.temp = 0
	return

    def con(self, word):
        check_list = []
        for w in word:
	    if w in self.hundreds:  
	        if w not in check_list:
	            check_list.append(w)
	        else:
		    raise RepetitionError, 'Word in the powers of 10 (%s) is repeated' % w #power of 10 is repeated; eg:three thousand and two thousand

        if 'and' in word:
	    del(word[word.index('and')])
        
	if word:
            self.temp = 0
	    for w in word:
	        w = w.lower()
	        if w in self.key:
	            self.temp += self.key[w]
	        elif w in self.hundreds:
	            if self.temp == 0:
		        self.temp = 1
		    self.temp = self.temp * pow(10, self.hundreds[w])
		    self.update()
		    
	        else:
	            raise InvalidWordError, 'Words does not define a number or check the spelling %s' %w #proper word not given
        
	    self.flag = 0
	    self.update()
	    print "Number: " + str(self.s)
	    s = self.s
	    self.s = 0
	    return s

	else:
	     raise NoWordGivenError, "Only 'and' given"

    def create(self, string):
        word = string.split(' ')
        s = self.con(word)
        return s

def main():
    if sys.argv[1:]:
        word = sys.argv[1:]
        obj = convert()
        obj.con(word)

    else:
        raise NoWordGivenError, "No word given to convert\nUsage: python <filename> <word>"

if __name__ == "__main__":
    main()
