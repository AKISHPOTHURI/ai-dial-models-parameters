from task.app.main import run

# TODO:
#  Try the `seed` parameter:
#       It allows us to reduce entropy by making the model's output more deterministic.
#       There's no universally "best" seed - any integer works fine. Common approaches:
#            - For testing: Use simple values like 42, 123, or 1000
#       Default: None or random unless specified on the LLM side
#  User massage: Name a random animal

# Let's try with a specific seed value
seed_value = 42

# First run with seed=42
print("=== First run with seed=42 ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    seed=seed_value,
    temperature=0.7  # Setting a non-zero temperature to see randomness
)

# Second run with the same seed=42 (should produce similar results)
print("\n=== Second run with seed=42 ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    seed=seed_value,
    temperature=0.7
)

# Third run with a different seed
print("\n=== Third run with seed=123 ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    seed=123,
    temperature=0.7
)

# Fourth run with no seed (should be different)
print("\n=== Fourth run with no seed ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    temperature=0.7
)