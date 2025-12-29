from task.app.main import run

# TODO:
#  Try `frequency_penalty` parameter.
#  Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's
#  likelihood to repeat the same line verbatim. Higher values == less repetitive text.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: Explain the water cycle in simple terms for children
# Let's try with no frequency penalty (default)
print("=== Testing with frequency_penalty=0 (default) ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    frequency_penalty=0
)

# Now with moderate frequency penalty
print("\n=== Testing with frequency_penalty=0.5 ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    frequency_penalty=0.5
)

# Finally with high frequency penalty
print("\n=== Testing with frequency_penalty=1.0 ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    frequency_penalty=1.0
)

# Let's try with a negative frequency penalty
print("\n=== Testing with frequency_penalty=-0.5 ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    frequency_penalty=-0.5
)
# Pay attention that when we set for `gpt-4o` frequency_penalty as -2.0 - the request is running too long,
# and in the result we can get something strange (such as repetitive words in the end).
# Copy the results and then check with separate request and ask LLM where is more repetitive blocks in texts.
# For Anthropic and Gemini this parameter will be ignored