class Solution:
    def numberToWords(self, num: int) -> str:
        def processOneDigit(num):
            converter = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return converter.get(num)
        
        def processTwoDigitLessThanTwenty(num):
            converter = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return converter.get(num)
        
        def processTensDigit(num):
            converter = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return converter.get(num)
        
        def processTwoDigit(num):
            if not num:
                return ''
            elif num < 10:
                return processOneDigit(num)
            elif num < 20:
                return processTwoDigitLessThanTwenty(num)
            else:
                tensDigit = num // 10
                rest = num - (tensDigit * 10)
                return processTensDigit(tensDigit) + ' ' + processOneDigit(rest) if rest else processTensDigit(tensDigit)
            
        def processThreeDigit(num):
            hundredDigit = num // 100
            rest = num - (hundredDigit * 100)
            if hundredDigit and rest:
                return processOneDigit(hundredDigit) + ' Hundred ' + processTwoDigit(rest)
            elif not hundredDigit and rest:
                return processTwoDigit(rest)
            elif hundredDigit and not rest:
                return processOneDigit(hundredDigit) + ' Hundred'
        
        billion = num // 1000000000
        million = (num - (billion * 1000000000)) // 1000000
        thousand = (num - (billion * 1000000000) - (million * 1000000)) // 1000
        rest = num - (billion * 1000000000) - (million * 1000000) - (thousand * 1000)
        if not num:
            return 'Zero'
        result = ''
        if billion:
            result = processThreeDigit(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += processThreeDigit(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += processThreeDigit(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += processThreeDigit(rest)
        return result