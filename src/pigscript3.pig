main_rel = LOAD 'initial.txt' using PigStorage('\t') AS (created_at:chararray, id_str:chararray, hashes:chararray);
filtered = FILTER main_rel BY hashes MATCHES '.+';
tokenized = FOREACH filtered GENERATE created_at, id_str, TOKENIZE(hashes) AS separated;
flattened = FOREACH tokenized GENERATE created_at, id_str, FLATTEN(separated) AS hash_tag;
temp_04 = GROUP flattened by hash_tag;
temp_05 = FOREACH temp_04 GENERATE group AS hash_tag, COUNT(flattened) AS count;
temp_06 = ORDER temp_05 BY count;
STORE temp_06 INTO 'Hottest_Topics';
