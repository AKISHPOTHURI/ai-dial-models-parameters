from task.app.main import run

# TODO:
#  Try the `temperature` parameter that controls the randomness of the output. It's a parameter for balancing creativity
#        and determinism. Range: 0.0 to 2.0, Default: 1.0
#  User massage: Describe the sound that the color purple makes when it's angry
print("\n=== Testing with temperature=0.0 ===")
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    print_request=True,
    temperature=0.0
)

print("\n=== Testing with temperature=0.5 ===")
run(
    deployment_name='gpt-4o',
    print_only_content=True,
    print_request=True,
    temperature=0.5
)

print("\n=== Testing with temperature=1.0 ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    temperature=1.0
)

# Let's try with an even higher temperature
print("\n=== Testing with temperature=1.5 ===")
run(
    deployment_name='gpt-4o',
    print_request=True,
    print_only_content=True,
    temperature=1.5
)