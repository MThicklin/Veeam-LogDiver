# LogDiver
A Veeam Log diver that pulls warning and error entries from VB&R logs.

Functions of Log diver:

Crawl
For ease of use, LogDiver is designed so logs can be copied into the LogDiver folder and it will crawl through the directory for logs.

Clean
The clean function removes all the files log diver created.  Clean doesn't touch any other files other then the .txt logdiver makes.

Stow
The stow function is set up to move both .log and .txt files into a folder you name.  This is so you don't have to recrawl over logs if you want to revisit files from a previous sesison of logdiver.

Stow4me
A stow function that displays the folders available in the logdiver directory and ask user where the files should go.

Nuke
The nuke function will delete all .log and .txt files out of the logdiver folder.  This acts as a reset if you no longer need any of the files.

VMC
The VMC function is still under construction, It's goal will be to make the VMC.log more readable.  Future features include being able to run system requirement calculations and note differences between the infrastructure by day.

Little bit of back story
I worked as a contractor for Veeam for a few months and made this program to help get to the errors in the logs faster.  Overall, I think the program is pretty good and I wanted to share that good with others who may want to get a look behind the scenes in the logs for Veeam.
