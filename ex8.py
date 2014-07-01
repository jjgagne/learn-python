formatter = "%r %r %r %r"

# 1 2 3 4
print formatter % (1, 2, 3, 4)
# 'One' 'Two' 'Three' 'Four'
print formatter % ("One", "Two", "Three", "Four")
# True False False True
print formatter % (True, False, False, True)
# '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
print formatter % (formatter, formatter, formatter, formatter)
# 'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
# NOTE: %r uses most optimal output... In this case though, double quotes used when there are single quotes in string.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)