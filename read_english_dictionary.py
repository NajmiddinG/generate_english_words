def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

res = set()
def dfs(word, remain):
    if not remain:
        res.add(word)
        return
    if len(word)>=3:
        res.add(word)
    for index, item in enumerate(remain):
        dfs(word+item, remain[:index]+remain[index+1:])
         
def get_words(words: str):
    words = words.lower()
    words = list(words)
    english_words = load_words()
    dfs('', words)
    res = list(res)
    res.sort(key=lambda x:len(x))
    i = 1
    ans = ""
    for index, item in enumerate(res):
        if item in english_words:
            ans+=f"{i} - {item}\n"
            i += 1
    return f"Harflar({ len(words) }) - { ' '.join(words) }\nSo'zlar({ i - 1 }):\n{ ans.strip() }"
