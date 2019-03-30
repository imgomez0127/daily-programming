import re
class Solution:
    def checkIPv4(self,IP:str) -> str:
        ipv4 = IP.split(".")
        if(ipv4 != []):
            for part in ipv4:
                try:
                    if(int(part) > 255):
                        return False
                except:
                    return False
        return True
                
    def checkIPv6(self, IP:str) -> str:
        return False
    def validIPAddress(self, IP: str) -> str:
        if(self.checkIPv4(IP)):
            return "IPv4"
        if(self.checkIPv6(IP)):
            return "IPv6"
        return "Neither" 
if __name__ == "__main__":
    sol = Solution()
    sol.validIPAddress("172.16.254.1")
    sol.validIPAddress("172.16.254.01")
