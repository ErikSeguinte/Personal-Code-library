import __future__
import sys
import string

def main(ST):
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "tale.txt"



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
                    value = st.get(word)
                    value +=1
                    st.put(word, value)

    max_word = "-1"
    st.put(max_word, 0)
    for word in st.keys():
        if st.get(word) > st.get(max_word):
            max_word = word
    print(max_word + ": "+ str(st.get(max_word)))
    st.delete("little")
    print(max_word + ": "+ str(st.get(max_word)))
    print(st.min_root().key, st.min_root().value)
    st.del_min()
    print(st.min_root().key, st.min_root().value)
    print(list(st.range_root("livelier", "lively")))


