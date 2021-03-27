class Solution:
    def validIPAddress(self, IP: str) -> str:
        def validateIPv4(IP):
            parts = IP.split('.')
            for part in parts:
                if len(part) not in [1, 2, 3]:
                    return 'Neither'
                if part[0] == '0' and len(part) != 1 or not part.isdigit() or int(part) > 255:
                    return 'Neither'
            return 'IPv4'
        def validateIPv6(IP):
            parts = IP.split(':')
            hexDigits = '0123456789abcdefABCDEF'
            for part in parts:
                if len(part) not in [1, 2, 3, 4] or not all(c in hexDigits for c in part):
                    return 'Neither'
            return 'IPv6'
        if IP.count('.') == 3:
            return validateIPv4(IP)
        elif IP.count(':') == 7:
            return validateIPv6(IP)
        else:
            return 'Neither'