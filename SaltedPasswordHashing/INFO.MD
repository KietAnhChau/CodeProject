# Salted Password Hashing

<p>Password hashing is the process of converting a password into a fixed-length string of characters that cannot be easily interpreted by a human or decoded quickly by an unauthorized machine.</p>

<p>According to crackstation</p>
<p>The general workflow for account registration and authentication in a hash-based account system is as follows:</p>
<ol>
	<li>The user creates an account.</li>
	<li>Their password is hashed and stored in the database. At no point is the plain-text (unencrypted) password ever written to the hard drive.</li>
	<li>When the user attempts to login, the hash of the password they entered is checked against the hash of their real password (retrieved from the database).</li>
	<li>If the hashes match, the user is granted access. If not, the user is told they entered invalid login credentials.</li>
	<li>Steps 3 and 4 repeat every time someone tries to login to their account.</li>
</ol>

<h2>The Basics: Hashing with Salt</h2>
Salt should be generated using a Cryptographically Secure Pseudo-Random Number Generator (CSPRNG)

Python: <a href="https://docs.python.org/3/library/secrets.html">Secret</a><br>
Dot NET (C#, VB): <a href="https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.rngcryptoserviceprovider?redirectedfrom=MSDN&view=net-7.0">System.Security.Cryptography.RNGCryptoServiceProvider</a><br>
Java: <a href="http://docs.oracle.com/javase/6/docs/api/java/security/SecureRandom.html">java.security.SecureRandom</a><br>

## Document
python: https://docs.python.org/3/library/secrets.html

## Reference
<a href="https://crackstation.net/hashing-security.htm">Salted Password Hashing - Doing it Right</a>