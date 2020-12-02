FLAVOR="m1.medium"
MASTER_FLAVOR=$FLAVOR
DOCKER_VOLUME_SIZE_GB=10

openstack coe cluster template create --coe kubernetes \
    --image "Fedora-Atomic-27-20180419" \
    --keypair dnagre \
    --external-network public --fixed-network codestorm-network-2 --fixed-subnet codestorm-subnet2 --network-driver flannel \
    --flavor $FLAVOR --master-flavor $MASTER_FLAVOR \
    --docker-volume-size $DOCKER_VOLUME_SIZE_GB --docker-storage-driver devicemapper \
    --floating-ip-enabled \
    --labels cloud-provider-enabled=true \
    --volume-driver cinder \
    codestorm_cluster_template_2
