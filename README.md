# 🧪 Pytest Practice Lab

## A Testing Playground for Mastering pytest

Welcome to my testing laboratory! This repository is my personal playground where I've been diving deep into **pytest** - Python's most powerful testing framework. Think of this as my testing sketchbook, filled with experiments, discoveries, and "aha!" moments in the world of software testing.

---

## 🎯 What This Repo Is About

This isn't just another "hello world" project. It's a **hands-on testing laboratory** where I systematically explore and implement various testing concepts, patterns, and best practices. Each test file represents a different testing challenge I've conquered.

---

## 🧩 What You'll Find Inside

### 📐 **Shape Hierarchy Testing** (`test_circle.py`, `test_rectangle.py`, `test_square.py`)
Geometric shapes aren't just for math class! I built a class hierarchy (Shape → Circle/Rectangle → Square) and learned:
- **Setup/Teardown methods** - Creating fresh test environments for every test
- **Fixture injection** (`conftest.py`) - Reusable test components across multiple files
- **Parameterized testing** - Testing multiple scenarios with a single elegant test function

```python
# Testing 4 different squares with one line of code!
@pytest.mark.parametrize("side_len, expected_area", [(5,25),(4,16),(3,9),(0,0)])
```

### 🎭 **Mocking & External Dependencies** (`test_service_to_mock.py`)
The real magic happens here! I learned how to test code that talks to the outside world WITHOUT actually talking to the outside world:
- **Mocking database calls** - Testing user retrieval without a real database
- **Mocking API requests** - Simulating HTTP responses (both success AND failure)
- **Understanding WHAT to mock** (external dependencies) vs **WHAT NOT to mock** (the code you're actually testing)

```python
# Testing error handling without crashing into real APIs
@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response.status_code = 400  # Simulate API failure
    with pytest.raises(requests.HTTPError):
        service.get_user_api()
```

### ⚡ **Edge Cases & Error Handling** (`test_my_functions.py`)
Because things break in the real world:
- **Division by zero** - Testing that proper exceptions are raised
- **Slow operations** - Marking and managing time-consuming tests with custom markers
- **Type hints** - Keeping code maintainable while testing

### 🏗️ **Test Organization Patterns**
- **Class-based tests** - Grouping related test methods
- **Function-based tests** - Simple, focused test functions
- **Shared fixtures** via `conftest.py` - DRY (Don't Repeat Yourself) testing

---

## 📁 Project Structure

```
pytest_practice/
├── src/                       # Source code (the system under test)
│   ├── __init__.py           # Makes src a proper Python package
│   ├── shape.py              # Shape hierarchy (Circle, Rectangle, Square)
│   ├── service_to_mock.py    # Functions with external dependencies
│   └── my_functions.py       # Utility functions to test
│
├── tests/                     # All test files live here
│   ├── __init__.py           # Makes tests a proper Python package
│   ├── conftest.py           # Shared pytest fixtures
│   ├── test_circle.py        # Circle-specific tests
│   ├── test_rectangle.py     # Rectangle tests with fixtures
│   ├── test_square.py        # Parameterized square tests
│   ├── test_my_functions.py  # Basic function tests + markers
│   └── test_service_to_mock.py # Mocking demonstrations
│
└── README.md                  # You are here!
```

---

## 🚀 Key Testing Concepts Demonstrated

| Concept | What I Learned | Where to See It |
|---------|---------------|-----------------|
| **Fixtures** | Reusable test setup across files | `conftest.py` → `test_rectangle.py` |
| **Setup/Teardown** | Fresh test state for every method | `test_circle.py` |
| **Mocking** | Replacing real dependencies with fakes | `test_service_to_mock.py` |
| **Parameterization** | One test, many inputs/outputs | `test_square.py` |
| **Exception Testing** | Verifying code fails correctly | `test_my_functions.py`, `test_service_to_mock.py` |
| **Custom Markers** | Tagging and selectively running tests | `@pytest.mark.slow` |
| **Mock Return Values** | Controlling what mocks output | `test_service_to_mock.py` |
| **Mock Side Effects** | Simulating errors and edge cases | `test_service_to_mock.py` |

---

## 💡 My Testing Philosophy

Through this practice, I've internalized some golden rules:

1. **"Don't test the mock, test your logic"** - Mocks are tools, not targets
2. **"Fast tests are good tests"** - Mock external calls to keep test suites lightning-fast
3. **"Isolate or die"** - Each test should stand alone, independent of others
4. **"Edge cases live here"** - If it can break, test it (division by zero, empty lists, null values, etc.)

---

## 🏃‍♂️ Running the Tests

```bash
# Run everything
pytest

# Run with verbose output (see test names)
pytest -v

# Run only slow tests (when you have time for coffee ☕)
pytest -m slow

# Run a specific test file
pytest tests/test_circle.py

# Run with print statements visible (great for debugging)
pytest -s

# Stop on first failure (fast feedback loop)
pytest -x

# Show the slowest tests
pytest --durations=3
```

---

## 🎓 What I Learned (The Hard Way)

- **Mocking the wrong thing** - I once mocked the function I was testing (facepalm). Now I know: mock EXTERNAL dependencies, not your own logic!
- **Fixtures are magical** - `conftest.py` can make fixtures available everywhere without explicit imports
- **Parameterization reduces code by 80%** - Testing 10 scenarios used to mean 10 functions. Now it's one function with 10 lines.
- **Verbose mode (-v) is your friend** - Dots (`.`) tell you nothing. Test names tell you everything.

---

## 🔮 What's Next?

This is a living repository. Future experiments will include:
- [ ] Async function testing
- [ ] Database integration testing with test containers
- [ ] Coverage reports and what 100% coverage really means
- [ ] Property-based testing with Hypothesis
- [ ] Mocking context managers and file I/O

---

## 🤔 Why I Built This

Testing isn't glamorous. Nobody brags about their test suite at parties. But **great software is tested software**. This repository is my deliberate practice - the testing equivalent of scales and arpeggios for a musician. Every test I write makes me a more confident, more reliable developer.

---

**Happy Testing!** 🐍✨

*"Code without tests is like a house without smoke detectors. It works until it doesn't."*
