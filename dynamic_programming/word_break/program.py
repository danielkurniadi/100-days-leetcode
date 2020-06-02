"""
"""

def word_break(string, dictionary):
    N = len(string)
    M = len(dictionary)

    dp = {}
    dictionary = {word: i for i, word in enumerate(dictionary)}

    def topDown(start):
        if (start, bit_state) in dp:
            return dp[(start, bit_state)]

        word = ""
        for i in range(start, N):
            word += string[i]

            if word in dictionary:
                bit = bit_state & ~ (1 << dictionary[word])

                if bit == 0 and i+1 == N:
                    return True

                res = topDown(i+1, bit)

                if res == True:
                    dp[(start, bit_state)] = True
                    return True

        dp[(start, bit_state)] = False
        return False


    init_bit = (1 << M) - 1
    return topDown(0, init_bit)


if __name__ == "__main__":
    # TEST CASE 1
    string = "penapenpena"
    dictionary = ["pen", "pena", "a"]
    
    print("Test input:", "string = ", string, "dictionary = ", dictionary)
    print("Output:", word_break(string, dictionary))
    