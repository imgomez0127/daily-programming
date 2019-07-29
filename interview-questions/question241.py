"""
    This question was asked by Palantir:
    calculate the h-index of given a list of 
    respective citations
"""
def compute_h_index(citation_list):
    h_index = 0
    for i in range(len(citation_list)):
        eligable_papers = 0
        for citation_count in citation_list:
            if citation_count >= i+1:
                eligable_papers += 1
        if(eligable_papers >= i+1):
            h_index = i+1
    return h_index

if __name__ == "__main__":
    citation_list = [33,30,20,15,7,6,5,4]
    print(compute_h_index(citation_list))
