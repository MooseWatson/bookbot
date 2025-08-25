def num_words(text):
    return len(text.split())

def character_count(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def char_sort(character_count):
    sorted_list =[]
    for char, count in character_count.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_list