from src.main import sort_waste

def test_plastic():
    assert sort_waste("bottle") == "plastic"
