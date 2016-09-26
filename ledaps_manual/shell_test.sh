#!/bin/bash


# Name the Scene in the data folder
echo "Please paste the Landsat Scene ID to process. (example: LT41760361990224XXX03)"
read sceneID

## declare an array variable
declare -a arr=($sceneID)

## now loop through the above array
for i in "${arr[@]}"
do
  # or do whatever with individual element of the array
  echo  "Processing $i"
done

# You can access them using echo "${arr[0]}", "${arr[1]}" also
