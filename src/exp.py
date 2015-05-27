import re

class Chunk(object):

	p = re.compile(r'\s+')

	def __init__(self, text, srcfile, srcline):
		self.text = text
		self.hash = hash(text)
		self.srcfile = srcfile
		self.srcline = srcline

	def __repr__(self):
		txt = self.p.sub(' ', self.text)
		wanted = 30
		if len(txt) > wanted:
			txt = txt[:wanted - 3] + '...'
		#return "Line %5d: #%23d=%s" % (self.srcline, self.hash, txt)
		return "%s:%d: %s" % (self.srcfile, self.srcline, txt)

def genchunks(srcfile, text, rows):
	"""Generate the ordered series of chunks, each
	chunk 'rows' number of rows long, from text.
	For example,
	>>> txt = 'abcd'
	'abcd'
	>>> list(genchunks(txt, 1)
	[['a'], ['b'], ['c'], ['d']
	>>> list(genchunks(txt, 2)
	[['a', 'b'], ['b', 'c'], ['c', 'd']]
	"""
	lines = text.splitlines()
	l = len(lines)
	for i in range(0, l - rows + 1):
		yield Chunk('\n'.join(lines[i:i+rows]), srcfile, i)

def sorted_chunks(srcfile, text, rows):
	chunks = list(genchunks(srcfile, text, rows))
	chunks.sort(key=lambda chunk:chunk.hash)
	return chunks


def readfile(f):
	with open(f, 'rb') as f:
		return f.read()

import fileinput

lines = []
for line in fileinput.input():
	lines.append(line)
txt = ''.join(lines)
#print txt

raw_chunks = sorted_chunks('tmp.h', txt, 3)

from collections import defaultdict

bag = defaultdict(list)

for chunk in raw_chunks:
	bag[chunk.hash].append(chunk)

for item in bag:
	chunks = bag[item]
	count = len(chunks)
	#print "%23d: #%d" % (item, count)
	if count > 1:
		print "--- Attention! Found duplication:"
		print chunks[0]
		for c in chunks[1:]:
			print 'Also found at line %d' % c.srcline
		print ''
