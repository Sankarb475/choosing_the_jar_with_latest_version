# choosing_the_jar_with_latest_version

We faced this issue while deploying/running our spark jar in production.
Our spark job launcher shell script picks up the jar name from a given directory and runs the spark application, but the jar 
gets created and deployed in that directory through an automated process and the version of the spark application changes 
frequently, because we are continuously upgrading, improving and optimizing our spark application code and giving it a new 
version.

So for the spark job launcher shell script to find the latest jar from the given directory, I created this python script 
which gets triggered from the shell script to find the jar we need to run.
