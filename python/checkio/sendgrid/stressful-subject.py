"""
Sofia has had a very stressful month and decided to take a vacation for a week. To avoid any stress during her vacation
she wants to forward emails with a stressful subject line to Stephen.

The function should recognise if a subject line is stressful. A stressful subject line means that all letters are in
uppercase, and/or ends by at least 3 exclamation marks, and/or contains at least one of the following “red”
words: "help", "asap", "urgent". Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp",
"H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP"

Input: Subject line as a string.

Output: Boolean.
"""
def is_stressful(subj):
    """
        recoognise stressful subject
    """
    red_words = ["help", "asap", "urgent"]
    # check if ends with '!!!':
    if subj[-3:] == "!!!":
        return True
    # check if ois uppercase:
    if subj.upper() == subj:
        return True
    # check if there is red word:
    for word in red_words:
        founded_word = ""
        index = 0
        next_letter = word[0]
        intterupted_letter = 0
        for sub_letter in subj.lower():
            if sub_letter == " ":
                founded_word = ""
                intterupted_letter = 0
            elif sub_letter == next_letter:
                index += 1
                founded_word += next_letter
                intterupted_letter = 0
                if index < len(word):
                    next_letter = word[index]
                else:
                    break
            elif sub_letter != founded_word[-1:]:
                if intterupted_letter == 1:
                    founded_word = ""
                intterupted_letter += 1
        if word == founded_word:
            return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("UUUURGGGEEEEENT here ") == True, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("We need you A.S.A.P.!!") == True, "Third"
    assert is_stressful("something is gona happen") == False, "Fourth"
    assert is_stressful("where are you?!!!!") == True, "Fourth"
    print('Done! Go Check it!')
