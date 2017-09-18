#iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
current_dir=`pwd`
cd `dirname $0`
init_path=`pwd`/yalas/app.py
echo Running with $init_path
FLASK_DEBUG=1  FLASK_APP=$init_path flask run --host=0.0.0.0
cd current_dir
