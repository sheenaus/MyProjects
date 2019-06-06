import os,glob
from flask import Flask, render_template, request,jsonify
from flask import flash
import pypyodbc
import json
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
def splitfile(filepath,limit):
    lines_per_file =limit
    smallfile = None
    with open(filepath) as bigfile:
        for lineno, line in enumerate(bigfile):
            if lineno % lines_per_file == 0:
                if smallfile:
                    smallfile.close()
                small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file)
                smallfile = open(os.getcwd()+'\\'+small_filename, "w")
            smallfile.write(line)
        if smallfile:
            smallfile.close()
    return()

def sort_file(file_indx):
    i=file_indx
    files = glob.glob(os.getcwd() + '\small_*.txt')
    #print(files)
    for file in files:
        lines=[]
        file1=open(file)
        wfile = open(os.getcwd() + '\sortfile_'+str(i)+'.txt',"w+")
        for line in file1 :
            lines.append(int(line.rstrip()))
        lines.sort()
        #print(file)
        file1.close()
        for line in lines:
            wfile.write(str(line)+'\n')
        wfile.close()
        i=i+file_indx
    return()
def mergesort(rec_limit):
    files = glob.glob(os.getcwd() + '\sortfile_*.txt')
    i = 0
    list = []
    list1 = []
    while (1):
        list = []
        list1 = []
        for file in files:
            f = open(file)
            # list=list+list1
            list1 = f.readlines()[i:i + rec_limit]
            for l in list1:
                list.append(int(l.rstrip()))
            f.close()
        list.sort()
        # print(list)
        wfile = open(os.getcwd() + '\\NewSortedfile.txt', "a")
        for line in list:
            wfile.write(str(line) + '\n')
        wfile.close()
        i = i + rec_limit
        if len(list) == 0:
            # print(len(list))
            break
    print('completed')
    return()

@app.route("/")
def index():
    return render_template("Sortfileupload.html")
@app.route("/upload", methods=['POST'])
def upload():
    print(APP_ROOT)
    target = os.path.join(APP_ROOT, 'sort/')
    print("hello")

    if not os.path.isdir(target):
        os.mkdir(target)
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print('iam herr'+destination)
        file.save(destination)
    cwd =os.getcwd()
    print(cwd)
    json_file_path= destination###'%s/%s' %(cwd,'Emp.json')
    print(json_file_path)
    rec_limt=1000
    file_indx=10
    list_limit=500
    splitfile(json_file_path,rec_limt)
    sort_file(file_indx)
    mergesort(list_limit)
    return (render_template("complete.html"))

if __name__ == '__main__':
    app.run(debug='True')



