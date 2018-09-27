# Swisscom test
# Powercycle 50 machines sc-powertest-001 ... sc-powertest-050
#

start=$(date +%s)

for x in {001..050}; do 
	echo $x
	./powercycle2.py sc-powertest-$x &
done

wait

end=$(date +%s)

echo "Total elapsed time :" $(( (end - start) / 60)) "mins" $(((end - start) % 60)) "seconds"
