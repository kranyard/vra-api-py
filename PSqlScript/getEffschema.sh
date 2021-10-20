deploymentName=$1

{
psql -d vcac <<EOF
COPY
(select eff_schema from comp_deployment where name = '$deploymentName' )
TO STDOUT;
EOF
} 
