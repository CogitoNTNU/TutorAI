""" The service module contains the business logic of the application. """

from django.core.files.uploadedfile import InMemoryUploadedFile
from flashcards.rag_service import post_context
from flashcards.knowledge_base.factory import create_database
from flashcards.knowledge_base.factory import create_embeddings_model
from flashcards.text_to_flashcards import Flashcard, generate_flashcards
from knowledge_base.db_interface import MongoDB
from knowledge_base.response_formulation import response_formulation 
from knowledge_base.db_interface import MongoDB, get_page_range
#from flashcards.knowledge_base import 

mongodb = MongoDB()



def process_flashcards(uploaded_file: InMemoryUploadedFile) -> list[Flashcard]:
    """
    Process the files and return the flashcards.
    """
    print("[INFO] Processing file", flush=True)

    # Extract text from the uploaded file
    # TODO: Use the scraper to extract the text from the uploaded file
    
    context: str = """
xv6: a simple, Unix-like teaching operating system

Russ Cox Frans Kaashoek Robert Morris

August 31, 2020


Contents

1 Operating system interfaces

1.1 Processesandmemory .......... 2.0... eee ee
1.2 WOand File descriptors... .......0 2.0.00. ee ee ee
13 Pipes... . ee
14 Filesystem .... 2... ... 2... ee
1.5  Realworld... 2... 2... 0.2.00. 0000000 22 eee
16 Exercises 2... ee

2 Operating system organization

2.1 Abstracting physical resources .... 2... 0... ee ee
2.2 User mode, supervisor mode, and systemcalls...................-,
2.3. Kernelorganization ..... 2... 2... ee
2.4 Code: xv6 organization... 2... 2. ee
2.5 Process overview ... 2...
2.6 Code: starting xv6 and the first process... 2... 2... 2... eee eee es
2.7 Realworld..... 2.2... 0.20. ee
2.8 Exercises 2...

3 Page tables

3.1 Paginghardware ........ 0... 2, ee
3.2 Kerneladdress space .... 2.2... 2. ee
3.3 Code: creating an address space... 2... 1 ee
3.4 Physical memory allocation. ....... 2.2... 0.00 0c eee ee ee
3.5 Code: Physical memory allocator... 2... 2... 0. ee ee ee
3.6 Process address space... 2...
3.7 Code:sbrk. 2... ee ee
3.8 Code:exec.. 2... ee
3.9 Realworld... 2... 0.0... 200.2000 2 2 ee ee
3.10 Exercises 2... ee

4 Traps and system calls
4.1 RISC-V trap machinery. .............. 0.00.00 00000022.
4.2 Traps fromuser space... 2... 2... ee

10
13
15
17
19
20

4.3 Code: Calling systemcalls .. 2... 2... 0.020200 02 eee ee ee ees
4.4 Code: Systemcallarguments ...........0. 02.0002 eee eee eee
4.5 Traps fromkernel space... . 2... 2... ee
4.6 Page-faultexceptions ... 2... 2.0... 0. ee ee
4.7 Realworld.. 2... 2. ee
4.8 Exercises 2...
Interrupts and device drivers

5.1 Code: Console input ............ 0... 0.02 eee eee es
5.2 Code: Console output... 2... ee ee
5.3. Concurrency indrivers ... 2... 2... 2. ee
5.4 Timerinterrupts.. 2... 2.0... ee
5.5 Realworld..... 20.20.20. 0. 02 ee ee
5.6 Exercises 2... .
Locking

6.1 Raceconditions .... 2... 2.0... 2.0. ee ee
6.2 Code: Locks... 2... 2. ee
6.3. Code: Using locks... .......0 0.0202 02 ee ees
6.4 Deadlock and lock ordering... .........0.. 2.00002 e ee eee ees
6.5 Locks andinterrupthandlers ............... 0.020002 eee eee
6.6 Instruction and memory ordering ............... 020202 eee eee
6.7 Sleeplocks ..... 2.2.0.0... 0. ee ee
6.8 Realworld.... 2... 2.0.20... 0. ee ee
6.9 Exercises . 2...
Scheduling

7.1 Multiplexing ... 2.2... 2.0... 0.200202 ee ee
7.2 Code: Context switching .......... 0... 0.00 eee ee ee es
7.3. Code: Scheduling... 2... 2... 2. ee ee
7.4 Code: mycpuandmyproc............ 0.000 eee ee
7.5 Sleepand wakeup... ....... 0.0. 0 ee ee
7.6 Code: Sleep and wakeup ...........0. 02.0000 eee eee ee ees
7.7 Code: Pipes .. 2... 2 2.
7.8 Code: Wait, exit,andkil .... 2... 2.0.0.0. 0.0.00 2.020200 0004
7.9 Realworld.... 2... 20.20... 0. ee
7.10 Exercises 2... .

File system

8.1
8.2
8.3
8.4

Overview .. 2...
Buffer cache layer... 2... ee
Code: Buffercache .. 1... 2... 2 ee ee
Logging layer... 1.

49
49
50
51
51
52
53

55
56
58
60
60
62
62
63
64
64

67
67
68
69
70
71
74
75
76
77
79

8.5 Logdesign ... 2... . 0. ee 85

8.6 Code: logging... 2... 2 ee 86
8.7 Code: Block allocator... 2... 2 ee 87
8.8 Inodelayer .... 2... . ee 87
8.9 Code: Inodes ... 2... 0... ee 89
8.10 Code: Inode content... 2... 2... 90
8.11 Code: directory layer... 2... ee 91
8.12 Code: Pathnames ... 2... . 92
8.13 File descriptor layer... 2... ee 93
8.14 Code: Systemcalls . 2... 0.0.0.0. 02 ee ee 94
8.15 Real world. 2... 95
8.16 Exercises 2... 96
9 Concurrency revisited 99
9.1 Locking patterns .. 2... 2... ee ee 99
9.2 Lock-like patterns... 2... 2 ee 100
9.3 Nolocksatall... 2... . 0 0. eee 100
9.4 Parallelism .. 2... 101
9.5 ExerciseS 2... 102
10 Summary 103


Foreword and acknowledgments

This is a draft text intended for a class on operating systems. It explains the main concepts of
operating systems by studying an example kernel, named xv6. xv6 is modeled on Dennis Ritchie�s
and Ken Thompson�s Unix Version 6 (v6) [14]. xv6 loosely follows the structure and style of v6,
but is implemented in ANSI C [6] for a multi-core RISC-V [12].

This text should be read along with the source code for xv6, an approach inspired by John Li-
ons� Commentary on UNIX 6th Edition [9]. See https://pdos.csail.mit.edu/6.S081
for pointers to on-line resources for v6 and xv6, including several lab assignments using xv6.

We have used this text in 6.828 and 6.S081, the operating systems classes at MIT. We thank the
faculty, teaching assistants, and students of those classes who have all directly or indirectly con-
tributed to xv6. In particular, we would like to thank Adam Belay, Austin Clements, and Nickolai
Zeldovich. Finally, we would like to thank people who emailed us bugs in the text or sugges-
tions for improvements: Abutalib Aghayev, Sebastian Boehm, Anton Burtsev, Raphael Carvalho,
Tej Chajed, Rasit Eskicioglu, Color Fuzzy, Giuseppe, Tao Guo, Naoki Hayama, Robert Hilder-
man, Wolfgang Keller, Austin Liew, Pavan Maddamsetti, Jacek Masiulaniec, Michael McConville,
m3hm00d, miguelgvieira, Mark Morrissey, Harry Pan, Askar Safin, Salman Shah, Adeodato Sim6,
Ruslan Savchenko, Pawel Szczurko, Warren Toomey, tyfkda, tzerbib, Xi Wang, and Zou Chang
Wei.

If you spot errors or have suggestions for improvement, please send email to Frans Kaashoek
and Robert Morris (kaashoek,rtm @csail.mit.edu).


Chapter 1

Operating system interfaces

The job of an operating system is to share a computer among multiple programs and to provide a
more useful set of services than the hardware alone supports. An operating system manages and
abstracts the low-level hardware, so that, for example, a word processor need not concern itself
with which type of disk hardware is being used. An operating system shares the hardware among
multiple programs so that they run (or appear to run) at the same time. Finally, operating systems
provide controlled ways for programs to interact, so that they can share data or work together.

An operating system provides services to user programs through an interface. Designing a good
interface turns out to be difficult. On the one hand, we would like the interface to be simple and
narrow because that makes it easier to get the implementation right. On the other hand, we may be
tempted to offer many sophisticated features to applications. The trick in resolving this tension is to
design interfaces that rely on a few mechanisms that can be combined to provide much generality.

This book uses a single operating system as a concrete example to illustrate operating system
concepts. That operating system, xv6, provides the basic interfaces introduced by Ken Thompson
and Dennis Ritchie�s Unix operating system [14], as well as mimicking Unix�s internal design.
Unix provides a narrow interface whose mechanisms combine well, offering a surprising degree
of generality. This interface has been so successful that modern operating systems�BSD, Linux,
Mac OS X, Solaris, and even, to a lesser extent, Microsoft Windows�have Unix-like interfaces.
Understanding xv6 is a good start toward understanding any of these systems and many others.

As Figure 1.1 shows, xv6 takes the traditional form of a kernel, a special program that provides
services to running programs. Each running program, called a process, has memory containing
instructions, data, and a stack. The instructions implement the program�s computation. The data
are the variables on which the computation acts. The stack organizes the program�s procedure calls.
A given computer typically has many processes but only a single kernel.

When a process needs to invoke a kernel service, it invokes a system call, one of the calls in
the operating system�s interface. The system call enters the kernel; the kernel performs the service
and returns. Thus a process alternates between executing in user space and kernel space.

The kernel uses the hardware protection mechanisms provided by a CPU! to ensure that each

'This text generally refers to the hardware element that executes a computation with the term CPU, an acronym
for central processing unit. Other documentation (e.g., the RISC-V specification) also uses the words processor, core,
and hart instead of CPU.

Figure 1.1: A kernel and two user processes.

process executing in user space can access only its own memory. The kernel executes with the
hardware privileges required to implement these protections; user programs execute without those
privileges. When a user program invokes a system call, the hardware raises the privilege level and
starts executing a pre-arranged function in the kernel.

The collection of system calls that a kernel provides is the interface that user programs see. The
xv6 kernel provides a subset of the services and system calls that Unix kernels traditionally offer.
Figure 1.2 lists all of xv6�s system calls.

The rest of this chapter outlines xv6�s services�processes, memory, file descriptors, pipes,
and a file system�and illustrates them with code snippets and discussions of how the shell, Unix�s
command-line user interface, uses them. The shell�s use of system calls illustrates how carefully
they have been designed.

The shell is an ordinary program that reads commands from the user and executes them. The
fact that the shell is a user program, and not part of the kernel, illustrates the power of the system
call interface: there is nothing special about the shell. It also means that the shell is easy to replace;
as a result, modern Unix systems have a variety of shells to choose from, each with its own user
interface and scripting features. The xv6 shell is a simple implementation of the essence of the
Unix Bourne shell. Its implementation can be found at (user/sh.c:1).

1.1 Processes and memory

An xv6 process consists of user-space memory (instructions, data, and stack) and per-process
state private to the kernel. Xv6 time-shares processes: it transparently switches the available CPUs
among the set of processes waiting to execute. When a process is not executing, xv6 saves its CPU
registers, restoring them when it next runs the process. The kernel associates a process identifier,
or PID, with each process.

A process may create a new process using the fork system call. Fork creates a new process,
called the child process, with exactly the same memory contents as the calling process, called
the parent process. Fork returns in both the parent and the child. In the parent, fork returns the
child�s PID; in the child, fork returns zero. For example, consider the following program fragment
written in the C programming language [6]:

int pid = fork();
if (pid > 0){
printf ("parent: child=%d\n", pid);

10

System call

int forkQ)

int exit(int status)
int wait(int *status)
int kill(int pid)

int getpid()

int sleep(int n)

Description

Create a process, return child�s PID.

Terminate the current process; status reported to wait(). No return.
Wait for a child to exit; exit status in *status; returns child PID.
Terminate process PID. Returns 0, or -1 for error.

Return the current process�s PID.

Pause for n clock ticks.

int exec(char *file, char *argv[]) Load a file and execute it with arguments; only returns if error.

char *sbrk(int n)

Grow process�s memory by n bytes. Returns start of new memory.

int open(char �file, int flags) Open a file; flags indicate read/write; returns an fd (file descriptor).
int write(int fd, char *buf, intn) Write n bytes from buf to file descriptor fd; returns n.
int read(int fd, char *buf, intn) | Read n bytes into buf; returns number read; or 0 if end of file.

int close(int fd)

int dup(int fd)

int pipe(int p[])

int chdir(char *dir)
int mkdir(char *dir)

Release open file fd.

Return a new file descriptor referring to the same file as fd.
Create a pipe, put read/write file descriptors in p[O] and p[1].
Change the current directory.

Create a new directory.

int mknod(char *file, int, int) Create a device file.

int fstat(int fd, struct stat *st) Place info about an open file into *st.

int stat(char �file, struct stat *st) Place info about a named file into *st.

int link(char *filel, char *file2) | Create another name (file2) for the file file1.

int unlink(char *file)

Remove a file.

Figure 1.2: Xv6 system calls. If not otherwise stated, these calls return 0 for no error, and -1 if

there�s an error.

pid = wait((int *) 0);

printf ("chil

} else if (pid

printf ("chil
exit (0);
} else {

d %d is done\n", pid);
== 0){

ld: exiting\n");

printf ("fork error\n");

}

The exit system call causes the calling process to stop executing and to release resources such as

memory and open files.

Exit takes an integer status argument, conventionally 0 to indicate success

and | to indicate failure. The wait system call returns the PID of an exited (or killed) child of

the current process and

copies the exit status of the child to the address passed to wait; if none of

the caller�s children has exited, wait waits for one to do so. If the caller has no children, wait

immediately returns -1.

address to wait.

If the parent doesn�t care about the exit status of a child, it can pass a 0

In the example, the output lines

11

parent: child=1234
child: exiting

might come out in either order, depending on whether the parent or child gets to its printf call
first. After the child exits, the parent�s wait returns, causing the parent to print

parent: child 1234 is done

Although the child has the same memory contents as the parent initially, the parent and child are
executing with different memory and different registers: changing a variable in one does not affect
the other. For example, when the return value of wait is stored into pid in the parent process, it
doesn�t change the variable pid in the child. The value of pid in the child will still be zero.

The exec system call replaces the calling process�s memory with a new memory image loaded
from a file stored in the file system. The file must have a particular format, which specifies which
part of the file holds instructions, which part is data, at which instruction to start, etc. xv6 uses the
ELF format, which Chapter 3 discusses in more detail. When exec succeeds, it does not return
to the calling program; instead, the instructions loaded from the file start executing at the entry
point declared in the ELF header. Exec takes two arguments: the name of the file containing the
executable and an array of string arguments. For example:

char xargv[3];

argv[0] = "echo";
argv[1] = "hello";
argv[2] = 0;

exec ("/bin/echo", argv);
printf ("exec error\n");

This fragment replaces the calling program with an instance of the program /bin/echo running
with the argument list echo hello. Most programs ignore the first element of the argument array,
which is conventionally the name of the program.

The xv6 shell uses the above calls to run programs on behalf of users. The main structure of
the shell is simple; see main (user/sh.c:145). The main loop reads a line of input from the user with
getcmd. Then it calls fork, which creates a copy of the shell process. The parent calls wait,
while the child runs the command. For example, if the user had typed �echo hello� to the shell,
runcmd would have been called with �echo hello� as the argument. runcmd (user/sh.c:58) runs
the actual command. For �echo hello�, it would call exec (user/sh.c:78). If exec succeeds then
the child will execute instructions from echo instead of runcmd. At some point echo will call
exit, which will cause the parent to return from wait in main (user/sh.c:145).

You might wonder why fork and exec are not combined in a single call; we will see later that
the shell exploits the separation in its implementation of I/O redirection. To avoid the wastefulness
of creating a duplicate process and then immediately replacing it (with exec), operating kernels
optimize the implementation of fork for this use case by using virtual memory techniques such
as copy-on-write (see Section 4.6).

Xv6 allocates most user-space memory implicitly: fork allocates the memory required for the
child�s copy of the parent�s memory, and exec allocates enough memory to hold the executable

12

file. A process that needs more memory at run-time (perhaps for malloc) can call sbrk (n) to
grow its data memory by n bytes; sbrk returns the location of the new memory.

1.2 W/O and File descriptors

A file descriptor is a small integer representing a kernel-managed object that a process may read
from or write to. A process may obtain a file descriptor by opening a file, directory, or device,
or by creating a pipe, or by duplicating an existing descriptor. For simplicity we�ll often refer
to the object a file descriptor refers to as a �file�; the file descriptor interface abstracts away the
differences between files, pipes, and devices, making them all look like streams of bytes. We�ll
refer to input and output as //O.

Internally, the xv6 kernel uses the file descriptor as an index into a per-process table, so that
every process has a private space of file descriptors starting at zero. By convention, a process reads
from file descriptor 0 (standard input), writes output to file descriptor 1 (standard output), and
writes error messages to file descriptor 2 (standard error). As we will see, the shell exploits the
convention to implement I/O redirection and pipelines. The shell ensures that it always has three
file descriptors open (user/sh.c:151), which are by default file descriptors for the console.

The read and write system calls read bytes from and write bytes to open files named by file
descriptors. The call read (fd, buf, n) reads at most n bytes from the file descriptor fd, copies
them into buf, and returns the number of bytes read. Each file descriptor that refers to a file has an
offset associated with it. Read reads data from the current file offset and then advances that offset
by the number of bytes read: a subsequent read will return the bytes following the ones returned
by the first read. When there are no more bytes to read, read returns zero to indicate the end of
the file.

The call write (fd, buf, n) writes n bytes from buf to the file descriptor fd and returns the
number of bytes written. Fewer than n bytes are written only when an error occurs. Like read,
write writes data at the current file offset and then advances that offset by the number of bytes
written: each write picks up where the previous one left off.

The following program fragment (which forms the essence of the program cat) copies data
from its standard input to its standard output. If an error occurs, it writes a message to the standard
error.

char buf[512];
int n;

for(;;){
n = read(0, buf, sizeof buf);
if(n == 0)
break;
if(n < 0){
fprintf(2, "read error\n");
exit(1);

13

if(write(l1, buf, n) !=n)f
fprintf(2, "write error\n");
exit(1);

}

The important thing to note in the code fragment is that cat doesn�t know whether it is reading
from a file, console, or a pipe. Similarly cat doesn�t know whether it is printing to a console, a
file, or whatever. The use of file descriptors and the convention that file descriptor 0 is input and
file descriptor 1 is output allows a simple implementation of cat.

The close system call releases a file descriptor, making it free for reuse by a future open,
pipe, or dup system call (see below). A newly allocated file descriptor is always the lowest-
numbered unused descriptor of the current process.

File descriptors and fork interact to make I/O redirection easy to implement. Fork copies
the parent�s file descriptor table along with its memory, so that the child starts with exactly the
same open files as the parent. The system call exec replaces the calling process�s memory but
preserves its file table. This behavior allows the shell to implement //O redirection by forking, re-
opening chosen file descriptors in the child, and then calling exec to run the new program. Here
is a simplified version of the code a shell runs for the command cat < input.txt:

char xargv[2];

argv[0] = "cat";
argv[1] = 0;
if (fork() == 0) {

close (0);
open ("input.txt", O_RDONLY) ;
exec("cat", argv);

}

After the child closes file descriptor 0, open is guaranteed to use that file descriptor for the newly
opened input.txt: 0 will be the smallest available file descriptor. cat then executes with file
descriptor 0 (standard input) referring to input .t xt. The parent process�s file descriptors are not
changed by this sequence, since it modifies only the child�s descriptors.

The code for I/O redirection in the xv6 shell works in exactly this way (user/sh.c:82). Recall that
at this point in the code the shell has already forked the child shell and that runcmd will call exec
to load the new program.

The second argument to open consists of a set of flags, expressed as bits, that control what
open does. The possible values are defined in the file control (fcntl) header (kernel/fentl.h:1-5):
O_RDONLY, O_WRONLY, O_RDWR, O_CREATE, and O_TRUNC, which instruct open to open the file
for reading, or for writing, or for both reading and writing, to create the file if it doesn�t exist, and
to truncate the file to zero length.

Now it should be clear why it is helpful that fork and exec are separate calls: between the
two, the shell has a chance to redirect the child�s I/O without disturbing the I/O setup of the main
shell. One could instead imagine a hypothetical combined forkexec system call, but the options

14

for doing I/O redirection with such a call seem awkward. The shell could modify its own I/O
setup before calling forkexec (and then un-do those modifications); or forkexec could take
instructions for I/O redirection as arguments; or (least attractively) every program like cat could
be taught to do its own I/O redirection.

Although fork copies the file descriptor table, each underlying file offset is shared between
parent and child. Consider this example:

if(fork() == 0) {
write(1, "hello ", 6);
exit (0);

} else {
wait (0);
write(l, "world\n", 6);

}

At the end of this fragment, the file attached to file descriptor 1 will contain the data hello world.
The write in the parent (which, thanks to wait, runs only after the child is done) picks up where
the child�s write left off. This behavior helps produce sequential output from sequences of shell
commands, like (echo hello; echo world) >output.txt.

The dup system call duplicates an existing file descriptor, returning a new one that refers to
the same underlying I/O object. Both file descriptors share an offset, just as the file descriptors
duplicated by fork do. This is another way to write hello world into a file:

fd = dup(1);
write(1, "hello ", 6);
write(fd, "world\n", 6);

Two file descriptors share an offset if they were derived from the same original file descriptor
by a sequence of fork and dup calls. Otherwise file descriptors do not share offsets, even if they
resulted from open calls for the same file. Dup allows shells to implement commands like this:
ls existing-file non-existing-file > tmp1 2>61. The 2>�1 tells the shell to give the
command a file descriptor 2 that is a duplicate of descriptor 1. Both the name of the existing file
and the error message for the non-existing file will show up in the file tmp1. The xv6 shell doesn�t
support I/O redirection for the error file descriptor, but now you know how to implement it.

File descriptors are a powerful abstraction, because they hide the details of what they are con-
nected to: a process writing to file descriptor 1 may be writing to a file, to a device like the console,
or to a pipe.

1.3 Pipes

A pipe is a small kernel buffer exposed to processes as a pair of file descriptors, one for reading
and one for writing. Writing data to one end of the pipe makes that data available for reading from
the other end of the pipe. Pipes provide a way for processes to communicate.

The following example code runs the program wc with standard input connected to the read
end of a pipe.

15

int p[2];
char xargv[2];

argv[0O] = "wc";
argv[1] = 0;

pipe (p);
if (fork

c
c
exec ("/bin/wce", argv);

} else {
close (p[0]);
write (p[1]

c

, �hello world\n", 12);
lose(p[1]);

}

The program calls pipe, which creates a new pipe and records the read and write file descriptors
in the array p. After fork, both parent and child have file descriptors referring to the pipe. The
child calls close and dup to make file descriptor zero refer to the read end of the pipe, closes the
file descriptors in p, and calls exec to run wc. When we reads from its standard input, it reads from
the pipe. The parent closes the read side of the pipe, writes to the pipe, and then closes the write
side.

If no data is available, a read on a pipe waits for either data to be written or for all file descrip-
tors referring to the write end to be closed; in the latter case, read will return 0, just as if the end of
a data file had been reached. The fact that read blocks until it is impossible for new data to arrive
is one reason that it�s important for the child to close the write end of the pipe before executing
wc above: if one of wc �s file descriptors referred to the write end of the pipe, wc would never see
end-of-file.

The xv6 shell implements pipelines such as grep fork sh.c | wc �1inamanner similar
to the above code (user/sh.c:100). The child process creates a pipe to connect the left end of the
pipeline with the right end. Then it calls fork and runcmd for the left end of the pipeline and
fork and runcmd for the right end, and waits for both to finish. The right end of the pipeline
may be a command that itself includes a pipe (e.g., a | b | c), which itself forks two new child
processes (one for b and one for c). Thus, the shell may create a tree of processes. The leaves
of this tree are commands and the interior nodes are processes that wait until the left and right
children complete.

In principle, one could have the interior nodes run the left end of a pipeline, but doing so
correctly would complicate the implementation. Consider making just the following modifica-
tion: change sh.c to not fork for p->left and run runcmd(p->left) in the interior pro-
cess. Then, for example, echo hi | wc won�t produce output, because when echo hi exits
in runcmd, the interior process exits and never calls fork to run the right end of the pipe. This

16

incorrect behavior could be fixed by not calling exit in runcmd for interior processes, but this
fix complicates the code: now runcmd needs to know if it a interior process or not. Complications
also arise when not forking for runcmd (p->right). For example, with just that modification,
sleep 10 | echo hi will immediately print �hi� instead of after 10 seconds, because echo
runs immediately and exits, not waiting for sleep to finish. Since the goal of the sh.c is to be as
simple as possible, it doesn�t try to avoid creating interior processes.

Pipes may seem no more powerful than temporary files: the pipeline

echo hello world | we
could be implemented without pipes as
echo hello world >/tmp/xyz; we </tmp/xyz

Pipes have at least four advantages over temporary files in this situation. First, pipes automatically
clean themselves up; with the file redirection, a shell would have to be careful to remove /tmp/xyz
when done. Second, pipes can pass arbitrarily long streams of data, while file redirection requires
enough free space on disk to store all the data. Third, pipes allow for parallel execution of pipeline
stages, while the file approach requires the first program to finish before the second starts. Fourth,
if you are implementing inter-process communication, pipes� blocking reads and writes are more
efficient than the non-blocking semantics of files.

1.4 File system

The xv6 file system provides data files, which contain uninterpreted byte arrays, and directories,
which contain named references to data files and other directories. The directories form a tree,
starting at a special directory called the root. A path like /a/b/c refers to the file or directory
named c inside the directory named b inside the directory named a in the root directory /. Paths
that don�t begin with / are evaluated relative to the calling process�s current directory, which can
be changed with the chdir system call. Both these code fragments open the same file (assuming
all the directories involved exist):

chdir("/a");
chdir("b");
open ("c", O_RDONLY);

open ("/a/b/c", O_RDONLY) ;

The first fragment changes the process�s current directory to /a/b; the second neither refers to nor
changes the process�s current directory.

There are system calls to create new files and directories: mkdir creates a new directory, open
with the O_CREATE flag creates a new data file, and mknod creates a new device file. This example
illustrates all three:

mkdir("/dir");
fd = open(" /dir/file", O_CREATE|O_WRONLY) ;
close (fd);

17

mknod("/console", 1, 1);

Mknod creates a special file that refers to a device. Associated with a device file are the major and
minor device numbers (the two arguments to mknod), which uniquely identify a kernel device.
When a process later opens a device file, the kernel diverts read and write system calls to the
kernel device implementation instead of passing them to the file system.

A file�s name is distinct from the file itself; the same underlying file, called an inode, can have
multiple names, called Jinks. Each link consists of an entry in a directory; the entry contains a file
name and a reference to an inode. An inode holds metadata about a file, including its type (file or
directory or device), its length, the location of the file�s content on disk, and the number of links to
a file.

The fstat system call retrieves information from the inode that a file descriptor refers to. It
fills ina struct stat, defined in stat .h (kernel/stat.h) as:

#define T_DIR 1 // Directory
#define T_FILE 2 // File
#define T_DEVICE 3 // Device

struct stat {
int dev; // File system�s disk device
uint ino; // Inode number
short type; // Type of file
short nlink; // Number of links to file
uint64 size; // Size of file in bytes
by

The 1ink system call creates another file system name referring to the same inode as an exist-
ing file. This fragment creates a new file named both a and b.

open ("
link ("

", O_CREATE |O_WRONLY) ;
" Mb") >
' 7

a
a
Reading from or writing to a is the same as reading from or writing to b. Each inode is identified
by a unique inode number. After the code sequence above, it is possible to determine that a and b
refer to the same underlying contents by inspecting the result of fst at: both will return the same
inode number (ino), and the nlink count will be set to 2.

The unlink system call removes a name from the file system. The file�s inode and the disk

space holding its content are only freed when the file�s link count is zero and no file descriptors
refer to it. Thus adding

unlink ("a");
to the last code sequence leaves the inode and file content accessible as b. Furthermore,

fd = open("/tmp/xyz", O_CREATE|O_RDWR) ;
unlink ("/tmp/xyz") ;

is an idiomatic way to create a temporary inode with no name that will be cleaned up when the
process closes fd or exits.

18
    """
    page_num = 1
    paragraph_num = 1
    db = create_database()
    embeddings = create_embeddings_model()
    pdf_name = None
    page_num_start = 1
    page_num_end = 5


    # Post the text into knowledge base
    context_posted: bool = post_context(context, page_num, paragraph_num, db, embeddings, pdf_name)

    #Get the specific context we will use in flashcards (ie. all context from page range)
    specific_context = get_page_range(pdf_name, page_num_start, page_num_end)

    # Generate flashcards from the text
    flashcards = generate_flashcards(specific_context)
    return flashcards


def process_answer(user_input: str) -> str:
    #This will answer a query only based on the list of closest correct answers from the data provided:

    #Generate the embedding for the user input
    embedding = create_embeddings_model()
    #Get a list of answers from the database
    curriculum_list = mongodb.get_curriculum(embedding)
    #Use this list to generate a response
    answer_GPT = response_formulation(user_input, curriculum_list)

    return answer_GPT
