#Finding no users: it assumes that aws configure output format is json
try:
    import subprocess
    import json
    import sys
    print("All required modules are imported successfully")
except Exception as e:
    print("The error is: {}".format(e))
    print("The script is going to terminate")
    sys.exit(1)
def list_of_users():
    users_list = [ ]
    cmd = "aws iam list-users"
    sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    rt = sp.wait()
    out,err = sp.communicate()
    if rt:
	print("The cmd: {} is faild to execute".format(cmd))
  	print("The error is: {}".format(err))
    else:
	#print("The output is: {}".format(out))
	out = json.loads(out)
	out_user_details = out.get('Users')
	for dict in out_user_details:
	    for key,value in dict.items():
	    	if key == "UserName" and value not in users_list:
		    users_list.append(value)
    return json.dumps(users_list)
		    
			
def main():
    print("The list_of_users are : {}".format(list_of_users()))
if __name__ == "__main__":
    main()
