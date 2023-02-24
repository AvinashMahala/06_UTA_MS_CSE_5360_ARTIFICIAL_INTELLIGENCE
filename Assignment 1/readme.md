---------------------------------------------------
Name     					- Avinash Mahala

UTA ID   					- 1002079433

Programming Language Used	- Python 3.9.7

---------------------------------------------------
How the Code is Structured?
---------------------------------------------------
All the Code files are in the same directory[1002079433].
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

"expense_8_puzzle.py <start-file> <goal-file> <method> <dump-flag>"

<start-file> and <goal-file> are required.

 <method> can be
	bfs - Breadth First Search
	ucs - Uniform Cost Search
	dfs - Depth First Search
	dls - Depth Limited Search (Note: Depth Limit will be obtained as a Console Input) [Note: This part is EC for CSE 4308 students]
	ids - Iterative Deepening Search [Note: This part is EC for CSE 4308 students]
	greedy - Greedy Seach
	a* - A* Search (Note: if no <method> is given, this should be the default option)
	
	If <dump-flag>  is given as true, search trace is dumped for analysis in <algorithmName>_trace-<date>-<time>.txt (Note: if <dump-flag> is not given, it is false by default)
------------------------------------------------------------------------------------------------------
