# https://www.youtube.com/watch?v=rfscVS0vtbw&t=528s
# ============== Building a Multiple Choice Quiz: 3:57:40
from Question import Question

ques_prompts = [
    'What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n',
    'What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n',
    'What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n']

# a list of question-solution pairs
ques_sol = [
    Question(ques_prompts[0], 'a'),
    Question(ques_prompts[1], 'c'),
    Question(ques_prompts[2], 'b')]

# create a function to execute the code


def run_test(ques_sol):
    score = 0
    # loop through the question-solution list
    for i in ques_sol:
        ans = input(i.prompt)
        if ans == i.answer:
            score += 1
    print('You got ' + str(score) + '/' +
          str(len(ques_sol)) + " questions correct!")


# --------------------
run_test(ques_sol)
