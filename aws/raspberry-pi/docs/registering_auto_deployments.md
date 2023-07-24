[Docs referenced from here](https://aws.amazon.com/blogs/devops/automating-deployments-to-raspberry-pi-devices-using-aws-codepipeline/)

```sh
sudo aws configure
...

# register instance as a codedeploy instance
sudo aws deploy register --instance-name <instance name> --iam-user-arn arn:aws:iam::<AWS_ACCOUNT_ID>:user/<name of user> --tags Key=Name,Value=<name of user> --region <region>

# Install CodeDeploy agent
sudo aws deploy install --override-config --config-file /etc/codedeploy-agent/conf/codedeploy.onpremises.yml --region <region>

# OPTIONAL: Fallback to install missing dependencies
sudo apt-get install ruby
sudo wget https://aws-codedeploy-us-west-2.s3.amazonaws.com/latest/install
sudo chmod +x ./install
sudo ./install auto

# Diagnostic
sudo service codedeploy-agent status

# Start agent
sudo service codedeploy-agent start
```