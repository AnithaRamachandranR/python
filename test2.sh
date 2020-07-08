aws s3 cp /home/ec2-user/anitha/ s3://anitha-bucket/ --recursive --exclude "*" --include "*.txt"
VARIABLE=`python ani.py`
if test $VARIABLE -eq 1; then
        aws s3 sync /home/ec2-user/anitha/  s3://anitha-bucket --exclude "*" --include "*.txt"
else
        echo "All files are copied...You are good to go...."
fi
