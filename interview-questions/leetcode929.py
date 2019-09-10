class Solution:
    def numUniqueEmails(self, emails):
        emails = [email.split("@") for email in emails] 
        email_set = set()
        for email in emails:
            stripped_local_name = ""
            for char in email[0]:
                if char == "+":
                    break
                elif char == ".":
                    continue
                stripped_local_name += char
            email_set.add(stripped_local_name+"@"+email[1])
        return len(email_set)

print(Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
