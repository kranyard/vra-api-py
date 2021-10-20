deploymentName=$1

{
psql -d vcac <<EOF
COPY
(select eff_state from comp_deployment where name = '$deploymentName' )
TO STDOUT;
EOF
} 
