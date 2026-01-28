### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

import sys

##Clean function
def clear_str (query):
    ##Remove leading/trailing spaces
    ##Creates error with Q6, since the Gradescope question has a trailing space
    ##s_query = query.strip()

    # Lower for comparison
    low_query = query.lower()
    return low_query

def welcome_assignment_answers(question):
    # Students do not have to follow the skeleton for this assignment.
    # Another way to implement is using a "case" statements similar to C.
    if clear_str(question) == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?".lower():
        answer = "pcap"
    elif clear_str(question) == "Are encoding and encryption the same? - Yes/No".lower():
        answer = "No"
    elif clear_str(question) == "Is it possible to decrypt a message without a key? - Yes/No".lower():
        answer = "No"
    elif clear_str(question) == "Is it possible to decode a message without a key? - Yes/No".lower():
        answer = "Yes" #No
    elif clear_str(question) == "Is a hashed message supposed to be un-hashed? - Yes/No".lower():
        answer = "No"
    elif clear_str(question) == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ".lower():
        answer = "9402f67f3955348dcddaa6dd0e369a05b00c51f1561eec44c3299ceb74a60d77"
    elif clear_str(question) == "Is MD5 a secured hashing algorithm? - Yes/No".lower():
        answer = "No"
    elif clear_str(question) == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number".lower():
        answer = 5
    elif clear_str(question) == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number".lower():
        answer = 3
    else:
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return answer
    # Complete all the questions.

if __name__ == "__main__":
    #use this space to debug and verify that the program works
    #debug_question = "Are encoding and encryption the same1? - Yes/No"
    if len(sys.argv) < 2:
        print("String needs to be added")
        sys.exit(1)

    question = sys.argv[1]
    try:
        print(welcome_assignment_answers(question))
    except ValueError as e:
        print(f"Error: {e}")