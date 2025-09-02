default_file="content/temp_summary.txt"

def Write_to_file(content,filename=default_file):
  
  f=open(filename,"w")
  f.write(content)
  f.close

def Read_to_file(filename=default_file):
  f=open(filename,"r")
  content=f.read()
  f.close
  return content

if __name__ == "__main__":
  print("File handle tester executing: ")
  print("Format")
  print("Read: 1,filename(optional)")
  print("Write: 2,content,filename(optional) \n")
  while True:
    userinput=input()
    splitted_input=userinput.split(',')
    if splitted_input[0]=="1":
        if len(splitted_input)>1:
            print(Read_to_file(splitted_input[1]))
        else:
           print(Read_to_file())
 
    elif splitted_input[0]=="2":
        if len(splitted_input)>2:
           Write_to_file(splitted_input[1],splitted_input[2])

        else:
           Write_to_file(splitted_input[1])
    elif splitted_input[0]=="quit":
       break
    else:
       print("Improper syntax \n")