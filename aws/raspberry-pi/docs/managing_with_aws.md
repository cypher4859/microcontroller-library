Method to do it ([referenced from here for SSM](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-install-managed-linux.html) and [from this tutorial](https://dev.to/aws-builders/managing-on-prem-systems-with-systems-manager-a-hands-on-guide-4c6g)):
1. Setup a raspberry pi with MicroSD that has Ubuntu Server installed (preferred v22 or LTS)
2. Plug it in, you'll need the peripherals for the beginning setup
3. Add the following snippet into `/etc/netplan/wireless.yml`:
```yaml
network:
  version: 2
  wifis:
    wlan0:
      dhcp4: yes
      dhcp6: no
      access-points:
        "<your network ESSID>":
	        password: "<your wifi password>"
```
4. do a `sudo netplan try`
5. confirm with a `ping google.com` (I had to restart after doing the netplan)
6. Do following SSM agent setup
```sh
sudo snap install amazon-ssm-agent --classic
sudo systemctl stop snap.amazon-ssm-agent.amazon-ssm-agent.service
sudo /snap/amazon-ssm-agent/current/amazon-ssm-agent -register -code "activation-code" -id "activation-id" -region "region" 
sudo systemctl start snap.amazon-ssm-agent.amazon-ssm-agent.service
```
7. You're done!

From here you should be able to do standard connects like:
```sh
aws ssm start-session --target <target instance>
```