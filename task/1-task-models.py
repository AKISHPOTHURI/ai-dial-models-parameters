from task.app.main import run

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# TODO:
#  Try different models (`deployment_name`) with such user request:
#  User massage: What LLMs can do?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

# First, let's try with GPT-4o
print("=== Testing with GPT-4o ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=False,
)

# Next, let's try with Claude
print("\n=== Testing with Claude 3.7 Sonnet ===")
run(
    deployment_name='claude-3-7-sonnet@20250219',
    print_request=True,
    print_only_content=False,
)

# Finally, let's try with Gemini
print("\n=== Testing with Gemini 2.5 Pro ===")
run(
    deployment_name='gemini-2.5-pro',
    print_request=True,
    print_only_content=False,
)