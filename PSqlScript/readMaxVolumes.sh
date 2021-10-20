deploymentName=$1
component=$2

{
psql -d vcac <<EOF
COPY
(select eff_state from comp_deployment where name = '$deploymentName' )
TO STDOUT;
EOF
} | jq .valueMap.$component.values.max_volumes.value.value
