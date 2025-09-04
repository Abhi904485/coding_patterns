# Coding Patterns

## How to Run Tests

- pytest                # run everything
- pytest tests/test_two_pointers/test_brute_force.py::test_user_role   # run one test
- pytest -k "addition"  # run tests matching keyword
- pytest -m "slow"      # run tests with marker
