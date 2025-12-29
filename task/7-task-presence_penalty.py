from task.app.main import run

# TODO:
#  Try `presence_penalty` parameter.
#  Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's
#  likelihood to talk about new topics. Higher values == more topic diversity.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: What is an entropy in LLM's responses?


# Let's try with no presence penalty (default)
print("=== Testing with presence_penalty=0 (default) ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    presence_penalty=0
)

# Now with moderate presence penalty
print("\n=== Testing with presence_penalty=0.5 ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    presence_penalty=0.5
)

# Finally with high presence penalty
print("\n=== Testing with presence_penalty=1.0 ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    presence_penalty=1.0
)

# Let's try with a negative presence penalty
print("\n=== Testing with presence_penalty=-0.5 ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    presence_penalty=-0.5
)

# In the final result, we can see that the higher `presence_penalty` (2.0) the more LLM is trying to add topics that
# somehow related to the main topic.
# For Anthropic and Gemini this parameter will be ignored