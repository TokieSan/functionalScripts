declare -a arr=("" "33575" "33576" "33574" "34474" "33683" "33283")
 
for val in ${arr[@]}; do
	xte "str $val"
	xte "key Tab"
	sleep .1
done

xte "key Return"
