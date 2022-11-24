gcc -fPIC -shared -o libmatmul.so matrix_multiplication.c

FILE=libmatmul.so

if test -f "$FILE"; then
    echo "SUCCESFUL"
else
    echo "ERROR"
fi