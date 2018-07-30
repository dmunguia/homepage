import resource 
from timeit import timeit

MEM_SIZE = 64 * 1024 * 1024

FLD_ActionGeo_CountryCode = 51
FLD_Actor1CountryCode = 7
FLD_Actor2CountryCode = 17
FLD_QuadClass = 29
FLD_SOURCEURL = 57

resource.setrlimit(resource.RLIMIT_AS, (MEM_SIZE, MEM_SIZE))

def ordenar_en_sitio(nombre_archivo_entrada, nombre_archivo_salida):
	# implementación del ejercicio #1
	return None


def agrupacion(nombre_archivo):	
	url = ''
	num_paises = 0
	# implementación del ejercicio #2
	return (url, num_paises)


def comprimir(nombre_archivo_entrada, nombre_archivo_comprimido):
	# implementación de puntos extra
	return None


def descomprimir(nombre_archivo_comprimido, nombre_archivo_salida):
	# implementación de puntos extra
	return None


print(timeit('ordenar_en_sitio("GDELT_20170511.export.csv", "GDELT_20170511.export.sorted.csv")', setup="from examen03 import ordenar_en_sitio", number = 1))
print(timeit('agrupacion("GDELT_20170511.export.sorted.csv")', setup="from examen03 import agrupacion", number = 1))
print(timeit('comprimir("GDELT_20170511.export.sorted.csv", "GDELT_20170511.export.sorted.huffman")', setup="from examen03 import comprimir", number = 1))
print(timeit('descomprimir("GDELT_20170511.export.sorted.huffman", "GDELT_20170511.export.sorted.csv")', setup="from examen03 import descomprimir", number = 1))

