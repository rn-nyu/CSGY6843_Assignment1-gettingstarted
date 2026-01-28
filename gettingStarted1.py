### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

## Raj: As a design choice, will prefer this questions and answer as a Dictionary or JSON file
## (purpose build), preferably in separate file.
## This makes it easily scalable, less error-prone and separates question and answer dataset from code logic

#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#"Are encoding and encryption the same? - Yes/No":
#"Is it possible to decrypt a message without a key? - Yes/No":
#"Is it possible to decode a message without a key? - Yes/No":
#"Is a hashed message supposed to be un-hashed? - Yes/No":
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#"Is MD5 a secured hashing algorithm? - Yes/No":
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":

## Dictionary with questions and answers
questions_list = {
"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?": "pcap",
"Are encoding and encryption the same? - Yes/No": "No",
"Is it possible to decrypt a message without a key? - Yes/No": "No",
"Is it possible to decode a message without a key? - Yes/No": "No",
"Is a hashed message supposed to be un-hashed? - Yes/No": "No",
"What is the SHA256 hashing value of your NYU email and use the answer in your code - ": "9402f67f3955348dcddaa6dd0e369a05b00c51f1561eec44c3299ceb74a60d77",
"Is MD5 a secured hashing algorithm? - Yes/No": "No",
"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number": 4,
"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number": 2
}
import sys

##Clean function
def clear_str (query):
    ##Remove leading/trailing spaces
    s_query = query.strip()

    # Remove extra spaces for resolving extra space in question words
    es_query = " ".join(s_query.split())

    # Lower for comparison
    les_query = es_query.lower()
    return les_query

def welcome_assignment_answers(user_question):
    # Validate whether missing question moved to main program as per project assignment

    # Placeholder variable for answer if question found
    user_answer = None

    # Clean the user question from leading/trailing or extra space between words,case sensitivity etc
    cl_question = clear_str(user_question)

    # Loop through the dictionary, compare with user question and print the ans
    for k, v in questions_list.items():
        if cl_question == k.lower():
            user_answer=v
            break

    if not user_answer:
        raise ValueError("Question not found")
        #print("Question not found")
        #sys.exit(1)
        #return user_answer
    return user_answer

if __name__ == "__main__":
    #use this space to debug and verify that the program works
    #debug_question = "Are encoding and encryption the same1? - Yes/No"
    if len(sys.argv) < 2:
        print("String needs to be added")
        sys.exit(1)

    question = sys.argv[1]
    #try:
    #if not question:
        #raise ValueError("Missing Question")
        #print("Missing Question")
    #else:
    welcome_assignment_answers(question)
    #except ValueError as e:
     #   print(f"Error: {e}")