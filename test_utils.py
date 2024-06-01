
import pytest
from src.utils import get_file_type

def test_get_file_type():
    assert get_file_type('example.pdf') == 'application/pdf', "PDF file type should be correctly identified"
    assert get_file_type('example.png') == 'image/png', "PNG file type should be correctly identified"
    # Add more test cases as needed
