import hashlib;
import passlib.hash;
import bcrypt;
from time import time;

salt="ZDzPE45C"
string="hello"
stringb=bytes(string.encode())
salt2="1111111111111111111111"
#generate salt for bcypt library from salt2
# = b"$2b$12$1111111111111111111111"
salt4 = bytes(f"$2b$12${salt2}".encode())

print ("**** General Hashes")
start = time()
md5 = hashlib.md5(string.encode()).hexdigest()
end = time()
print ("\tMD5:", md5)
print ("\t\tLength:", len(md5))
print ("\t\tTime:", end - start)

start = time()
sha1 = hashlib.sha1(string.encode()).hexdigest()
end = time()
print ("\tSHA1:", sha1)
print ("\t\tLength:", len(sha1))
print ("\t\tTime:", end - start)

start = time()
sha2 = hashlib.sha256(string.encode()).hexdigest()
end = time()
print ("\tSHA256:", sha2)
print ("\t\tLength:", len(sha2))
print ("\t\tTime:", end - start)

start = time()
sha5 = hashlib.sha512(string.encode()).hexdigest()
end = time()
print ("\tSHA512:", sha5)
print ("\t\tLength:", len(sha5))
print ("\t\tTime:", end - start)

print ("**** Hashes (with salt)")

start = time()
des = passlib.hash.des_crypt.hash(string, salt=salt[:2])
end = time()
print ("\tDES:", des)
print ("\t\tLength:", len(des))
print ("\t\tTime:", end - start)

start = time()
md5salt = passlib.hash.md5_crypt.hash(string, salt=salt)
end = time()
print ("\tMD5:",md5salt)
print ("\t\tLength:", len(md5salt))
print ("\t\tTime:", end - start)

start = time()
sunmd5 = passlib.hash.sun_md5_crypt.hash(string, salt=salt)
end = time()
print ("\tSun MD5:", sunmd5)
print ("\t\tLength:", len(sunmd5))
print ("\t\tTime:", end - start)

start = time()
apr1 = passlib.hash.apr_md5_crypt.hash(string, salt=salt)
end = time()
print ("\tAPR1:",apr1)
print ("\t\tLength:", len(apr1))
print ("\t\tTime:", end - start)

start = time()
sha1salt = passlib.hash.sha1_crypt.hash(string, salt=salt)
end = time()
print ("\tSHA1:", sha1salt)
print ("\t\tLength:", len(sha1salt))
print ("\t\tTime:", end - start)

start = time()
sha2salt = passlib.hash.sha256_crypt.hash(string, salt=salt)
end = time()
print ("\tSHA256:", sha2salt)
print ("\t\tLength:", len(sha2salt))
print ("\t\tTime:", end - start)

start = time()
sha5salt = passlib.hash.sha512_crypt.hash(string, salt=salt)
end = time()
print ("\tSHA512:", sha5salt)
print ("\t\tLength:", len(sha5salt))
print ("\t\tTime:", end - start)

start = time()
phpass = passlib.hash.phpass.hash(string, salt=salt)
end = time()
print ("\tPHPASS:",phpass)
print ("\t\tLength:", len(phpass))
print ("\t\tTime:", end - start)

start = time()
PBKDF2sha1 =passlib.hash.pbkdf2_sha1.hash(string, salt=salt.encode())
end = time()
print ("\tPBKDF2 (SHA1):",PBKDF2sha1)
print ("\t\tLength:", len(PBKDF2sha1))
print ("\t\tTime:", end - start)

start = time()
PBKDF2sha2 =passlib.hash.pbkdf2_sha256.hash(string, salt=salt.encode())
end = time()
print ("\tPBKDF2 (SHA2):",PBKDF2sha2)
print ("\t\tLength:", len(PBKDF2sha2))
print ("\t\tTime:", end - start)

#print ("PBKDF2 (SHA512):",passlib.hash.pbkdf2_sha512.encrypt(string, salt=salt))
#print ("CTA PBKDF2:",passlib.hash.cta_pbkdf2_sha1.encrypt(string, salt=salt))
#print ("DLITZ PBKDF2:",passlib.hash.dlitz_pbkdf2_sha1.encrypt(string, salt=salt))

print ("**** MS Windows Hashes")

start = time()
lmhash = passlib.hash.lmhash.hash(string)
end = time()
print ("\tLM Hash:",lmhash)
print ("\t\tLength:", len(lmhash))
print ("\t\tTime:", end - start)

start = time()
nthash =passlib.hash.nthash.hash(string)
end = time()
print ("\tNT Hash:",nthash)
print ("\t\tLength:", len(nthash))
print ("\t\tTime:", end - start)

start = time()
msdcc=passlib.hash.msdcc.hash(string, salt)
end = time()
print ("\tMS DCC:",msdcc)
print ("\t\tLength:", len(msdcc))
print ("\t\tTime:", end - start)

start = time()
msdcc2=passlib.hash.msdcc2.hash(string, salt)
end = time()
print ("\tMS DCC2:",msdcc2)
print ("\t\tLength:", len(msdcc2))
print ("\t\tTime:", end - start)

start = time()
ldapmd5=passlib.hash.ldap_hex_md5.hash(string)
end = time()
print ("\tLDAP (Hex MD5):",ldapmd5)
print ("\t\tLength:", len(ldapmd5))
print ("\t\tTime:", end - start)

start = time()
ldapsha1=passlib.hash.ldap_hex_sha1.hash(string)
end = time()
print ("\tLDAP (Hex SHA1):",ldapsha1)
print ("\t\tLength:", len(ldapsha1))
print ("\t\tTime:", end - start)

start = time()
ldaplass=passlib.hash.atlassian_pbkdf2_sha1.hash(string)
end = time()
print ("\tLDAP (At Lass):",ldaplass)
print ("\t\tLength:", len(ldaplass))
print ("\t\tTime:", end - start)

start = time()
ldapfshp=passlib.hash.fshp.hash(string)
end = time()
print ("\tLDAP (FSHP):",ldapfshp)
print ("\t\tLength:", len(ldapfshp))
print ("\t\tTime:", end - start)

print ("**** Database Hashes")

start = time()
mssql2000=passlib.hash.mssql2000.hash(string)
end = time()
print ("\tMS SQL 2000:",mssql2000)
print ("\t\tLength:", len(mssql2000))
print ("\t\tTime:", end - start)

start = time()
mssql2005=passlib.hash.mssql2005.hash(string)
end = time()
print ("\tMS SQL 2005:",mssql2005)
print ("\t\tLength:", len(mssql2005))
print ("\t\tTime:", end - start)

start = time()
mysql323=passlib.hash.mysql323.hash(string)
end = time()
print ("\tMySQL 323:",mysql323)
print ("\t\tLength:", len(mysql323))
print ("\t\tTime:", end - start)

start = time()
mysql=passlib.hash.mysql41.hash(string)
end = time()
print ("\tMySQL:",mysql)
print ("\t\tLength:", len(mysql))
print ("\t\tTime:", end - start)

start = time()
postgres=passlib.hash.postgres_md5.hash(string, user=salt)
end = time()
print ("\tPostgres (MD5):",postgres)
print ("\t\tLength:", len(postgres))
print ("\t\tTime:", end - start)

start = time()
oracle10=passlib.hash.oracle10.hash(string, user=salt)
end = time()
print ("\tOracle 10:",oracle10)
print ("\t\tLength:", len(oracle10))
print ("\t\tTime:", end - start)

start = time()
oracle11=passlib.hash.oracle11.hash(string)
end = time()
print ("\tOracle 11:",oracle11)
print ("\t\tLength:", len(oracle11))
print ("\t\tTime:", end - start)

print ("**** Other Known Hashes")

start = time()
ciscopix=passlib.hash.cisco_pix.hash(string, user=salt)
end = time()
print ("\tCisco PIX:",ciscopix)
print ("\t\tLength:", len(ciscopix))
print ("\t\tTime:", end - start)

start = time()
cisotype7=passlib.hash.cisco_type7.hash(string)
end = time()
print ("\tCisco Type 7:",cisotype7)
print ("\t\tLength:", len(cisotype7))
print ("\t\tTime:", end - start)

start = time()
dyangodes=passlib.hash.django_des_crypt.hash(string, salt=salt)
end = time()
print ("\tDyango DES:",dyangodes)
print ("\t\tLength:", len(dyangodes))
print ("\t\tTime:", end - start)

start = time()
djangomd5=passlib.hash.django_salted_md5.hash(string, salt=salt[:2])
end = time()
print ("\tDjango MD5:",djangomd5)
print ("\t\tLength:", len(djangomd5))
print ("\t\tTime:", end - start)

start = time()
dyangosha1=passlib.hash.django_salted_sha1.hash(string, salt=salt)
end = time()
print ("\tDjango SHA1:",dyangosha1)
print ("\t\tLength:", len(dyangosha1))
print ("\t\tTime:", end - start)

start = time()
dyangobcrypt=passlib.hash.django_bcrypt.hash(string,salt=salt2)
end = time()
print ("\tDjango Bcrypt:", dyangobcrypt)
print ("\t\tLength:", len(dyangobcrypt))
print ("\t\tTime:", end - start)

start = time()
dyangopbkdf2sha1=passlib.hash.django_pbkdf2_sha1.hash(string, salt=salt)
end = time()
print ("\tDjango PBKDF2 SHA1:", dyangopbkdf2sha1)
print ("\t\tLength:", len(dyangopbkdf2sha1))
print ("\t\tTime:", end - start)

start = time()
dyangopbkdf2sha2=passlib.hash.django_pbkdf2_sha256.hash(string, salt=salt)
end = time()
print ("\tDjango PBKDF2 SHA2:", dyangopbkdf2sha2)
print ("\t\tLength:", len(dyangopbkdf2sha2))
print ("\t\tTime:", end - start)

#print ("\tBcrypt:"+passlib.hash.bcrypt.hash(string, salt=salt2[:22]))
start = time()
salt3 = bcrypt.gensalt(rounds=16)
bcrypt = bcrypt.hashpw(stringb, salt4).decode()
end = time()
print ("\tBcrypt library:", bcrypt)
print ("\t\tLength:", len(bcrypt))
print ("\t\tTime:", end - start)