declare -a data
data=(`ssh -i /home/ec2-user/key.pem ec2-user@18.206.219.186 'ls -R ani/ | grep .csv' `)
echo ${data[@]}
ssh -i /home/ec2-user/key.pem ec2-user@18.206.219.186 'aws s3 cp /home/ec2-user/ani/ s3://anitha-bucket/ --exclude "*" --include "*.csv" --recursive'
VARIABLE=`python test.py ${data[@]}`
#echo ${VARIABLE}
if test $VARIABLE -eq 1; then
     ssh -i /home/ec2-user/key.pem ec2-user@18.206.219.186 'aws s3 sync /home/ec2-user/ani/  s3://anitha-bucket/ --exclude "*" --include "*.csv" '
     VARIABLE1=`python test.py ${data[@]}`

     if test $VARIABLE1 -eq 1; then
          ssh -i /home/ec2-user/key.pem ec2-user@18.206.219.186 'aws s3 sync /home/ec2-user/ani/  s3://anitha-bucket/ --exclude "*" --include "*.csv" '
          echo "files"
     else
             echo "ALL FILES ARE COPIED...!"
     fi
else
        echo "All files are copied....."
fi
