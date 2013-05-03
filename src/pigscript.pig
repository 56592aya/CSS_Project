main_rel = LOAD 'initial.txt' using PigStorage('\t') AS (created_at:chararray, id_str:chararray, hashes:chararray);

tokenized = FOREACH main_rel GENERATE created_at, id_str, TOKENIZE(hashes) AS separated;
flattened = FOREACH tokenized GENERATE created_at, id_str, FLATTEN(separated) AS hash_tag;
temp_04 = GROUP flattened by id_str;
temp_05 = FOREACH temp_04 GENERATE group AS id_str, COUNT(flattened) AS count;
temp_06 = ORDER temp_05 BY count;
STORE temp_06 INTO 'results_count';
