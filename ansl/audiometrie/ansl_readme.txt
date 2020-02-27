Welcome to the ANSL-toolbox!

This readme should provide all the necessary info on how to operate the ANSL-experiment, for Information on the stimuli (and units) used and how the graphs are created look into the provided jupyter notebooks. If there are further open questions feel free to message me at m.earnest211@gmail.com or on github.

Requirements:
- A working version of pyhton2 (https://www.python.org/downloads/)
	- additionaly you'll need some software libraries(primarily librosa(https://pypi.org/project/librosa/))
	  that the standard distribution does not contain, especially when working with the provided jupyter notebooks for analysis and stimuli preparation
- The psychopy toolbox (version 1.85.4) (https://github.com/psychopy/psychopy/releases/tag/1.85.4)

- before running the experiment make sure that you have downloaded the folders "plotting" and "stimuli" and added them to the same directory as the ansl.py script


The ANSL_experiment:
- Can be opened either via psychopy or via commandline on unix-systems with the command -> python2 ansl.py

- Once started you will be prompted to input a subject-id for which then an additional folder will be created under /ansl/data/

- Next a graphical user interface should pop up, asking you to specify which acquisition protocol you want to run (e.g. baseline, epi, mprage)
	- the order in which you'll run the experiment is up to you and every condition can be repeated indefinetly

- After you've choosen which acquisition protocol you want to run from the dropdown menu hit ok and another window 
	should pop-up asking you if you'll want run all stimuli in all possible orders of frequency and volume progression
	-> if you answer yes (approximately 7-13 minutes depending on particpants response time)
		-> the experiment will start and present the stimuli in 4 different blocks
		  (ascending in frequency and increasing in volume, descending in frequency and increasing in volume etc.)
	-> if you answer no: (approximately 2-3 minutes depending on particpants response time)
		-> another window will pop up prompting you to specify which combination of frequency and volume progression
		   you want to present (resulting in one block of stimuli presentation)

- At the beginning of every block the experiment will wait until it has registered 3 trigger from your mri, meaning you need to receive the trigger-signal as a keyboard input.
  For the baseline condition (or testing purposes or if setting up the trigger input is too much of a hassle) it is necessary that you provide that input yourself by pressing
  "t" 3 times on your keyboard.
	-> standard is assigning to the "t"-key to the trigger
	  (this can be changed to whatever is convenient for you by simply exchanging the "t" in "theseKeys = event.getKeys('t')" at line 110 and 460 of the ansl.py file)

- The participant than has to indicate wether a tone becomes audible/inaudible for one trial by pressing the "7" key
  (again this can be changed in the script by exchanging the "7" in lines 184, 185, 198, 211, 519, 520, 536 and 549)

- After a block or trial was completed the user interface will reapear and prompt you to choose another condition

- If you're finished with the experiment simply click cancel or hit the esc-key, which will output a series of pngs
  containing the results of your participant in addition to the .tsv files containing the raw-data






