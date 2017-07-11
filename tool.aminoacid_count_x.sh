cat $1 | awk '/^ATOM/ {print $4}' | sort | uniq -c | awk '{printf "%s\t%s\n",$2,$1}'
