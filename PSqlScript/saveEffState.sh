deployment=$1

SCRIPTS=/tmp/eff

su - postgres -c "$SCRIPTS/getEffstate.sh $deployment" | grep -v "Last login" 
