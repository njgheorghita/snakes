import pytest

from snakes.services import (
    extract_image_link,
    get_five_recent_pictures,
)


@pytest.mark.parametrize(
    "string,expected",
    (
        ("asdf", None),
        ("a.a.ahttp://www.web.com/pic.jpgasdf12", "http://www.web.com/pic.jpg"),
    )
)
def test_extract_image_link(string, expected):
    assert extract_image_link(string) == expected


def test_get_five_recent_pictures():
    pics = get_five_recent_pictures()
    assert len(pics) is 5


