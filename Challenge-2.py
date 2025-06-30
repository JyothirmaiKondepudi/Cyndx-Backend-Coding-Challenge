from collections import defaultdict
def analyze_anagrams(words):
    d = defaultdict(list)
    
    for word in words:
        counter = [0]*26
        for letter in word:
            i = letter.lower()
            index = ord(i) - ord('a')
            counter[index]+=1
        d[tuple(counter)].append(word)
    return d
words = ["listen", "silent", "hello", "bored", "robed", "study", "dusty", "THE", "HET"]
d = analyze_anagrams(words)
res = {
    "largest_group":max(d.values(), key =len),
    "total_groups":len(d)
       }
anagramGroups = list(d.values())
print(res)
print(anagramGroups)