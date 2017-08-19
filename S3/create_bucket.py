try:
    #print"This is import section"
    import subprocess
    import sys
    print("imported all modules successfully")
except Exception as e:
    print("The error is: {}".format(e))
    sys.exit(1)

def create_bucket(bucket_name):
    #bucket_name = raw_input("Enter bucket_name : ")
    try:
        cmd = "aws s3 mb s3://" + bucket_name
        print("The cmd is: {}".format(cmd))
        sp = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        rt=sp.wait()
        #print("The rt code is: ",rt)
        out,err = sp.communicate()
        if not rt:
            print("The out is: ",out)
        else:
            print("The err is: ",err)
            sys.exit(3)
    except Exception as e:
        print("The error is: {}".format(e))
def main(bucket_name):
    #print("This is main function")
    create_bucket(bucket_name)
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("The usage of this program is: {}   <bucket_name>".format(sys.argv[0]))
        sys.exit(2)
    else:
        sys.exit(main(sys.argv[1]))
