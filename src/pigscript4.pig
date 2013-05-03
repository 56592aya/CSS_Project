main_rel = LOAD 'initial.txt' using PigStorage('\t') AS (created_at:chararray, id_str:chararray, hashes:chararray);

tokenized = FOREACH main_rel GENERATE created_at, id_str, TOKENIZE(hashes) AS separated;
STORE tokenized INTO 'all';
