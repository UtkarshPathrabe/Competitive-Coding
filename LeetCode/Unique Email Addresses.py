class Solution:
    def getFormattedEMail(self, email):
        userName, domain = email.split('@')
        if '+' in userName:
            userName = userName.split('+')[0]
        if '.' in userName:
            userName = ''.join(userName.split('.'))
        return userName + '@' + domain
    
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailsSet = set()
        for email in emails:
            emailsSet.add(self.getFormattedEMail(email))
        return len(emailsSet)