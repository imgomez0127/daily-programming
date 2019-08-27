class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        visited_websites = {}
        for domain in cpdomains:
            visit_count,address = domain.split()
            visit_count = int(visit_count)
            addresses = address.split(".")
            for i in range(len(addresses)):
                current_address = ".".join(addresses[i:])
                visited_websites[current_address] = visited_websites.get(current_address,0) + visit_count
        return [str(value) + " " + key for key,value in visited_websites.items()]
