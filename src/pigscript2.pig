main_rel = LOAD 'initial.txt' using PigStorage('\t') AS (created_at:chararray, id_str:chararray, hashes:chararray);
filtered = FILTER main_rel BY hashes MATCHES '.+';
tokenized = FOREACH filtered GENERATE created_at, id_str, TOKENIZE(hashes) AS separated;
flattened = FOREACH tokenized GENERATE created_at, id_str, FLATTEN(separated) AS hash_tag;
STORE  flattened INTO 'Flattened';


