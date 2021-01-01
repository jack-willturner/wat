class TrieNode():
    def __init__(self, char=None, children={}, leaf=False):
        self.char = char
        self.children = {} # self.children = children doesn't work
        self.leaf = leaf
    
class Trie():
    def __init__(self, root):
        self.root = root
        
    def insert(self, word):
        cur = self.root
        for i, char in enumerate(word):   
            nx = cur.children.get(char, None) 
            
            if nx is None:
                nx = TrieNode(char, leaf=(i==len(word)-1))
                cur.children[char] = nx 
                
            cur = nx 
    
    def search(self, word):
        cur = self.root
        for i, char in enumerate(word):
            nx = cur.children.get(char, None)
            print(char, nx)
            if nx is None:
                return False
            else:
                if i == len(word)-1 and nx.leaf:
                    return True
                cur = nx
                
words = ['dog','deer','deal']
root = TrieNode()
trie = Trie(root)

for word in words:
    trie.insert(word)
    
trie.search('dear') == True
