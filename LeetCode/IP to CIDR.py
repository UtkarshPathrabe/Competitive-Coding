class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        def IPtoInt(IP):
            result = 0
            for part in IP.split('.'):
                result = 256 * result + int(part)
            return result
        def InttoIP(x):
            return '.'.join(str((x >> i) % 256) for i in (24, 16, 8, 0))
        start, result = IPtoInt(ip), []
        while n:
            usable = max(1, (start & -start))
            while usable > n:
                usable >>= 1
            mask = int(32 - log(usable, 2))
            result.append(InttoIP(start) + '/' + str(mask))
            start += usable
            n -= usable
        return result