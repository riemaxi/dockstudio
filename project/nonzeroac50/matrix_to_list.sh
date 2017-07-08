cat report/matrix.tsv | python matrix_to_list.py | grep -ve '^[NT,0]' | awk '{printf "%s\t%s\t%s\n",$2,$3,$1}' | sort
