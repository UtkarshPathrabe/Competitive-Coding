class Solution:
    def entityParser(self, text: str) -> str:
        PARSER_MAP = {
            "&quot;": '"',
            "&apos;":"'",
            "&gt;":">",
            "&lt;":"<",
            "&frasl;":"/",
            "&amp;":"&"
        }
        for key in PARSER_MAP:
            if key in text:
                text = text.replace(key, PARSER_MAP[key])
        return text