question = input("Enter the question: ")
answer_a = input("Enter answer A: ")
answer_b = input("Enter answer B: ")
answer_c = input("Enter answer C: ")
answer_d = input("Enter answer D: ")
correct_answer = input("Enter the letter of the correct answer: ")

question_string = f"{question} \n A. {answer_a} \n B. {answer_b} \n C. {answer_c} \n D. {answer_d} \n Correct Answer: {correct_answer} \n"

with open("questions.txt", "a") as file:
    file.write(question_string)
