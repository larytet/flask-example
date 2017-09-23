#iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
current_dir=`pwd`
cd `dirname $0`
init_path=`pwd`/yalas
echo Running with $init_path

if [ -z "$1" ]
then 
	FLASK_DEBUG=1 FLASK_APP=$init_path/app.py flask run --host=0.0.0.0 &
	flask_process_id=$!
	echo Flask is started $flask_process_id
	sleep 1
	pytest -s $init_path/../yalas_test.py
	#kill $flask_process_id
	cd $current_dir

	# kill all child processes
	kill 0
else
	FLASK_DEBUG=1 FLASK_APP=$init_path/app.py flask run --host=0.0.0.0 
fi
