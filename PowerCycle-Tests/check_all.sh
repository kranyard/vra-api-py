# Swisscom test
#

#for x in {001..050}; do 
	#./get_resourcestate.py sc-powertest-$x 
#done

for i in `cat machines200.txt` ; do
	./get_resourcestate.py $i
done
