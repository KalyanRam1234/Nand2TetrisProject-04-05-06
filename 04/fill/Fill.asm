// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(OUT)
@16384
D=A
@SCREEN
A=D
@counter
M=0
D=0
(LOOP)
	@SCREEN
	A=A+D
	M=-1
	D=A
	@24575
	D=D-A
	@OUT
	D;JGT
	(NOTPRESS)	
		@24576
		D=M
		@WHITE
		D;JEQ
	@counter
	M=M+1
	D=M
	@LOOP
	0;JMP
(WHITE)
	@16384
	D=A
	@SCREEN
	A=D
	@counter
	M=0
	D=0
	(WHILE)
		@SCREEN
		A=A+D
		M=0
		D=A
		@24575
		D=D-A
		@WHITE
		D;JGT
		(PRESS) 
			@24576  
			D=M
			@OUT
			D;JGT  
		@counter
		M=M+1
		D=M
		@WHILE
		0;JMP