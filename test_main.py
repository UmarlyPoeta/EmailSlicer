from main import EmailSlicer
import pytest


def test_1():
    with pytest.raises():
        assert EmailSlicer("adamedu.pl")
        assert EmailSlicer("pat?ryk@gmail.com")
        assert EmailSlicer("patryk@1980.edu")
        assert EmailSlicer("patryk@gmail")
        assert EmailSlicer("@gmail.com")
        assert EmailSlicer("patryk@")
        assert EmailSlicer("patrykgmail")

def test_2():
    assert EmailSlicer("patryk@gmail.com")=={"username":"patryk","domain":"gmail.com"} 
    assert EmailSlicer("patryk@student.edu.pl")=={"username":"patryk","domain":"student.edu.pl"} 
    assert EmailSlicer("pat1923@")=={"username":"patryk","domain":"gmail.com"} 
    assert EmailSlicer("patryk_k@gmail.com")=={"username":"patryk_k","domain":"gmail.com"} 
