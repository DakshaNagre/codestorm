# we can override the default values of the template
FLAVOR="m1.medium"
MASTER_FLAVOR=$FLAVOR
DOCKER_VOLUME_SIZE_GB=10
KEYPAIR=dnagre-api-key

# number of instances
N_MASTER=1
N_NODES=3

openstack coe cluster create --cluster-template codestorm_cluster_template_2 \
    --master-count $N_MASTER --node-count $N_NODES \
    --keypair dnagre \
    --master-flavor $MASTER_FLAVOR --flavor $FLAVOR \
    --docker-volume-size $DOCKER_VOLUME_SIZE_GB k8s
