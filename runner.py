import VASFile

vf1 = VASFile.VASFile('C:\\Users\\vasun\\Documents\\intern_docs\\cpp-dependencies-master\\cpp-dependencies-master\\src\\Configuration.cpp')
vf1.get_content()
vf1.get_dependencies()
print(vf1.dependencies)