cat report/matrix.tsv | python matrix_to_list.py | grep -ve '^[NT,0]' | awk '{printf "%s\t%s\t%s\t%s\t%s\t%s\n",$1,$3,$4,$2,$5,$6}' | sort
#cat report/matrix.tsv | python matrix_to_list.py | grep -ve '^[NT,0]' | awk '{printf "%s\t%s\t%s\t%s\t%s\n",$3,$4,$2,$5,$6}' | sort
