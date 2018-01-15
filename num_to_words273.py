class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        until_nineteen = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        #print(len(until_nineteen))
        #print(until_nineteen[16])
        def words(n):
            if n < 20:
                return until_nineteen[n-1:n]
            if n < 100:
                return [tens[n//10 - 2]] + words(n%10)
            if n < 1000:
                return [until_nineteen[n//100-1]] + ['Hundred'] + words(n%100)
            for i, word in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(i+1):
                    return words(n//1000**i) + [word] + words(n%1000**i)
            
                
        return ' '.join(words(num)) or 'Zero'