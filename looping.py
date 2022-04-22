# Perulangan (loop)

# for kondisi:
# 	aksi

# isi dengan list
angka2_list = [1,3,5,7,9] 
print(angka2_list)

print("\n Program 1 ")
for i in angka2_list:
	print(f"i sekarang -> {i}")



# ini dengan range
angka2_range = range(13)
print("\n Program 2 ")
for i in angka2_range:
	print(f"i sekarang -> {i}")



angka2_range = range(5,10)
print("\n Program 3 ")
for i in angka2_range:
	print(f"i sekarang -> {i}")
	# print("saya keren")

# menggunakan string

data_str = "saya suka belajar"
print("\n Program 4 ")
for huruf in data_str:
	print(huruf)