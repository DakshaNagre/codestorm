openstack network create codestorm-network-2

openstack subnet create --network codestorm-network-2 --subnet-range 10.0.0.0/24 codestorm-subnet2

openstack router create codestorm-router2

openstack router add subnet codestorm-router2 codestorm-subnet2

openstack router set --external-gateway public codestorm-router2
