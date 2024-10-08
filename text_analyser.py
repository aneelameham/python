def analyze_text(text):
    text = text.strip()
    num_characters = len(text)

    words = text.split()
    num_words = len(words)

    sentences = [s for s in text.split('.') if s]
    num_sentences = len(sentences)

    word_frequency = {}
    for word in words:
        word = word.lower().strip(",.!?\"'")
        if word:
            word_frequency[word] = word_frequency.get(word, 0) + 1

    most_frequent_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:5]

    avg_word_length = sum(len(word) for word in words) / num_words if num_words > 0 else 0

    avg_sentence_length = num_words / num_sentences if num_sentences > 0 else 0

    return {
        'num_characters': num_characters,
        'num_words': num_words,
        'num_sentences': num_sentences,
        'most_frequent_words': most_frequent_words,
        'avg_word_length': avg_word_length,
        'avg_sentence_length': avg_sentence_length
    }


def main():
    # Prompt for user input
    user_input = input("Please enter some text: ")

    # Analyze the text
    stats = analyze_text(user_input)

    # Display results
    print("\nText Analysis Results:")
    print(f"Number of characters: {stats['num_characters']}")
    print(f"Number of words: {stats['num_words']}")
    print(f"Number of sentences: {stats['num_sentences']}")
    print(f"Most frequent words: {stats['most_frequent_words']}")
    print(f"Average word length: {stats['avg_word_length']:.2f}")
    print(f"Average sentence length: {stats['avg_sentence_length']:.2f} words")


if __name__ == "__main__":
    main()

#Common frogs metamorphose through three distinct developmental life stages - aquatic larva, terrestrial juvenile, and adult. They have corpulent bodies with a rounded snout, webbed feet and long hind legs adapted for swimming in water and hopping on land. Common frogs are often confused with the common toad (Bufo bufo), but frogs can easily be distinguished as they have longer legs, hop, and have a moist skin, whereas toads crawl and have a dry 'warty' skin. The spawn of the two species also differs, in that frog spawn is laid in clumps and toad spawn is laid in long strings.