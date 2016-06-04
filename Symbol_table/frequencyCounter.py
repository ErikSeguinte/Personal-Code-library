import __future__
import sys
import string

def main(ST):
    if len(sys.argv) > 1:
        input_file = sys.argv[1]



    st = ST()

    with open(input_file,'r') as i_file:
        for line in i_file:
            if line == '\n':
                continue
            line = line.split(" ")

            for word in line:
                word = "".join([ch for ch in word if ch not in set(string.punctuation)])
                # print(st.get(word))

                if len(word) < 6:
                    continue

                if not st.contains(word):
                    st.put(word, 1)
                else:
                    print(word + str(st.get(word)))
                    value = st.get(word)
                    value +=1
                    st.put(word, value)

    max_word = "-1"
    st.put(max_word, 0)
    for word in st.keys():
        print(word, st.get(word))
        if st.get(word) > st.get(max_word):
            print(max_word)
            max_word = word
    print(max_word + ": "+ str(st.get(max_word)))


