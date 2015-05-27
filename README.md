dupits v0.1
===========

At a glance
-----------

dupits finds duplication in the files specified on standard
input, and then prints a result of its finding to standard output.

A typical use would be:

	find . -name "*.py" | python dupits.py

If there is absolutely no duplication in the python files found,
you will see the mightly message

	Found no duplication. Congrats!

However, in a more realistic scenario, you would be shown something
like this

	Found duplicate lines:
		def test_one(self):
			self.assertEqual(1, 1)



Command line options
====================


Dependencies
============

Dupits is written in Python2.7 and tested only on that platform for now.

No external libraries are necessary.


License
=======

dupits is licensed under the forgiving MIT-license. Basically, do whatever
you please but don't blame me :)


