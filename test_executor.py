from planner import create_plan
from executor import execute_plan

request = "Create a proposal for an AI Hospital Management System."

plan = create_plan(request)

document = execute_plan(plan)

print(document)