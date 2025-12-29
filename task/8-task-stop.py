from task.app.main import run

# TODO:
#  Try `stop` parameter.
#  `stop` (str or list[str]): Tells the AI to stop generating text when it encounters specific words or phrases.
#  Like setting custom "end of response" triggers.
#       Default: None
#  User massage: Explain the key components of a Large Language Model architecture

# Let's try with no stop sequence (default)
print("=== Testing with no stop sequence ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True
)

# Now with a stop sequence at "10"
print("\n=== Testing with stop sequence '10' ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    stop=["10"]
)

# Let's try with multiple stop sequences
print("\n=== Testing with multiple stop sequences ['5', '15'] ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    stop=["5", "15"]
)

# Let's try with a stop sequence that's a phrase
print("\n=== Testing with stop sequence 'that's enough' ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    stop=["that's enough"]
)

# With `stop` parameter we can stop content generation. It can be used for some policies/guardrails. For instance,
# we are the company with the name `Pear` and we don't want that anybody will see in results that our competitor `Apple`
# is cool (stop: ["Apple is cool", "Apple top"]).
# The `finish_reason` will be set as `stop`. So, the users won't know what is the real reason why LLM has stopped generation.