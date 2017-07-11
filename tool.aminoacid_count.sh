cat $1 | awk '/^ATOM(.*)(GLY|GLU|GLN|SER|LYS|LEU|TYR|VAL|ILE|LYS|ALA|ARG|PRO|PHE|MET|TRP|ASP)/ {if (length($4)==3) print $4}' | sort | uniq -c
