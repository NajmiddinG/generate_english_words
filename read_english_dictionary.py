def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def get_words(words: str):
    words = words.lower()
    english_words = load_words()
    res = []
    for index, item in enumerate(english_words):
        can = bool(len(item)>2)
        for j in item:
            if j not in words:
                can = False
                break
        if can:
            check = True
            for i in item:
                if item.count(i)>words.count(i):
                    check = False
                    break
            if check:
                res.append(item)
        
    res.sort(key=lambda x:len(x))
    ans = ""
    i = 1
    for index, item in enumerate(res):
        ans+=f"{i} - {item}\n"
        i += 1
    return f"Harflar({ len(words) }) - { ' '.join(words) }\nSo'zlar({ i - 1 }):\n{ ans.strip() }"


# def load_words():
#     with open('words_alpha.txt') as word_file:
#         valid_words = set(word_file.read().split())

#     return valid_words

# res = []
# def dfs(word, remain):
#     if not remain and word not in res:
#         res.append(word)
#         return
#     if len(word)>2 and word not in res:
#         res.append(word)
#     for index, item in enumerate(remain):
#         dfs(word+item, remain[:index]+remain[index+1:])
         
# def get_words(words: str):
#     global res
#     words = words.lower()
#     words = list(words)
#     english_words = load_words()
#     dfs('', words)
#     res.sort(key=lambda x:len(x))
#     i = 1
#     ans = ""
#     for index, item in enumerate(res):
#         if item in english_words:
#             ans+=f"{i} - {item}\n"
#             i += 1
#     return f"Harflar({ len(words) }) - { ' '.join(words) }\nSo'zlar({ i - 1 }):\n{ ans.strip() }"
