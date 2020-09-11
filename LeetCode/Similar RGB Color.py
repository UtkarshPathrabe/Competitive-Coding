class Solution:
    def similarRGB(self, color: str) -> str:
        def similar(hexNumber):
            q, r = divmod(int(hexNumber, 16), 17)
            if r > 8:
                q += 1
            return '{:02x}'.format(17 * q)
        return '#' + similar(color[1:3]) + similar(color[3:5]) + similar(color[5:])