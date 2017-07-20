#/bin/bash

cut -c2,7 
cut -c2-7

### 
cut -f-3  ## prints first 3 fields
cut -c13-  ### print from 13th to end
cut -f1-3 -d ' ' ## first three words
### 
head -c20 : first 20 chars
head -22|tail 11  - lines between 12  to 22

tr '(' '['|tr ')' ']' = replace all ( with [])

sort -t $'\t' -k2,2 -nr
sort -t $'\t' -k2,2 -n -r
