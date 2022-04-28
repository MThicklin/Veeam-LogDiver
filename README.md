# Veeam LogDiver aka LogDiver
A Log diver that pulls warning and error entries from VB&R logs.

LogDiver isn't meant to replace troubleshooting but make it esier to locate the errors inside the logs.

## Using LogDiver
Basic LogDiver use:  
-Ensure you have at least Python 3.9 installed.  
-Download the code and extract where you want.  
-Copy your Veeam Logs into the folder.  
-Finally open a command prompt inside the log dive directory.
-Type 'python logdiver.py crawl'  
-Logdiver will output a .txt file named after each of the logs found with the line numbers of the errors / warnings from the original log files.

Other functions are listed below.  You can run them with 'python logdiver.py <function losted below>'.

## Functions of Log diver:

crawl  
For ease of use, LogDiver is designed so logs can be copied into the LogDiver folder and it will crawl through the directory for logs.  After LogDiver crawls through the directory, it will output a text file with the errors / warnings and their line numbers so you can open the original log file and know where the entries are located.

clean  
The clean function removes all the files log diver created.  Clean doesn't touch any other files other then the .txt logdiver makes.  If you accidentally clean your files too early, you still have th option to run crawl agian.

nuke  
The nuke function will delete all .log and .txt files out of the logdiver folder.  This acts as a reset if you no longer need any of the files.  This function has a safety where the user must YES (All CAPS) to activate.

stow  
The stow function is set up to move both .log and .txt files into a folder you name.  This is so you don't have to recrawl over logs if you want to revisit files from a previous sesison of logdiver.

stow4me  
A stow function that displays the folders available in the logdiver directory and ask user where the files should go.

vmc  
The VMC function is still under construction, It's goal will be to make the VMC.log more readable.
