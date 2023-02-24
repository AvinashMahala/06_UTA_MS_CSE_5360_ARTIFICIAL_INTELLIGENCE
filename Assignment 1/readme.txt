---------------------------------------------------
Name     					- Avinash Mahala
UTA ID   					- 1002079433
Programming Language Used	- Python 3.9.7
---------------------------------------------------

Device Specifications:-
---------------------------------------------------
Processor	        Intel(R) Core(TM) i5-9300H CPU @ 2.40GHz   2.40 GHz
Installed RAM	    24.0 GB (23.8 GB usable)
System type	        64-bit operating system, x64-based processor
Pen and touch	    No pen or touch input is available for this display
Manufacturer		Acer
Device Model		Nitro AN517-51
---------------------------------------------------
Windows(Operating System) Specifications:-
---------------------------------------------------
Edition	      	Windows 11 Home Single Language Version	21H2
Installed on	‎Sat-‎30-‎Oct-‎2021
OS build		22000.1219
Experience		Windows Feature Experience Pack 1000.22000.1219.0
---------------------------------------------------
Python Used  	Version 3.9.7
---------------------------------------------------
---------------------------------------------------
How the Code is Structured?
---------------------------------------------------
All the Code files are in the same directory[].
There is only one more directory called "trace_logs"
[if not present will be created at runtime when the 
<dump-flag> is marked as true] which 
will contain all the trace log files for all the searches.
---------------------------------------------------

How to run the Code?
------------------------------------------------------------------------------------------------------
1. Copy the unzipped contents to a new folder named "1002079433".
2. Open Windows Terminal in this directory.[Make sure to install 
	Python before this step as per the version mentioned above and set the same as 
	environment variable(This will enable python command to run from Windows Command Window)].
3. Run the Below Commands as required in order to see the desired output and trace logs:-

expense_8_puzzle.py <start-file> <goal-file> <method> <dump-flag>

<start-file> and <goal-file> are required.

 <method> can be
	bfs - Breadth First Search
	ucs - Uniform Cost Search
	dfs - Depth First Search
	dls - Depth Limited Search (Note: Depth Limit is obtained as a Console Input[If not provided There is a default value set.])
	ids - Iterative Deepening Search
	greedy - Greedy Seach
	a* - A* Search (Note: if no <method> is given, this should be the default option)
	
	If <dump-flag>  is given as true, search trace is dumped for analysis in 
	<algorithmName>_trace-<date>-<time>.txt (Note: if <dump-flag> is not given, it is false by default)
------------------------------------------------------------------------------------------------------