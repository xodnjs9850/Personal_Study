import os
import hashlib
import pefile

#Scan Virus
def ScanVirus(vdb, vsize, sdb, fname) :
	ret, vname = ScanHash(vdb, vsize, fname)
	if ret == True :
		return ret, vname

	fp = open(fname, 'rb')
	for t in sdb :
		if ScanStr(fp, t[0], t[1]) == True :
			ret = True
			vname = t[2]
			break
	fp.close()
	return ret, vname

#Chack Virus
def SearchVDB(vdb, fmd5):
	for t in vdb:
		if t[0] == fmd5:
			return True, t[1]

	return False, ''

#HASH Scan
def ScanHash(vdb, vsize, fname):
	ret = False
	vname = ''

	size = os.path.getsize(fname)
	if vsize.count(size) :
		file = pefile.PE(fname)
		fmd5 = file.get_imphash()
		file.close()

		ret, vname = SearchVDB(vdb, fmd5)
		
	return ret, vname

#Location Search
def ScanStr(fp, offset, mal_str) :
	size = len(mal_str)

	fp.seek(offset)
	buf = fp.read(size)
	buf = buf.decode()
		
	if buf == mal_str :
		return True
	else :
		return False

