deploymentName=$1
updatedSchema=$(cat)

{
psql -d vcac <<EOF
update comp_deployment set eff_schema='$updatedSchema' where name = '$deploymentName'
EOF
} 
