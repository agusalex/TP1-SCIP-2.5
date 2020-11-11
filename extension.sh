cp tests/extension/extension_test1_B.txt ./input_B.txt;
cp tests/extension/extension_test1_N.txt ./input_N.txt;
scip -f extension.zpl;
rm input_B.txt input_N.txt;

