import os
from subprocess import check_output
base_dir = "/home/madisnit/Desktop/git/test4"
print base_dir
def excute_file():
	test = []
	os.chdir(base_dir+"/data")
	for i in os.listdir('.'):
		if i.endswith(".py"):
			test.append(i)
	for files in test:
		cmd = 'python'+' '+ files
		test = check_output(cmd,shell=True)	
	return test
if __name__ == "__main__":
	excute_file()
