from planner import create_plan
from executor import execute_plan
from reflection import review_document

request = "Create an AI Hospital proposal."

plan = create_plan(request)

document = execute_plan(plan)

final_document = review_document(document)

print(final_document)