from s3_uploader import utils


def test_get_filename():
    assert utils.get_filename({b'Content-Disposition': b'form-data; name="file"; filename="images.jpeg"',
                               b'Content-Type': b'image/jpeg'}) == 'images.jpeg'
