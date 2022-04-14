from struct import unpack

def ColorConversion(Y, Cr, Cb):
	#Converts Y, Cr and Cb to RGB color space
    R = Cr * (2 - 2 * 0.299) + Y
    B = Cb * (2 - 2 * 0.114) + Y
    G = (Y - 0.114 * B - 0.299 * R) / 0.587
    return (Clamp(R + 128), Clamp(G + 128), Clamp(B + 128))

def Clamp(col):
	col = 255 if col>255 else col
	col = 0 if col<0 else col
	return  int(col)

def PrintMatrix(m):
	#A convenience function for printing matrices
	for j in range(8):
		print("| ", end="")
		for i in range(8):
			print("% 3.4f " % m[i + j * 8], end="")
		print("|")

def RemoveFF00(data):
	#Removes 0x00 after 0xff in the image scan section of JPEG
	datapro = []
	i = 0
	while(True):
		b, bnext = unpack("BB",data[i:i+2])		
		if (b == 0xff):
			if (bnext != 0):
				break
			datapro.append(data[i])
			i+=2
		else:
			datapro.append(data[i])
			i+=1
	#print(i-3,i-2,i-1,i,i+1,i+2,i+3)
	#print(data[i-3:i+4].hex())
	return datapro, i

def DecodeNumber(code, bits):
    l = 2 ** (code - 1)	#就是二进制,B100000...(code位，code - 1个0）
    if bits >= l:
        return bits
    else:
        return bits - (2 * l - 1)
