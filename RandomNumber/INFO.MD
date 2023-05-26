# RandomNumber

<b>/dev/urandom<b> is a special file in Unix-like operating systems that serves as a cryptographically secure pseudorandom number generator. 
It allows access to environmental noise collected from device drivers and other sources. <br>
<b>/dev/random<b> and <b>/dev/urandom<b> are similar, but <b>/dev/random<b> blocks if there is not enough entropy available, while <b>/dev/urandom<b> never blocks.


## Reference
<a href="https://sockpuppet.org/blog/2014/02/25/safely-generate-random-numbers/">How To Safely Generate A Random Number</a>