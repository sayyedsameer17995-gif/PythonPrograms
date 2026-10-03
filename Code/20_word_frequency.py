def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


sentence = "python is easy and python is powerful"
print("Word frequency:", word_frequency(sentence))
