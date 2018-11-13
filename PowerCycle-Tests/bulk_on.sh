# Swisscom test
# Powercycle 50 machines sc-powertest-001 ... sc-powertest-050
#


for x in `cat off.txt` ; do
	echo $x
	./turnoff_machine.py $x 
done

