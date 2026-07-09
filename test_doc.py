from planner import create_plan
from executor import execute_plan
from reflection import review_document
from doc_generator import create_word

request = "Create an AI Hospital proposal."

plan = create_plan(request)

document = execute_plan(plan)

reviewed = review_document(document)

path = create_word(reviewed)

print(path)