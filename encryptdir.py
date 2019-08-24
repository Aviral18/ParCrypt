import os, random, struct, hashlib, json
import threading, time, thread
from Crypto.Cipher import AES


def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    
    if not out_filename:
        out_filename = in_filename + '@'

    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))
    os.remove(in_filename)
def decrypt_file(key, in_filename, filename, out_filename=None, chunksize=24*1024):
    
    if not out_filename:
        out_filename = filename.replace('@','')

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)
    os.remove(in_filename)
def renamefiles(pth):
	os.chdir(pth)
	ls=os.listdir(pth)
	index={}
	for a in ls:
		temp=a
		b=os.urandom(32).encode('hex')
		index[temp]=b
		os.rename(a,b)
	j=json.dumps(index)
	f=open("index.json","w")
	f.write(j)
	f.close()
		
def main(ps, pth, op):
	#ps=raw_input("Enter the key : ")
	key = hashlib.sha256(ps).digest()
	#pth=raw_input("Enter the path : ")
	os.chdir(pth)
	dirs=os.listdir(pth)
	#op=int(raw_input("Encrypt(0) or Decrypt(1) "))
	if(op==0) : 
		for in_filename in dirs :
			t=threading.Thread(target=encrypt_file,args=(key, in_filename,))
			t.start()
			t.join()
		print("Encrypted")
		renamefiles(pth)
		
	else :
		indexfile=open("index.json","r")
		newindex=json.load(indexfile)
		#print(newindex)
		infiles=list(newindex.values())
		outfiles=list(newindex.keys())
		dirs.remove('index.json')
		for i in dirs :
			in_filename=outfiles[infiles.index(i)]
			#print (in_filename)
			t=threading.Thread(target=decrypt_file,args=(key, i, in_filename,))
			t.start()
			t.join()
			#os.remove(i)
		print("Decrypted")
	
