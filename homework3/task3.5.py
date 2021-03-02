
def get_jokes(n):
    from random import randrange

    try:
        my_jokes = []
        nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
        adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
        adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        i = 1
        while n >= i:
            random_idx = randrange(len(nouns))
            random_idx1 = randrange(len(adverbs))
            random_idx2 = randrange(len(adjectives))
            word = nouns[random_idx]
            word1 = adverbs[random_idx1]
            word2 = adjectives[random_idx2]
            a = (f'{word}, {word1}, {word2}')
            my_jokes.append(a)
            if nouns.index(word) == nouns.index(word):
                nouns.pop(nouns.index(word))
            if adverbs.index(word1) == adverbs.index(word1):
                adverbs.pop(adverbs.index(word1))
            if adjectives.index(word2) == adjectives.index(word2):
                adjectives.pop(adjectives.index(word2))

            i += 1
    except IndentationError:
        "ошибка"
    except ValueError:
        "ошибка"


    # print(a, end= ' ')
    print(my_jokes)

get_jokes(9)