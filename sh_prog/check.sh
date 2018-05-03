currentver="$(python -V 2>&1)"


if ! echo $currentver | grep "2.7" ; then
    echo Python version used is $currentver our tested version is 2.7.x
fi



