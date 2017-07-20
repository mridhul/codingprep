Unix[0]="Ubuntu"
Unix[1]="Centos"
Unix[3]="Fedora"

echo ${Unix[@]}

declare -a Ubuntu=(14.04 14.10 16.04 16.10)

echo ${Ubuntu[@]}

echo ${#Ubuntu[@]}

for i in 1..${Ubuntu[@]};do
	echo $i
done

arrSize=${#Ubuntu[@]}
for ((i=0;i<$arrSize;i++));do
echo $i
done

echo ${Unix[@]:1:2}   #python [unix:1]
echo ${Unix[0]:0:3}

echo ${Unix[@]/Ubuntu/kubuntu} #: replace in an array

declare -a fullArray=("${Ubuntu[@]}" "${Unix[@]}")

echo ${fullArray[@]}

declare -a pattern=(${arr[@]/*[Aa]*/})
echo ${pattern[@]}

sed -i = case insenstive - sed -e 's/thy/your/ig'
sed highlight - sed -e 's/thy/{$}/ig
sed -r 's/[0-9]{4} /**** /g''   - number masking (credit card)