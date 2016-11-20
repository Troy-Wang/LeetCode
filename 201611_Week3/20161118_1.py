"""
423. Reconstruct Original Digits from English
Given a non-empty string containing an out-of-order English representation of digits 0-9,
output the digits in ascending order.
"""


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        ret = ''
        for digit in s:
            dic.setdefault(digit, 0)
            dic[digit] += 1
        if 'z' in dic.keys() and dic['z']:
            ret += dic['z'] * '0'
            temp = dic['z']
            dic['z'] -= temp
            dic['e'] -= temp
            dic['r'] -= temp
            dic['o'] -= temp
        if 'w' in dic.keys() and dic['w']:
            ret += dic['w'] * '2'
            temp = dic['w']
            dic['t'] -= temp
            dic['w'] -= temp
            dic['o'] -= temp
        if 'x' in dic.keys() and dic['x']:
            ret += dic['x'] * '6'
            temp = dic['x']
            dic['s'] -= temp
            dic['i'] -= temp
            dic['x'] -= temp
        if 's' in dic.keys() and dic['s']:
            ret += dic['s'] * '7'
            temp = dic['s']
            dic['s'] -= temp
            dic['e'] -= 2 * temp
            dic['v'] -= temp
            dic['n'] -= temp
        if 'g' in dic.keys() and dic['g']:
            ret += dic['g'] * '8'
            temp = dic['g']
            dic['e'] -= temp
            dic['i'] -= temp
            dic['g'] -= temp
            dic['h'] -= temp
            dic['t'] -= temp
        if 'h' in dic.keys() and dic['h']:
            ret += dic['h'] * '3'
            temp = dic['h']
            dic['t'] -= temp
            dic['e'] -= 2 * temp
            dic['h'] -= temp
            dic['r'] -= temp
        if 'r' in dic.keys() and dic['r']:
            ret += dic['r'] * '4'
            temp = dic['r']
            dic['f'] -= temp
            dic['o'] -= temp
            dic['u'] -= temp
            dic['r'] -= temp
        if 'f' in dic.keys() and dic['f']:
            ret += dic['f'] * '5'
            temp = dic['f']
            dic['f'] -= temp
            dic['i'] -= temp
            dic['v'] -= temp
            dic['e'] -= temp
        if 'o' in dic.keys() and dic['o']:
            ret += dic['o'] * '1'
            temp = dic['o']
            dic['o'] -= temp
            dic['n'] -= temp
            dic['e'] -= temp
        if 'e' in dic.keys() and dic['e']:
            ret += dic['e'] * '9'
            temp = dic['e']
            dic['n'] -= 2 * temp
            dic['i'] -= temp
            dic['e'] -= temp
        return ''.join(sorted(list(ret)))


solution = Solution()
print(solution.originalDigits('owoztneoer'))
