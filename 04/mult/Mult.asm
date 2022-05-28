// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
@product
M=0
(LOOP)
	@0
	D=M
	@END
	D;JEQ
	@1
	D=M
	@product
	M=M+D
	@0
	M=M-1
	@LOOP
	0;JMP
(END)
	@product
	D=M
	@2
	M=D
(TERMINATE)
	@TERMINATE
	0;JMP