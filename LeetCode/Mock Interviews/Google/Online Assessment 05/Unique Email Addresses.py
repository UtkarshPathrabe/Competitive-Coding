class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def formatEmail(email):
            emailParts = email.split('@')
            emailParts[0] = emailParts[0].replace('.', '')
            return emailParts[0].split('+')[0] + '@' + emailParts[1]
        emailsSet = set()
        for email in emails:
            emailsSet.add(formatEmail(email))
        return len(emailsSet)