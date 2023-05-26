# RandomNumber

/dev/urandom is a special file in Unix-like operating systems that serves as a cryptographically secure pseudorandom number generator. 
It allows access to environmental noise collected from device drivers and other sources. 
/dev/random and /dev/urandom are similar, but /dev/random blocks if there is not enough entropy available, while /dev/urandom never blocks.


How To Safely Generate A Random Number
<a href="https://sockpuppet.org/blog/2014/02/25/safely-generate-random-numbers/">How To Safely Generate A Random Number</a>