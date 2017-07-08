#cat report/assay.tsv | awk '/\s+/ {printf "%s\t%s\n", $2, $1}' | sort > report/sop_assay.tsv
#cat report/assay.tsv | awk '/\s+/ {printf "%s\t%s\n", $1, $2}' | sort > report/assay_sop.tsv
#cat import/matrix.tsv | awk '{print $1}' | sort > import/matrix_assay.txt
#cat report/sergio_toxic.csv | awk 'BEGIN {FS=","};{printf "%s\t%s\n", $1,$2}' | sort > report/sop_toxic.tsv
#cat report/sergio_toxic.csv | awk 'BEGIN {FS=","};{printf "%s\t%s\n", $2,$1}' | sort > report/toxic_sop.tsv
#join import/receptor.txt report/toxic_sop.tsv | awk '{printf "%s\t%s\n",$2,$1}' | sort > report/sop_protein.tsv

sh matrix_to_list.sh | awk '{print $1}' | uniq

#cat log/scoring_scoring.txt | sort > report/docking_score.txt

#join report/protein_assay.tsv report/docking_score.txt | sort | awk '{printf "%s\t%s\t%s\n",$2,$3,$4}' > report/assay__compound__docking_score.tsv

#sh matrix_to_list.sh > report/assay__compound__sipes_score.tsv

#sh compound_atoms_report.sh > report/compound_atoms.tsv
#sh compound_torsions_report.sh > report/compound_torsions.tsv
#join report/compound_atoms.tsv report/compound_torsions.tsv | awk '{printf "%s\t%s\t%s\n",$1,$2,$3}' | sort > report/compound_atoms_torsions.tsv

