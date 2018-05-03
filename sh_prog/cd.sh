lof="$(ls -l  2>&1)"

if ! echo $lof | grep 'cache' | grep 'rw' ; then
    echo 'There is no write permission for the cache directory'
else
   echo ok
fi



