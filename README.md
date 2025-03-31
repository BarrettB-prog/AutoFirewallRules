HIGH POSSIBILITY OF FALSE POSITIVES

The script pulls IPs related to C2 traffic from abuse.ch, however, it pulls from the unverified list, creating a possibility for false positives.

The script also removes previous 'BadIP' rules, so if run once in January and again in May, it will delete all January IPs, and overwrite with those currently on the list in May.
! Does not remove all other firewall rules, just those added from he script, variable name 'BadIP' !

Regex statement added to prevent (however unlikely) Remote Code Execution (RCE). Now checks to insure only IPs are able to be added.
