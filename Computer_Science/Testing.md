Behavior-Driven Development- TDD with user stories incorporated
Stubbing- Defining mock functions/classes with expected outputs to DRY test code

-Good testing acts as documentation and reduces the incidence of bugs
-Test the result of a function, not its line-by-line implementation

Testing Considerations:
	-What methods/functions do you need?
		-What are their expected outputs?
	-What classes are needed?
	-What needs to happen? (Errors, methods called, etc.)

Testing Flow:
	1. Write a test for what you want your code to accomplish
	2. Run the test and watch it fail
	3. Write code to pass the test
	4. Refactor code
	5. Repeat steps 1-4 as necessary

-Unit ests should be kept DRY by focusing only on individual classes
Integration- Verify that units work together. These tests run slower and are harder to refactor due to multiple dependencies

For MVCs:
Unit- Models
Integration/Service - Controller
UI - End to End

Travis-CI:
	CI enables better control over a project.
	Automated tests prevent buggy code from being merged
	Auto-merging can be used to speed up work.
	-Create travis.yml at project root and specify language
	-Github tags specify code release versions