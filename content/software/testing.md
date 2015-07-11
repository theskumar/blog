Title: Testing (Software Development)
Slug: testing
Date: 2015-06-16 01:03:10
Tags: testing, pytest, presentation, software, python
Category: software
Summary: Getting familiar with testing in software industry.

The idea is here is to introduce you to the world of testing in software industry and provide some guidelines and things to keep in mind while you are doing so.

<iframe src="https://docs.google.com/presentation/embed?id=1yesEE3ScAsJ3L8AkNMTvEZfOcblBkyVVu1JG0KeCG-4&amp;start=false&amp;loop=false&amp; frameborder="0" width="100%" height="378" style="border:0" allowfullscreen=true></iframe>
<a href="https://docs.google.com/presentation/d/1yesEE3ScAsJ3L8AkNMTvEZfOcblBkyVVu1JG0KeCG-4/pub" target="_blank"><small>Open in new tab</small></a>

# What is Software Testing?

Testing in it's very basic terms means, __"check if something is working as espected"__. There are many ways of doing it. Some do by it by hand, some peole automate it, some do it in controlled environment, some do it in in production, some do it themself, some ask someone else to do it for them. In software industry, testing almost the same thing. 

__Consider software project analogous to your dream house building project__. In general, you plan for it, design it, hire people to get doing things and then in general you'll not test it while you are developing it! Once developed, you'll show it to someone, get it approved. Then you either sell it to someone or live in the same house. 

If you live in that same house, you'll probably be able to extend/modify the house as per your need as because you know how you have built it. But the other guy who purchased your house, it's hard and or probably impossible to modify or extend it because he has no clues when the house will fall apart, unless you provide a written specs of the house.

Whatever the do with the house, as time passes it becomes increasingly difficult to modify/extend/maintain that house, unless you have a repeatable way to testing that your house for it's capabilities. 

Software testing is very much how it is with house testing, it's useful, most people don't do it, it's costly and hard to it and you feel it's increasing need as time passes. 

# Why testing is important?

> In softwares industry, a bad code is acceptable, not a wrong code.

- Know your code works
- Save time
- Better code
- It help a software live longer
- It makes everyone happy, removing fear
- “Debugging is hard, testing is easy”

# When to test code?

As with anything, 

> Softwares must be tested, *as soon as possible*.

The reason being, if you don't 1) probably you'll never do it 2) the value of that test decreases as much as you delay it.

> Now is better than never.
> -- [Zen of Python, PEP20][zen]

# How to test?

> Tools are your friend, keep them handy and sharp.

## Testing Tools

If you are able to write or speak in a particular lauguage, it become very easy to test or tell it to someone what to test. Now, if you have a better tools, it just becomes a breeze to test anything.

While testing, the tools can be categorized in two catergories:
1. Tools that help in discovering, run and cleaning up a test (pytest, unittest, nose, tox, DjangoTestRunner, etc.)
2. Tools you can use inside your test code (mock, freezegun, responses)


```shell
$ pip install pytest
```

```python
# file: my_utils.py
def is_prime(num):
    ## Do something here and return true or false
    return True


# file: test_my_utils.py
from my_utils import is_prime

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(43) is True
    assert is_prime("abc") is False
    assert is_prime(10) is False
```
```shell
$ py.test
```

# Further Reading:

1. [pytest.org][pytest]
2. [Testing Your Code - Python Guide][python-guide-testing] - by [Kenneth Reitz]
3. [Getting Started Testing] - by [Ned Batchelder]

Got questions/suggestion, write in the comment below.

[Edit this][edit-url] | [Changelog/Contributors][changelog]

---

[edit-url]: https://github.com/theskumar/blog/edit/master/content/software/testing.md
[changelog]: https://github.com/theskumar/blog/commits/master/content/software/testing.md
[pytest]: http://pytest.org
[python-guide-testing]: http://docs.python-guide.org/en/latest/writing/tests/
[zen]: https://www.python.org/dev/peps/pep-0020/
[Getting Started Testing]: http://bit.ly/pytest0
[Ned Batchelder]: http://nedbatchelder.com/site/aboutned.html
[Kenneth Reitz]: http://www.kennethreitz.org/
