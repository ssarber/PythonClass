#!/usr/local/bin/python3
print('Content-type: text/html\n')
# coding: utf-8

def get_numbers_from_file(file_name):

    # file_one = 'speeches/abraham_lincoln_1st.txt'
    speeches_file = open(file_name);

    stop_words = open('stop_words.txt')
    # stop_words = stop_words.read().split("\n")
    stop_words = re.split(r'\W+',stop_words.read())

    lines = speeches_file.read().split("\n")
    line_count = len(lines);

    word_count = 0
    char_count = 0

    for line in lines:
        words = line.split()
        for word in words:
            if word.lower() not in stop_words:
                word_count += 1
                char_count +=len(lines)

    print ("<pre>" + "File %s has %d lines, %d words, %d characters.\n" % (file_name, line_count, word_count, char_count) + "</pre>")


get_numbers_from_file('speeches/abraham_lincoln_1st.txt')
get_numbers_from_file('speeches/abraham_lincoln_2nd.txt')
get_numbers_from_file('speeches/barack_obama.txt')
get_numbers_from_file('speeches/bill_clinton_1st.txt')
get_numbers_from_file('speeches/franklin_roosevelt_2nd.txt')
get_numbers_from_file('speeches/john_kennedy.txt')
get_numbers_from_file('speeches/richard_nixon.txt')
get_numbers_from_file('speeches/ronald_reagan_1st.txt')
get_numbers_from_file('speeches/teddy_roosevelt.txt')
get_numbers_from_file('speeches/thomas_jefferson_1st.txt')
mpopova@hills.ccsf.edu