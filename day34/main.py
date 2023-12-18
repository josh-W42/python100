from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests


def replace_encodings(q: str) -> str:
    return q.replace("&quot;", "'").replace("&#039;", "'")


try:
    response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
    response.raise_for_status()

    data = response.json()
    results: list[dict] = data['results']

    for result in results:
        result['question'] = replace_encodings(result['question'])

    question_data = results

except requests.HTTPError:
    print("Error occurred when contacting quiz api, using default data")

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
