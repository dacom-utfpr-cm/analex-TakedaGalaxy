import pytest
import subprocess
import shlex
import os, fnmatch

import analex

test_cases = [("", "-k"), ("teste.c", "-k"), ("notexists.cm", "-k")]

for file in fnmatch.filter(os.listdir('tests'), '*.cm'):
    test_cases.append((file, "-k"))

@pytest.mark.parametrize("input_file, args", test_cases)
def test_execute(input_file, args):
    if(input_file != ''):
        path_file = 'tests/' + input_file
    else:
        path_file = ""
    
    cmd = "python analex.py {0} {1}".format(args, path_file)
    process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    stdout, stderr = process.communicate()
    stdout, stderr

    path_file = 'tests/' + input_file
    output_file = open(path_file + ".lex.out", "r")

    #read whole file to a string
    expected_output = output_file.read()

    output_file.close()

    saida_certa = stdout.decode("utf-8").replace("\r", "");

    print("Generated output:")
    print(saida_certa)
    print("Expected output:")
    print(expected_output)

    assert saida_certa.strip() == expected_output.strip()
