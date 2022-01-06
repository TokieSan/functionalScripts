echo 2133309 > /var/run/rsnapshot.pid 
/usr/bin/rm -rf /.snapshots/weekly.3/ 
mv /.snapshots/weekly.2/ /.snapshots/weekly.3/ 
mv /.snapshots/weekly.1/ /.snapshots/weekly.2/ 
/usr/bin/cp -al /.snapshots/weekly.0 /.snapshots/weekly.1 
/usr/bin/rsync -a --delete --numeric-ids --relative --delete-excluded /etc/ \
    /.snapshots/weekly.0/localhost/ 
/usr/bin/rsync -a --delete --numeric-ids --relative --delete-excluded \
    /usr/local/ /.snapshots/weekly.0/localhost/ 
/usr/bin/rsync -a --delete --numeric-ids --relative --delete-excluded \
    /etc/passwd /.snapshots/weekly.0/localhost/ 
/usr/bin/rsync -a --delete --numeric-ids --relative --delete-excluded \
    /home/elt0khy/Documents/ /.snapshots/weekly.0/localhost/ 
/usr/bin/rsync -a --delete --numeric-ids --relative --delete-excluded \
    /home/elt0khy/.shoosh/ /.snapshots/weekly.0/localhost/ 
/usr/bin/rsync -a --delete --numeric-ids --relative --delete-excluded \
    /home/elt0khy/.config/ /.snapshots/weekly.0/localhost/ 
touch /.snapshots/weekly.0/ 
