
The file `picofssd` in this directory gets copied into
/etc/default if the server is to be started by SysVInit.

It provides overrides for the server options:

* PIDFILE
* LOGLEVEL
* VERBOSE

Set these values like this:

* PIDFILE

By default set to `/var/run/picofssd.pid`.

Probably doesn't need changing unless the user is trying to set up the `picofssd` to run on an OS 
other than Raspbian, which may not have the `/var/run/` path.

* LOGLEVEL

Set to either `info` or `debug`.

Affects filtering of `syslog` messages.

* VERBOSE

Set to some string value other than 'no' to have start and stop messages written to 
`/var/log/daemon.log` by the init system.



