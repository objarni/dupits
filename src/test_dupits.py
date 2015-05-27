def test_finds_duplication_in_single_file(self):
	dupFinder = DupFinder()
	dupFinder.look_through('test.c', 'abc\ndef\abc\ndef\n')
	report = dupFinder.generate_report()
	self.assertEqual("""\
This piece of code was found more than once:
    abc
    def
""", report)

