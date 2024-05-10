sudo cp /home/ubuntu/api/gunicorn/orders/gunicorn.socket /etc/systemd/system/gunicorn-orders.socket
sudo cp /home/ubuntu/api/gunicorn/orders/gunicorn.service /etc/systemd/system/gunicorn-orders.service

sudo cp /home/ubuntu/api/gunicorn/user/gunicorn.socket /etc/systemd/system/gunicorn-user.socket
sudo cp /home/ubuntu/api/gunicorn/user/gunicorn.service /etc/systemd/system/gunicorn-user.service

sudo systemctl start gunicorn-orders.service
sudo systemctl enable gunicorn-orders.service

sudo systemctl start gunicorn-user.service
sudo systemctl enable gunicorn-user.service
