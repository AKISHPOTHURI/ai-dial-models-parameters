from task.app.main import run

# TODO:
#  Try `max_tokens` parameter. It sets the maximum length of the AI's response. The AI will stop generating text once it hits this limit.
#  User massage: What is token when we are working with LLM?
# Let's try with a very limited max_tokens
print("=== Testing with max_tokens=20 ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    max_tokens=20
)

# Now with a moderate limit
print("\n=== Testing with max_tokens=100 ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    max_tokens=100
)

# Finally with a generous limit
print("\n=== Testing with max_tokens=500 ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    max_tokens=500
)

# Let's try with default (no explicit limit)
print("\n=== Testing with default max_tokens ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True
)
# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length`, and if you check the
# `content,` it is clearly unfinished.