for i in 1 2 3
do
    cp tests/caso2/caso2_test${i}_B.txt ./input_B.txt;
    cp tests/caso2/caso2_test${i}_N.txt ./input_N.txt;
    scip -f caso2.zpl;
    rm input_B.txt input_N.txt;
done

