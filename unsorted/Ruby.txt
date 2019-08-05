Keywords:
	initialize- Constructor method
	extend- Include module functions as class methods
	include- Include module functions as instance methods
	private- Restricts access to method in interface
	super- Runs equivalent parent class method (e.g. initialize)
	yield- for accepting a proc
	&- added alongside variable name to tell function to expect a proc or pass one
		-In a definition: makes a block a proc
		-In a method call: makes a proc a block
		proc.call to call the proc (remember to pass it arguments)
	ARGV- keyword to return an array of strings typed after a script name in the terminal
	< for establishing exception hierarchy
	inspect- Method for outputting unique hash for an object
		-Custom inspect methods useful for generating readable output
	<=> - Spaceship operator
		1 if right value is greater
		0 if two values are equal
		-1 if left is greater value

Exception Handling:
	begin
	rescue Error => e # to handle exception, Error for specific exception or its subclass
	retry # restarts begin block if triggered
	ensure # this code always executes
	end

-Modules take primacy in method calls over classes
-Avoid defining instance variables outside of the constructor for cleaner code

(Check if == is an object comparison)

RSPEC Basic Syntax:
	Context _condition_ *For nesting describes
		Describe _condition_ *For gathering related unit tests
			it _does_something_ *The unit test
				expect _result_ *Evaluates code
	let keyword persists a variable across describe blocks
	rspec --init to start
