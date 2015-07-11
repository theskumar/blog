Title: Testing (Software Development)
Slug: testing
Date: 2015-06-16 01:03:10
Tags: testing, pytest, presentation, software, python
Category: software
Summary: Getting familiar with testing in software industry.

The idea is here is to introduce you the world of testing in software industry and provide some guidelines and things to keep in mind while you are doing so.

<iframe src="https://docs.google.com/presentation/embed?id=1yesEE3ScAsJ3L8AkNMTvEZfOcblBkyVVu1JG0KeCG-4&amp;start=false&amp;loop=false&amp; frameborder="0" width="100%" height="378" style="border:0" allowfullscreen=true></iframe>
<a href="https://docs.google.com/presentation/d/1yesEE3ScAsJ3L8AkNMTvEZfOcblBkyVVu1JG0KeCG-4/pub" target="_blank"><small>Open in new tab</small></a>

# What is Testing?

Testing in it's very basic terms means, __"See if something is working"__ and there are many ways of doing it. Some do by trying things in a controlled environment, some do out in the world live, some ask someone else to do it for them. 

In software industry, testing almost the same thing.

> In softwares industry, a bad code is acceptable, not a wrong code.


# Testing Tools

If you are able to write or speak in a particular lauguage, it become very easy to test or tell it to someone what to test. Now, if you have a better 

While testing, the tools can be categorized in two catergories:
1. Tools that help in discovering, run and cleaning up a test (pytest, unittest, nose, tox, DjangoTestRunner, etc.)
2. Tools you can use inside your test code (mock, freezegun, responses)


```
$ pip install pytest
```

```python
# file: utils.py
def is_prime(num):
    ## Do something here and return true or false
    return True


# file: test_simple_interest.py
from utils import is_prime

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(43) is True
    assert is_prime("abc") is False
    assert is_prime(10) is False
```
```
$ py.test
```

# Further Reading:

1. [pytest.org][pytest]
2. [Testing Your Code - Python Guide][python-guide-testing] - by Kenneth Reitz


[pytest]: http://pytest.org
[python-guide-testing]: http://docs.python-guide.org/en/latest/writing/tests/
