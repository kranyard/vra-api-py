# Swisscom test
# Powercycle 50 machines sc-powertest-001 ... sc-powertest-050
#

start=$(date +%s)

#for x in {001..050}; do 
for x in `cat machines200.txt` ; do
	echo $x
	./powercycle2.py $x >> log.txt 2>&1 &
done

wait

end=$(date +%s)

echo "Total elapsed time :" $(( (end - start) / 60)) "mins" $(((end - start) % 60)) "seconds"
