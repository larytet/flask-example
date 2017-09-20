#iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
current_dir=`pwd`
cd `dirname $0`
init_path=`pwd`/yalas
echo Running with $init_path
FLASK_DEBUG=1  FLASK_APP=$init_path/app.py flask run --host=0.0.0.0 &
#python $init_path/app_test.py
cd $current_dir
