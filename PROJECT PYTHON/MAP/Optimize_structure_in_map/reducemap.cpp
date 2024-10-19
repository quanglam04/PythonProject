#include<iostream>
#include<fstream>
#include<vector>
#include<map>
using namespace std;
string optimize_name(string s){
    int i=s.size()-1; 
    while (s[i] !=  '\\' ) i--;
	i++;
	string tmp="";
	for (;i<s.size();i++){
		if(s[i] !='.' ) tmp=tmp+s[i];
		else break;
	}
	return tmp+"optimize.txt";
}
int main (int argc,char* argv[] ){

	if (argc != 2) {
        cout << "Please enter file path" << endl;
        return 1;
    }
	string filepath = argv[1];
    for (int i = 0; i < filepath.length(); i++) {
        if (filepath[i] == '\\') {
            filepath.insert(i, "\\");
            i++;
        }
    }
	vector<string> v;
	fstream f(filepath);
	string s;
	int pre_string_size=0;
	while(f>>s){
		v.push_back(s);
		if (pre_string_size != 0  && pre_string_size !=s.size() ){
			cout<<"Your map is having a size error, please check at the link  \"..\\ pythonproject \\ project python \\ map \" ";
			return 0;
		}
		pre_string_size=s.size();
	}
	f.close();
	map<pair<int,int> , int> mp_width,mp_height;
	int visited[v.size()+1][s.size()+1] ={0};
	
	for (int i=0;i<v.size();i++) {
		for (int j=0;j<s.size();j++){
			if (!visited[i][j] && v[i][j]=='1'  ) {
				visited[i][j]=1;
				j=j+1;
				int width=1;
				while ( j<v[i].size()  and v[i][j]=='1'  ) {
					width++;
					visited[i][j]=3;
					j++;
				}
				if (width==1) visited[i][j-1]=2;
				mp_width[make_pair(i,j-width)]=width;
			}	
		}
	}
	

	map<pair<int,int>, int>::iterator it; 
	for (it=mp_width.begin();it!=mp_width.end();it++){
		pair<int,int> p = it->first;
		int i=p.first,j=p.second;
		int height =0; 
		if (visited[i][j]==1 || visited[i][j]==2 ){
			while (i<v.size() and v[i][j]=='1'){
				height++;
				i++;
				if(visited[i][j] !=1) visited[i][j]=3;
			}
				
		}

		mp_height[p]=height;
	}
	string res=optimize_name(filepath);
	ofstream of(res);
	if (of.is_open()){
		for (int i=0;i<v.size();i++){
			for (int j=0;j<s.size();j++){
				if(v[i][j]=='1' && visited[i][j] <3 && visited[i][j]>0 ){
					pair<int,int>p ={i,j}; 
					if (mp_width[p] >1 and mp_height[p]==1 ) mp_height[p]=0;
					else if(mp_width[p] ==1 and mp_height[p] >1  ) mp_width[p]=0;
					if (mp_width[p] !=0 )  of<<"("<<j<<", "<<i<<", "<<mp_width[p]<<", 1),"<<endl;
					if (mp_height[p] !=0 ) of<<"("<<j<<", "<<i<<", 1, "<<mp_height[p]<<"),"<<endl;
				}
		   	}
	    }
		of.close();		
  	}
  	else{
  	    cout<<"Can't read";	
	} 


	

}
