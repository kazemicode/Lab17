# Lab 17 - CST 205
# Sara Kazemi


# Builds off of Lab 14, in which we built a frequency dictionary of unique words in Green Eggs and Ham
# And determined the most frequent word.
# In this lab, we create an HTML file and write the words in the frequency dictionary to that HTML file.
# My approach was to use the frequencies directly to influence the font size and the amount of greenness
# of each word in the frequency dictionary.
# I used scaling factors so that the most frequent word would have the maximum amount of greenness (or hexadecimal FF)
# The font size of each word is equivalent to its frequency plus 10 (for legibility)
# The most frequent word also gets highlighted in black

original_text = open('eggs.txt', 'r')
# Returns total word count found in the text
def word_count(text):
    count = 0
    for line in text:
        line = line.strip().split()  # strip of leading/trailing whitespace and put each word in list
        count += len(line)  # word count is simply the length of each list since elements are words found in line
    return count

# Finds all unique words in the text and adds them to the dictionary keys
# If found again, increments the count held in the key's corresponding value.
def get_unique_words(text):
    unique_words = {}
    for line in text:
        line = line.strip().lower().split()
        for word in line:
            if word not in unique_words:
                unique_words.update({word: 1})
            else:
                unique_words[word] = unique_words[word] + 1
    return unique_words

# Length of the dictionary is equivalent to the number of unique word in text
def unique_word_count(dict):
    return len(dict)

# Prints out unique words from the text in unsorted order
# with their counts.
def print_dictionary(dict):
    for key in dict:
        print(f'word: {key:10} | count: {dict[key]:10}')

# Prints out unique words from the text in alphabetical order
# with their counts.
def print_dict_alpha(dict):
    sorted_dict = sorted(dict)
    for word in sorted_dict:
        print(f'word: {word:10} | count: {dict[word]:10}')

# Find the larges value in the dictionary to get most frequent word
def get_most_frequent(dict):
    values=[]
    for value in dict.values():
        values.append(value)
    return max(values)

# Print out the most frequent word and its count
def get_most_freq_word(max, dict):
    for word in dict:
        if dict[word] == max:
            #print(f'\t*****MOST FREQUENT WORD*****\nword: {word:10} | count: {dict[word]:10}')
            return word

# Write words from story to HTML
# Font size (in pixels) is the frequency of the word plus 10 (so font is at least 11)
# Amount of greenness of the font is determined by frequency
def write_html(word_dict, html_file):
    most_freq = get_most_freq_word(get_most_frequent(word_dict), word_dict)
    html_file.write("<h1>Unique Words in <i>Green Eggs and Ham</i></h1>\n<h2>Size and greenness determined by word frequency</h2><hr>")
    for key in word_dict:
        factor = int(255/get_most_frequent(word_dict))  # Factor and additive are used to scale greenness
        additive = 255 % get_most_frequent(word_dict)   # so the word with max frequency will have the max greenness
        hex_val = '{:x}'.format(word_dict[key] * factor + additive) # Convert frequency * factor + additive to hex
        font_val = str(word_dict[key] + 10) # Makes the minimum font size 11
        if len(hex_val) == 1:   # if frequency in hex was a single digit, we need to adjust the hex value to two digits
            hex_val = str(0) + str(hex_val)
        else:
            hex_val = str(hex_val)
        if key == most_freq: # highlight the most frequent word in black
            html_file.write("<p  style=\"color:#33" + hex_val + "33; font-size:" + font_val + "px; background-color: black; font-family:monospace\">" + key + "</p>\n")
        else:
            html_file.write("<p style=\"color:#33" + hex_val + "33; font-size:" + font_val + "px; font-family:monospace\">" + key + "</p>\n")


dictionary = get_unique_words(original_text)
file = open("green.html", "wt")
write_html(dictionary, file)
original_text.close()