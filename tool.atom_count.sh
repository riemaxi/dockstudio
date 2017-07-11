cat $1 | awk '/^ATOM/{print $1}' | uniq -c
