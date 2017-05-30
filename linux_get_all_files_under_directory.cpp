#include <unistd.h>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>
#include <dirent.h> 
#include <sys/stat.h>  



void getFiles(string path,string exd,vector<string>& files)
{
    string p;
    struct stat statbuf;
    // check the parameter !
    if( NULL == path.c_str() )
    {
        std::cout<<" dir_name is null ! "<<std::endl;
        return;
    }

    // check if dir_name is a valid dir
    struct stat s;
    lstat( path.c_str() , &s );
    if( ! S_ISDIR( s.st_mode ) )
    {
        std::cout<<"path is not a valid directory !"<<std::endl;
        return;
    }

    struct dirent * filename;    // return value for readdir()
    DIR * dir;                   // return value for opendir()
    dir = opendir( path.c_str() );
    if( NULL == dir )
    {
        std::cout<<"Can not open dir "<<path<<endl;
        return;
    }
    std::cout<<"Successfully opened the dir !"<<std::endl;

    /* read all the files in the dir ~ */
    while( ( filename = readdir(dir) ) != NULL )
    {
     string temp_name = p.assign(path).append("/").append(filename->d_name);
	 lstat(temp_name.c_str(), &statbuf); // 
         if(S_IFDIR &statbuf.st_mode)    // 
         {
            if (strcmp(".", filename->d_name) == 0 || strcmp("..",filename->d_name) == 0)
              continue;
            printf("%s/\n",  filename->d_name);  // 
            getFiles( p.assign(path).append("/").append(filename->d_name), exd, files);              //
         }
	 else{
		if (string(filename->d_name).find(exd) != string::npos){
           		files.push_back(p.assign(path).append("/").append(filename->d_name));
		 }
	     }
        //cout<<filename ->d_name <<endl;
    }
}
