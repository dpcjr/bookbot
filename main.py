def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents


def word_count(words):
    total_words = words.split()
    return len(total_words)        

def character_count(characters):
    total_characters = {}
    lowered_text = characters.lower()
    for char in lowered_text:
        if char.isalpha():
            if char in total_characters:
                total_characters[char] += 1
            else:
                total_characters[char] = 1
    return total_characters

def sort_on(dict):
    return dict["count"]

def get_sorted_chars(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)
    return char_list



if __name__ == "__main__":
    contents = main()
    word_total = word_count(contents)
    character_total = character_count(contents)
    sorted_chars = get_sorted_chars(character_total)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_total} words found in the document\n")

    for char_dict in sorted_chars:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")

    print("--- End report ---")

    


    