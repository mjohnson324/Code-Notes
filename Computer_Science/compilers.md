Compilers:
	Just In Time- Compilation on the fly
		Deoptimization aka "Bailing Out-" when compiled code is discarded to avoid errors
	Type Specialization- when a compiler assumes a specific data type
	-Interpreters run loops slowly because they must re-read the same code
	-Compilers can optimize code for runtime speed
	-Code which runs repeatedly sent to Baseline Compiler
	-BC does not focus on optimization to prevent delays in execution
	-Optimizing Compiler creates fast code for code that runs many times
	-Repeat optimizations/deoptimizations are slower than pure baseline compilation

	Assembly Language- symbolic machine code
		a. Thinking: Arithmetic Logic Unit (the workhorse)
		b. Short-term memory: Registers (in the cpu, separate processes)
		c. Long-term memory: RAM
	Intermediate Representation- Code that exists between assembly and high-level languages
	-Intermediate representations prevent the need to translate every language to machine-specific assembly
	-Machine code instructions have opcodes (operation) dictating ALU operations
		Example: 111 010101 001 010: 010101 = add, 001 = R1, 010 = R2 (add R1 & R2)
	-Every machine architecture has its own machine code

Decompiler: Program which converts an executable back into source  cod 
