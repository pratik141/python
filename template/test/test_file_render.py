from file_render import render_data
import unittest
import os

enabletracemalloc = False

if enabletracemalloc:
	import tracemalloc
	tracemalloc.start()

class TestFileRender(unittest.TestCase):

	def setup(self):
		tt = open("test_template", "w")
		tt.write("""{\n  "var1": "{{ testvar1 }}",\n  "var2": "{{ testvar2 }}" \n}""")
		tt.close()

		td = open("test_data", "w")
		td.write("""testvar1: val1\ntestvar2: val2""")
		td.close()

	def test_render_data(self):
		vardict   = {}
		separator = ":" 
		try:
			self.setup()
			expected_data = """{\n  "var1": "val1",\n  "var2": "val2" \n}"""

			render_data("test_template", "test_data", "outputfile", vardict, separator)
			f = open("outputfile","r")
			data = f.read()
			f.close()
			self.assertEqual(expected_data, data)

		finally:
			os.remove("test_template")
			os.remove("test_data")
			os.remove("outputfile")
			if enabletracemalloc:
				snapshot = tracemalloc.take_snapshot()
				top_stats = snapshot.statistics('lineno')

				print("[ Top 10 ]")
				for stat in top_stats[:10]:
				    print(stat)


if __name__ == '__main__':
	unittest.main()
