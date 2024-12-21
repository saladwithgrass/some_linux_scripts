TO_REPLACE=$1
REPLACE_WITH=$2
FILE=$3
cmd="sed -i s/\"$TO_REPLACE/$REPLACE_WITH/g\" $FILE"
echo "to be executed: $cmd"
eval {$cmd}
