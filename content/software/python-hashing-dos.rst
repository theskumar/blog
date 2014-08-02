Prevent Hash DoS in python
###################################
:date: 2013-09-1 12:00
:tags: python, security
:slug: hash-dos-in-python
:category: programming
:summary: How can you prevent denial of service attacks in python if you are using python <= 3


.. raw:: html

   <blockquote class="twitter-tweet"><p>$ export PYTHONHASHSEED=random &#10;&#10;Makes hashes of types unpredictable across <a href="https://twitter.com/search?q=%23python&amp;src=hash">#python</a> invocations, making your app more secure to DOS attacks.</p>&mdash; Anand B Pillai (@pythonhacker) <a href="https://twitter.com/pythonhacker/statuses/375671280394989568">September 5, 2013</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


Denial of Service through hash table multi-collisions or `Hash DoS`_ has been
first reported in 28-Dec-2011 [#]_.


Python and Ruby are partially vulnerable, depending on version or whether the server
running the code is a 32 bit or 64 bit machine. Python 2 by default does not provide
random value for ``PYTHONHASHSEED`` [#]_ though it's behaviour is changed in
python 3 [#]_ which means it has ``random`` as it default value.


References
----------

.. _Hash DoS: http://www.purehacking.com/blogs/josh-zlatin/introduction-to-hash-dos-attacks
.. [#] https://www.nruns.com/_downloads/advisory28122011.pdf
.. [#] http://docs.python.org/2/using/cmdline.html#envvar-PYTHONHASHSEED
.. [#] http://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED
