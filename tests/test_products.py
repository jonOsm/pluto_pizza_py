def test_index_invalid_input():
    # negative or 0 item requets should return 422
    # negative or 0 offset should return 422
    pass


valid_product_index_input = [({"page": 1, "size": 12})]


def test_index_valid_input():
    # it should return the specified number of items
    # it should return offset according
    # it should return an image url with a path of "static"
    # loading that image should return 200 with the image data
    # a token should not be required to load images
    pass
