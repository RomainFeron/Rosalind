if [ ! -d problems/code/$1 ]; then
	mkdir problems/code/$1
fi
if [ ! -d problems/data/$1 ]; then
	mkdir problems/data/$1
fi
if [ ! -d problems/output/$1 ]; then
	mkdir problems/output/$1
fi
if [ ! -f problems/code/$1/__init__.py ]; then
	touch problems/code/$1/__init__.py
	echo "from .solution import run" > problems/code/$1/__init__.py
fi
if [ ! -f problems/code/$1/solution.py ]; then
	touch problems/code/$1/solution.py
	echo "import os" > problems/code/$1/solution.py
	echo "\n\ndef run(data_dir, output_dir):\n" >> problems/code/$1/solution.py
	echo "    input_file_path = os.path.join(data_dir, 'data.txt')" >> problems/code/$1/solution.py
	echo "    output_file_path = os.path.join(output_dir, 'output.txt')\n" >> problems/code/$1/solution.py
	echo "    input_file = open(input_file_path)" >> problems/code/$1/solution.py
	echo "    output_file = open(output_file_path, 'w')\n" >> problems/code/$1/solution.py 
fi
if [ ! -f problems/data/$1/data.txt ]; then
	touch problems/data/$1/data.txt
fi
if [ ! -f problems/output/$1/output.txt ]; then
	touch problems/output/$1/output.txt
fi