run:
	python f.py --port 8081 &
	python g.py --port 8082 &
	python main.py --port-h 8081 --port-g 8082