deployment=$1

SCRIPTS=/tmp/eff

su - postgres -c "$SCRIPTS/getEffschema.sh $deployment" | grep -v "Last login" 
