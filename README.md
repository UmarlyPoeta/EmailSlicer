# Email Slicer

This Python program provides a simple utility to extract the username and domain from an email address.

## Usage

To use the program, run it and input your email address when prompted:

```python
python main.py
```

The program will then display the extracted username and domain of the provided email address.

## EmailSlicer Function

The core functionality is encapsulated in the `EmailSlicer` function, which takes an email address as input and returns a dictionary containing the username and domain.

```python
def EmailSlicer(email):
    # ...
```

### Example:

```python
result = EmailSlicer("user@example.com")
print(result)  # Output: {"username": "user", "domain": "example.com"}
```

## Input

The program prompts the user for their email address using the `input` function:

```python
email = input("What's your email: ")
```

## Regular Expression

The email address is validated and parsed using a regular expression:

```python
time = re.search(r"([\w\d_]+)@([\w.]+.[\w.]+)", email, flags=re.IGNORECASE)
```

- `([\w\d_]+)`: Matches the username part of the email address, allowing alphanumeric characters and underscores.
- `@`: Matches the '@' symbol separating the username and domain.
- `([\w.]+.[\w.]+)`: Matches the domain, allowing alphanumeric characters and periods. The final `[\w.]+` ensures at least one period in the domain.

## Handling Errors

If the input email address does not match the expected format, the program raises a `ValueError`:

```python
raise ValueError("Invalid email address")
```

## Running the Program

The main function, `main()`, orchestrates the interaction with the user and prints the result:

```python
if __name__ == "__main__":
    main()
```

## Testing

The program includes a set of tests to ensure the accuracy of the `EmailSlicer` function. These tests are defined in `test_main.py`:

```python
from main import EmailSlicer
import pytest

def test_1():
    with pytest.raises(ValueError):
        assert EmailSlicer("adamedu.pl")
        assert EmailSlicer("pat?ryk@gmail.com")
        assert EmailSlicer("patryk@1980.edu")
        assert EmailSlicer("patryk@gmail")
        assert EmailSlicer("@gmail.com")
        assert EmailSlicer("patryk@")
        assert EmailSlicer("patrykgmail")

def test_2():
    assert EmailSlicer("patryk@gmail.com") == {"username": "patryk", "domain": "gmail.com"} 
    assert EmailSlicer("patryk@student.edu.pl") == {"username": "patryk", "domain": "student.edu.pl"} 
    assert EmailSlicer("pat1923@") == {"username": "patryk", "domain": "gmail.com"} 
    assert EmailSlicer("patryk_k@gmail.com") == {"username": "patryk_k", "domain": "gmail.com"}
```

To run the tests:

```bash
pytest test_main.py
```

Feel free to modify the code or integrate it into your projects as needed. If you want to enhance the functionality, consider expanding the regular expression to handle more edge cases.
